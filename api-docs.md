# API: lista użytkowników

## `GET /api/users`

Zwraca listę użytkowników. Wyniki można pobierać stronicami i opcjonalnie filtrować według roli.

### Parametry zapytania

| Parametr | Typ | Wymagany | Domyślnie | Opis |
|---|---|---:|---:|---|
| `page` | liczba całkowita | Nie | `1` | Numer strony wyników. |
| `limit` | liczba całkowita | Nie | `10` | Liczba wyników na stronie; maksymalnie `100`. |
| `role` | tekst | Nie | — | Zwraca użytkowników o podanej roli. |

### Przykładowe żądanie

```http
GET /api/users?page=2&limit=5&role=admin
```

Równoważny adres URL:

```text
/api/users?page=2&limit=5&role=admin
```

### Przykładowa odpowiedź

Poniższy przykład zakłada, że API zwraca tablicę obiektów użytkownika. Rzeczywisty format odpowiedzi i dostępne pola zależą od implementacji:

```json
[
  {
    "id": 6,
    "name": "Anna Nowak",
    "role": "admin"
  },
  {
    "id": 9,
    "name": "Jan Kowalski",
    "role": "admin"
  }
]
```

Dokumentacja wejściowa nie określa formatu błędów ani zachowania dla nieprawidłowych wartości parametrów. Te szczegóły należy uzupełnić zgodnie z implementacją API.
