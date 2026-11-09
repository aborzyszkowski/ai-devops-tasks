# Zadanie 28

## Skrypt i użyte biblioteki

Skrypt [`jenkins-manager.py`](./jenkins-manager.py) komunikuje się z Jenkins Remote Access API przez HTTP. Korzysta wyłącznie z biblioteki standardowej Pythona:

- `urllib.request` wysyła żądania HTTP;
- `urllib.error` obsługuje błędy HTTP i połączenia;
- `urllib.parse` koduje nazwy zadań w adresach URL;
- `json` odczytuje odpowiedzi API;
- `argparse`, `os`, `base64` i `sys` obsługują argumenty CLI, konfigurację, Basic Auth i komunikaty procesu.

Nie trzeba instalować dodatkowych pakietów.

## Konfiguracja

Utwórz w Jenkins konto lub token API przeznaczony do automatyzacji i nadaj mu wyłącznie wymagane uprawnienia do odczytu zadań/buildów oraz uruchamiania buildów. Ustaw zmienne środowiskowe, nie wpisuj tokenu do skryptu ani do repozytorium.

Przykład w PowerShell:

```powershell
$env:JENKINS_URL = "https://jenkins.example.com"
$env:JENKINS_USERNAME = "api-user"
$env:JENKINS_API_TOKEN = "wstaw-token-z-bezpiecznego-magazynu"
```

W Bash:

```bash
export JENKINS_URL="https://jenkins.example.com"
export JENKINS_USERNAME="api-user"
export JENKINS_API_TOKEN="wstaw-token-z-bezpiecznego-magazynu"
```

## Przykładowe polecenia

Wyświetlenie zadań:

```bash
python jenkins-manager.py jobs
```

Sprawdzenie ostatnich buildów:

```bash
python jenkins-manager.py status
```

Uruchomienie zadania:

```bash
python jenkins-manager.py build my-node-app
```

Zadanie znajdujące się w folderze:

```bash
python jenkins-manager.py build Backend/my-node-app
```

## Jak działa skrypt?

- `jobs` pobiera listę zadań z API Jenkins. Dla folderów i projektów wielogałęziowych przegląda również zagnieżdżone zadania.
- `status` pobiera dla każdego zadania ostatni build i wyświetla jego numer, wynik lub stan `BUILDING`; zadania bez buildów są oznaczone osobno.
- `build` wysyła żądanie `POST` do endpointu uruchamiania zadania. Dla instalacji z ochroną CSRF skrypt pobiera crumb i dołącza go do żądania.
- Każde żądanie używa HTTP Basic Auth z nazwą użytkownika i tokenem API. Błędy połączenia, HTTP, brak konfiguracji i błędna odpowiedź API są zgłaszane z niezerowym kodem zakończenia.

Ustaw `JENKINS_URL` jako adres bazowy instancji, także wtedy, gdy Jenkins działa pod kontekstową ścieżką, np. `https://example.com/jenkins`. Skrypt zakłada dostęp do API przez HTTPS w środowisku produkcyjnym. Uruchomienie builda może wymagać dodatkowych uprawnień, a zadania z parametrami mogą wymagać osobnego endpointu `buildWithParameters`.
