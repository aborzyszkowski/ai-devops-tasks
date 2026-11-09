# Zadanie 26

## Pliki

- [`Jenkinsfile-with-errors`](./Jenkinsfile-with-errors) zawiera oryginalny pipeline.
- [`Jenkinsfile-fixed`](./Jenkinsfile-fixed) zawiera poprawioną wersję.

## Znalezione problemy i poprawki

1. **Literówka `stesp`:** Jenkins Declarative Pipeline oczekuje sekcji `steps`. Błędna nazwa uniemożliwia poprawne przetworzenie etapu `Build`; została zmieniona na `steps`.
2. **Niepoprawne polecenie budowania Node.js:** `npm build` nie uruchamia skryptu `build` z `package.json`. Zostało zastąpione przez `npm run build`.
3. **Powtarzalność instalacji zależności:** użyto `npm ci`, które instaluje wersje zapisane w lockfile i nadaje się do automatycznych buildów. Projekt musi mieć aktualny `package-lock.json`; jeśli go nie ma, należy go dodać albo tymczasowo użyć `npm install`.
4. **Położenie warunku `when`:** warunek przeniesiono przed `steps` w etapie `Deploy`, zgodnie z typowym układem dyrektyw Declarative Pipeline. Ogranicza on wdrożenie do gałęzi `master`; dyrektywa `branch` jest przeznaczona dla zadań typu Multibranch Pipeline.
5. **Nazwa obrazu i uwierzytelnianie rejestru:** obraz jest budowany i publikowany pod tą samą, pełną nazwą (`docker.io/your-dockerhub-user/myapp:latest`). Login i hasło nie są wpisane do skryptu — pobierane są z Jenkins Credentials przez identyfikator `docker-registry-credentials`, a hasło przekazywane jest do `docker login` przez standardowe wejście.

Przed użyciem należy podmienić `your-dockerhub-user`, skonfigurować w Jenkins poświadczenie username/password o wskazanym ID oraz zapewnić agentowi dostęp do Node.js, npm i Dockera. Jeśli główna gałąź projektu nazywa się `main`, należy zmienić warunek `branch 'master'` na `branch 'main'`. Poprawiony Jenkinsfile zakłada agenta Linux/macOS, ponieważ używa kroku `sh`.
