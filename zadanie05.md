# Zadanie 5

## Prompt

Stwórz prosty diagram ASCII Art przedstawiający połączenie klienta, serwera aplikacji i bazy danych. Dodaj do diagramu opisy elementów i kierunki przepływu danych.

## Diagram

```text
+------------+     HTTP request      +------------------+      SQL query       +------------+
| CLIENT     | --------------------> | APP SERVER       | --------------------> | DATABASE   |
| browser or |                       | business logic   |                       | app data   |
| mobile app | <-------------------- | response (JSON)  | <-------------------- | query rows |
+------------+    response (JSON)    +------------------+    query results     +------------+
```

Klient wysyła żądanie do serwera aplikacji. Serwer przetwarza je, komunikuje się z bazą danych, a następnie zwraca klientowi odpowiedź. Diagram używa znaków ASCII; strzałki pokazują przepływ żądania i odpowiedzi.
