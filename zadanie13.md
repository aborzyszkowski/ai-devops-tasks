# Zadanie 13

## Oryginalna funkcja

Oryginalny kod znajduje się w pliku [`fetch-user.js`](./fetch-user.js). Pobiera dane użytkownika, sprawdza status odpowiedzi HTTP, przekształca znacznik ostatniego logowania na obiekt `Date`, a w przypadku błędu zapisuje go w konsoli i zwraca `null`.

## Wersja z JSDoc

Funkcja z komentarzem dokumentacyjnym znajduje się w pliku [`fetch-user-documented.js`](./fetch-user-documented.js). Komentarz JSDoc jest umieszczony bezpośrednio nad funkcją:

- `@param` opisuje parametr `userId` oraz jego typ.
- `@returns` określa, że funkcja zwraca obietnicę (`Promise`) zawierającą obiekt z polami `name`, `email` i `lastLogin` typu `Date`, albo `null` w razie błędu.

JSDoc to format komentarzy dla JavaScriptu, który dokumentuje funkcje i ich parametry oraz zwracane wartości. Edytory, takie jak VS Code, mogą używać tych informacji do wyświetlania podpowiedzi i sprawdzania typów. Komentarz dokumentuje istniejące zachowanie funkcji — nie zmienia jej działania.
