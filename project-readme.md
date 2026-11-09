# Simple Task API

REST API do zarządzania zadaniami, zbudowane w Node.js i Express z bazą MongoDB.

## Opis

API umożliwia tworzenie, odczytywanie, aktualizowanie i usuwanie zadań. Udostępnia też filtrowanie zadań według statusu i priorytetu oraz prostą autoryzację użytkowników.

## Instalacja

Wymagane są Node.js, npm i dostępna instancja MongoDB.

1. Pobierz repozytorium i przejdź do katalogu projektu.
2. Zainstaluj zależności:

   ```bash
   npm install
   ```

3. Skonfiguruj zmienne środowiskowe, co najmniej adres połączenia z MongoDB (`MONGODB_URI`) i port serwera (`PORT`). Jeśli projekt używa tokenów, skonfiguruj również wymagany sekret autoryzacji.
4. Uruchom aplikację poleceniem zdefiniowanym w `package.json`, np.:

   ```bash
   npm start
   ```

Dokładne nazwy zmiennych i skryptów zależą od implementacji projektu.

## Użycie

Po uruchomieniu serwer nasłuchuje na skonfigurowanym porcie, np. `http://localhost:3000`. Żądania wysyłaj do ścieżek `/api/...` opisanych w sekcji endpointów.

Przykładowe żądanie utworzenia zadania:

```bash
curl -X POST http://localhost:3000/api/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"title":"Przygotować wdrożenie","status":"pending","priority":"high"}'
```

Wymagany format tokenu oraz dozwolone wartości statusu i priorytetu należy potwierdzić w implementacji.

## Endpointy API

Poniższa tabela przedstawia proponowany, typowy układ endpointów na podstawie opisu funkcjonalności. Metody HTTP i ścieżki należy dopasować do rzeczywistej implementacji.

| Metoda | Endpoint | Opis |
|---|---|---|
| `POST` | `/api/auth/register` | Rejestracja użytkownika (jeśli jest obsługiwana). |
| `POST` | `/api/auth/login` | Uwierzytelnienie użytkownika; szczegóły odpowiedzi zależą od implementacji. |
| `GET` | `/api/tasks` | Pobranie listy zadań; opcjonalne filtry, np. `?status=pending&priority=high`. |
| `GET` | `/api/tasks/:id` | Pobranie pojedynczego zadania. |
| `POST` | `/api/tasks` | Utworzenie zadania. |
| `PUT` | `/api/tasks/:id` | Aktualizacja zadania. |
| `DELETE` | `/api/tasks/:id` | Usunięcie zadania. |

Endpointy zadań mogą wymagać uwierzytelnienia. Wymagania autoryzacji, formaty żądań i odpowiedzi, kody błędów oraz dozwolone wartości pól powinny zostać opisane zgodnie z działającą implementacją.
