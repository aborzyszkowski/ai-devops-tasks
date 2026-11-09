# Zadanie 8

## Prompt

```text
ERROR: for app  Cannot start service app: driver failed programming external connectivity on endpoint app (172.18.0.2): Error starting userland proxy: listen tcp4 0.0.0.0:3000: bind: address already in use
```

Co oznacza ten błąd i jak mogę go rozwiązać?

## Odpowiedź

Błąd oznacza, że Docker nie może uruchomić usługi `app`, ponieważ port `3000` na hoście jest już zajęty. Wpis `0.0.0.0:3000` wskazuje port hosta, na którym Docker próbuje nasłuchiwać. Może go używać inny kontener albo proces uruchomiony bezpośrednio na komputerze.

### 1. Sprawdź, co zajmuje port

Na Linuksie można sprawdzić proces nasłuchujący na porcie:

```bash
sudo ss -ltnp 'sport = :3000'
```

Aby sprawdzić, czy port publikuje inny kontener:

```bash
docker ps --filter publish=3000
```

### 2. Zwolnij port albo zmień mapowanie

- Jeśli port zajmuje niepotrzebny kontener, zatrzymaj konkretny kontener po sprawdzeniu jego nazwy lub ID: `docker stop NAZWA_LUB_ID`.
- Jeśli port zajmuje lokalny proces, zatrzymaj go w odpowiedni dla niego sposób, o ile masz pewność, że nie jest potrzebny.
- Jeśli oba procesy powinny działać jednocześnie, zmień port **hosta** aplikacji, np. w `docker-compose.yml`:

```yaml
services:
  app:
    ports:
      - "3001:3000"
```

Zapis ma postać `PORT_HOSTA:PORTU_KONTENERA`. W tym przykładzie aplikacja nadal działa na porcie `3000` wewnątrz kontenera, ale jest dostępna na hoście pod adresem `http://localhost:3001`. Po zmianie uruchom ponownie usługę, np. poleceniem `docker compose up -d`.

Nie zatrzymuj w ciemno wszystkich kontenerów ani nie kończ procesu, zanim nie ustalisz, do czego służy. Jeśli port musi pozostać `3000`, trzeba zwolnić właśnie ten port zamiast zmieniać mapowanie.
