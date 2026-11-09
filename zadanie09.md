# Zadanie 9

## Prompt

```yaml
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD=password
```

Czy plik jest poprawny? Popraw błędy, jeśli istnieją.

## Odpowiedź

Plik zawiera błąd składni YAML: w definicji usługi `app` po kluczu `ports` brakuje dwukropka. Poprawiona wersja:

```yaml
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: password
```

W sekcji `environment` hasło zapisano jako parę klucz-wartość YAML (`POSTGRES_PASSWORD: password`); równoważny zapis listowy to `- POSTGRES_PASSWORD=password`. Hasło `password` jest słabe i nie powinno być używane w rzeczywistym środowisku. W praktyce należy przekazać silne hasło spoza pliku, np. przez zmienną środowiskową lub Docker secrets.
