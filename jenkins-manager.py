#!/usr/bin/env python3
"""List Jenkins jobs, inspect their latest builds, and trigger builds."""

import argparse
import base64
import json
import os
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


TIMEOUT_SECONDS = 20


class JenkinsError(Exception):
    """Raised when Jenkins configuration or an API request fails."""


class JenkinsClient:
    def __init__(self, base_url, username, api_token):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.api_token = api_token
        self.authorization = "Basic " + base64.b64encode(
            f"{username}:{api_token}".encode("utf-8")
        ).decode("ascii")

    def _request(self, url, method="GET", data=None, headers=None):
        request_headers = {
            "Authorization": self.authorization,
            "Accept": "application/json",
        }
        if headers:
            request_headers.update(headers)
        request = Request(url, data=data, headers=request_headers, method=method)

        try:
            with urlopen(request, timeout=TIMEOUT_SECONDS) as response:
                body = response.read()
                return response.status, response.headers, body
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace").strip()
            message = f"Jenkins zwrócił HTTP {error.code} dla {url}"
            if detail:
                message += f": {detail[:500]}"
            raise JenkinsError(message) from error
        except URLError as error:
            raise JenkinsError(f"Nie można połączyć się z Jenkins: {error.reason}") from error
        except TimeoutError as error:
            raise JenkinsError(f"Przekroczono limit czasu żądania do {url}") from error

    def _get_json(self, url):
        _, _, body = self._request(url)
        try:
            return json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise JenkinsError(f"Jenkins zwrócił nieprawidłowy JSON dla {url}") from error

    def _jobs_at(self, url, visited):
        if url in visited:
            return []
        visited.add(url)
        data = self._get_json(url + "/api/json?tree=jobs[name,url,color,_class]")
        jobs = []
        for job in data.get("jobs", []):
            jobs.append(job)
            job_class = job.get("_class", "")
            if job_class.endswith("Folder") or job_class.endswith("MultiBranchProject"):
                jobs.extend(self._jobs_at(job["url"].rstrip("/"), visited))
        return jobs

    def list_jobs(self):
        return self._jobs_at(self.base_url, set())

    def latest_build(self, job):
        details = self._get_json(
            job["url"].rstrip("/") + "/api/json?tree=lastBuild[number,result,building,url]"
        )
        return details.get("lastBuild")

    def _crumb_headers(self):
        crumb_url = self.base_url + "/crumbIssuer/api/json"
        try:
            _, _, body = self._request(crumb_url)
        except JenkinsError as error:
            if "HTTP 404" in str(error):
                return {}
            raise

        try:
            crumb_data = json.loads(body.decode("utf-8"))
            return {crumb_data["crumbRequestField"]: crumb_data["crumb"]}
        except (UnicodeDecodeError, json.JSONDecodeError, KeyError) as error:
            raise JenkinsError("Jenkins zwrócił nieprawidłową odpowiedź CSRF crumb") from error

    def trigger_build(self, job_name):
        job_url = self.base_url
        for segment in job_name.split("/"):
            if not segment:
                raise JenkinsError("Nazwa zadania nie może zawierać pustych segmentów")
            job_url += "/job/" + quote(segment, safe="")

        status, response_headers, _ = self._request(
            job_url + "/build",
            method="POST",
            data=b"",
            headers=self._crumb_headers(),
        )
        return status, response_headers.get("Location")


def create_client():
    base_url = os.environ.get("JENKINS_URL", "").strip()
    username = os.environ.get("JENKINS_USERNAME", "").strip()
    api_token = os.environ.get("JENKINS_API_TOKEN", "")
    if not base_url or not username or not api_token:
        raise JenkinsError(
            "Ustaw zmienne JENKINS_URL, JENKINS_USERNAME i JENKINS_API_TOKEN."
        )
    if not base_url.startswith(("http://", "https://")):
        raise JenkinsError("JENKINS_URL musi zaczynać się od http:// lub https://.")
    return JenkinsClient(base_url, username, api_token)


def main():
    parser = argparse.ArgumentParser(description="Zarządzanie zadaniami Jenkins przez API.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("jobs", help="Wyświetla zadania Jenkins.")
    subparsers.add_parser("status", help="Wyświetla status ostatnich buildów.")
    build_parser = subparsers.add_parser("build", help="Uruchamia wskazane zadanie.")
    build_parser.add_argument(
        "job_name",
        help="Nazwa zadania; zadania w folderach podaj jako Folder/Zadanie.",
    )
    args = parser.parse_args()

    try:
        client = create_client()
        if args.command == "jobs":
            jobs = client.list_jobs()
            for job in jobs:
                print(f"{job['name']} ({job['url']})")
            if not jobs:
                print("Nie znaleziono zadań.")
        elif args.command == "status":
            jobs = client.list_jobs()
            for job in jobs:
                if job.get("_class", "").endswith(("Folder", "MultiBranchProject")):
                    continue
                build = client.latest_build(job)
                if build is None:
                    print(f"{job['name']}: brak buildów")
                    continue
                state = "BUILDING" if build.get("building") else build.get("result", "UNKNOWN")
                print(f"{job['name']}: #{build.get('number', '?')} {state} ({build.get('url', '')})")
        else:
            status, queue_url = client.trigger_build(args.job_name)
            print(f"Zadanie {args.job_name} dodano do kolejki Jenkins (HTTP {status}).")
            if queue_url:
                print(f"Kolejka: {queue_url}")
    except JenkinsError as error:
        print(f"Błąd: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
