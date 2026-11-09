# Zadanie 25

## Wyjaśnienie etapów Jenkinsfile

Plik [`Jenkinsfile`](./Jenkinsfile) definiuje deklaratywny pipeline dla aplikacji Node.js. Etapy wykonują się kolejno; domyślnie niepowodzenie jednego z nich zatrzymuje dalsze etapy.

1. **Checkout** — `checkout scm` pobiera kod z repozytorium skonfigurowanego dla zadania Jenkinsa.
2. **Install dependencies** — `npm install` instaluje pakiety wymagane przez aplikację.
3. **Test** — `npm test` uruchamia testy projektu. Jeśli testy zakończą się błędem, pipeline nie przejdzie do budowania i publikowania obrazu.
4. **Build application** — `npm run build` uruchamia skrypt budowania zdefiniowany w `package.json`.
5. **Build Docker image** — wtyczka Jenkins Docker Pipeline buduje obraz na podstawie `Dockerfile` w katalogu repozytorium i nadaje mu tag z numerem buildu.
6. **Publish Docker image** — pipeline loguje się do rejestru przy użyciu poświadczeń Jenkinsa i publikuje obraz z tagiem buildu.

## Konfiguracja przed użyciem

- Zmień `DOCKER_REGISTRY` oraz `IMAGE_NAME` na adres i nazwę własnego rejestru/obrazu. Host w `IMAGE_NAME` powinien odpowiadać rejestrowi wskazanemu przez `DOCKER_REGISTRY`.
- Dodaj w Jenkins **Credentials** poświadczenie typu username/password i ustaw jego ID zgodnie z `DOCKER_CREDENTIALS_ID`. Nie wpisuj loginu ani hasła bezpośrednio do pliku.
- Agent Jenkinsa musi mieć Node.js, npm, Docker CLI i dostęp do działającego demona Docker.
- Projekt musi zawierać `package.json` z poleceniami `test` i `build`, a także plik `Dockerfile`.
- Pipeline używa kroku `docker` z wtyczki **Docker Pipeline**.

## Najlepsze praktyki dla pipeline'ów Jenkins

- Przechowuj sekrety w Jenkins Credentials i ogranicz dostęp do nich; nie publikuj obrazów z niezaufanych pull requestów przy użyciu poświadczeń produkcyjnych.
- Uruchamiaj testy przed budowaniem i publikowaniem obrazu, aby wadliwy kod nie został wypchnięty do rejestru.
- Używaj przewidywalnych, najlepiej niezmiennych tagów, takich jak numer buildu lub commit. W tym przykładzie numer buildu zapobiega nadpisywaniu obrazu w kolejnych buildach.
- Utrzymuj agentów i wtyczki Jenkinsa aktualne oraz ograniczaj uprawnienia agentów do niezbędnego minimum. Dostęp do demona Docker może dawać szerokie uprawnienia na hoście agenta.
- W produkcji rozważ `npm ci` z zatwierdzonym lockfile zamiast `npm install`, skanowanie zależności i obrazu oraz publikowanie wyłącznie po spełnieniu polityk jakości i bezpieczeństwa.
