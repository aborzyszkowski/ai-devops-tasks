# Zadanie 15

## Oryginalna funkcja

Oryginalna wersja znajduje się w pliku [`config.js`](./config.js). Wybiera konfigurację za pomocą łańcucha warunków `if` / `else if` i zwraca konfigurację środowiska `development` jako domyślną.

## Wersja zrefaktoryzowana

Refaktoryzacja znajduje się w pliku [`config-refactored.js`](./config-refactored.js). Zamiast powtarzać bloki warunkowe, definiuje konfiguracje w jednym obiekcie `environmentConfigs`, a funkcja wybiera właściwą po nazwie środowiska.

## Zmiany i korzyści

- **Mniej powtórzeń:** konfiguracje są zebrane w jednym miejscu, co ułatwia ich porównywanie i aktualizowanie.
- **Łatwiejsze dodawanie środowisk:** nowe środowisko można dopisać jako kolejny wpis bez rozbudowy łańcucha warunków.
- **Bezpieczny wybór domyślny:** `hasOwnProperty.call` sprawdza, czy podana nazwa jest własnym kluczem obiektu. Nieznane środowisko nadal używa konfiguracji `development`.
- **Zachowanie niezależnych wyników:** spread (`{ ...config }`) zwraca nowy obiekt przy każdym wywołaniu, tak jak oryginalna funkcja. Modyfikacja zwróconego obiektu nie zmienia konfiguracji przechowywanej wewnętrznie.

Obie wersje można wczytać w projekcie Node.js przez `require('./config')` lub `require('./config-refactored')`.
