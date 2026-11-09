# Zadanie 21

## Proces konwersji

Dane wejściowe zawierają obiekt `users` z tablicą użytkowników. Każdy użytkownik został przekształcony w jeden wiersz CSV, a jego pola zapisano w kolumnach `id`, `name`, `email` i `roles`.

- Oryginalny JSON znajduje się w pliku [`users.json`](./users.json).
- Wynikowa tabela CSV znajduje się w pliku [`users.csv`](./users.csv).

W kolumnie `roles` tablicę zachowano jako tekst w formacie JSON, np. `["admin","user"]`. Cudzysłowy wewnątrz tego tekstu są podwojone zgodnie z regułami CSV, a całe pole otoczono cudzysłowami. Dzięki temu tablica może zawierać wiele wartości, a jej strukturę można odtworzyć przez ponowne sparsowanie zawartości pola jako JSON.

## Potencjalne wyzwania

- **Tablice i obiekty:** CSV nie ma natywnego typu dla zagnieżdżonych danych. Zapis JSON zachowuje strukturę, ale odbiorca musi wiedzieć, że wartość kolumny `roles` należy sparsować jako JSON.
- **Separatory i cudzysłowy:** przecinki, cudzysłowy lub znaki nowej linii w polach tekstowych wymagają poprawnego cytowania i escapowania zgodnego z CSV.
- **Brakujące i puste wartości:** trzeba uzgodnić, czy brak pola, pusta wartość i `null` mają różne reprezentacje.
- **Typy danych:** CSV nie przechowuje informacji o typach. Przykładowo `id` jest zapisane jako tekst i aplikacja odczytująca musi potraktować je jako liczbę, jeśli tego wymaga.
