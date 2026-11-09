# Zadanie 18

## Pięć kluczowych praktyk bezpieczeństwa dla Docker w produkcji

1. **Uruchamiaj kontenery jako użytkownik nieuprzywilejowany.** Nie uruchamiaj aplikacji jako `root`, jeśli nie jest to konieczne. Zmniejsza to możliwe skutki przejęcia procesu w kontenerze.
2. **Ogranicz uprawnienia i zasoby kontenera.** Odrzuć niepotrzebne capabilities, włącz `no-new-privileges`, rozważ system plików tylko do odczytu i ustaw limity CPU oraz pamięci. Przy systemie plików tylko do odczytu zapewnij zapisywalne wolumeny wyłącznie tam, gdzie aplikacja ich potrzebuje.
3. **Używaj zaufanych, minimalnych i aktualnych obrazów.** Przypinaj wersje bazowych obrazów, regularnie aktualizuj zależności i skanuj obrazy oraz pakiety pod kątem znanych podatności.
4. **Chroń sekrety.** Nie umieszczaj haseł, tokenów ani kluczy w obrazie, repozytorium lub jawnych plikach Compose. Korzystaj z menedżera sekretów odpowiedniego dla środowiska; ogranicz dostęp i regularnie wymieniaj dane dostępowe.
5. **Ogranicz dostęp sieciowy.** Publikuj tylko wymagane porty, izoluj usługi w sieciach i nie wystawiaj bazy danych bezpośrednio do Internetu. Wymagaj szyfrowania połączeń tam, gdzie jest to potrzebne.

## Jak uruchomić aplikację jako użytkownik nieuprzywilejowany?

Poniższy przykład zakłada aplikację Node.js i port `3000`. Użytkownik i grupa o identyfikatorze `10001` są tworzeni w obrazie; `USER` ustawia konto używane do uruchomienia procesu aplikacji.

### Dockerfile

```dockerfile
FROM node:22-bookworm-slim

ENV NODE_ENV=production
WORKDIR /app

RUN groupadd --system --gid 10001 app \
    && useradd --system --uid 10001 --gid app \
       --home-dir /app --no-create-home --shell /usr/sbin/nologin app

COPY package*.json ./
RUN npm ci --omit=dev

COPY --chown=10001:10001 . .

USER 10001:10001

EXPOSE 3000
CMD ["node", "server.js"]
```

Ważne jest, aby `USER` obowiązywał w czasie uruchamiania aplikacji. Jeśli aplikacja musi zapisywać pliki, przygotuj odpowiedni katalog z prawami zapisu dla użytkownika `10001` zamiast uruchamiać cały proces jako `root`.

### docker-compose.yml

```yaml
services:
  app:
    build: .
    user: "10001:10001"
    ports:
      - "3000:3000"
```

Wpis `user` jawnie wymusza ten sam UID i GID również w Compose. Muszą one odpowiadać użytkownikowi skonfigurowanemu w obrazie. Jeśli aplikacja używa bind mountów lub wolumenów do zapisu, ich uprawnienia również muszą umożliwiać zapis temu użytkownikowi.

Po zbudowaniu i uruchomieniu można sprawdzić tożsamość procesu w kontenerze:

```bash
docker compose build app
docker compose run --rm app id
```

Wynik powinien pokazać UID `10001`, a nie `0` (root). Nazwa skryptu startowego w `CMD` (`server.js`) oraz wymagane katalogi do zapisu powinny być dostosowane do konkretnej aplikacji.
