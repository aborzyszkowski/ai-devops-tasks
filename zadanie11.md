# Zadanie 11

## Czym jest Jest?

Jest to narzędzie do testowania kodu JavaScript. Uruchamia testy i sprawdza ich wyniki, a w razie błędu pokazuje, czego oczekiwano i jaki wynik otrzymano.

## Kod funkcji

Plik `sum.js` zawiera funkcję oraz eksportuje ją, aby test mógł ją zaimportować:

```js
function sum(a, b) {
  return a + b;
}

module.exports = sum;
```

## Test jednostkowy

Plik `sum.test.js` wywołuje funkcję z liczbami `2` i `3`, a następnie sprawdza, czy wynikiem jest `5`:

```js
const sum = require('./sum');

test('adds two numbers', () => {
  expect(sum(2, 3)).toBe(5);
});
```

- `require('./sum')` wczytuje funkcję z pliku `sum.js`.
- `test(...)` definiuje test z czytelną nazwą.
- `expect(...)` przekazuje otrzymany wynik do sprawdzenia, a `.toBe(5)` oczekuje dokładnie wartości `5`.

## Instalacja i uruchomienie

W katalogu projektu, jeśli nie ma jeszcze pliku `package.json`, zainicjuj projekt i zainstaluj Jest jako zależność deweloperską:

```bash
npm init -y
npm install --save-dev jest
```

Uruchom test bezpośrednio:

```bash
npx jest sum.test.js
```

Można też dodać do sekcji `"scripts"` w `package.json`:

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

W istniejącym `package.json` należy dopisać wpis `"test": "jest"` do już istniejącej sekcji `"scripts"`, zamiast zastępować cały plik. Testy można wtedy uruchamiać poleceniem:

```bash
npm test
```

## Przykładowa struktura projektu

```text
projekt/
├── node_modules/       # zainstalowane pakiety (generowane przez npm)
├── package.json        # konfiguracja projektu i skrypt testowy
├── package-lock.json   # zapis dokładnych wersji zależności
├── sum.js              # testowana funkcja
├── sum.test.js         # test jednostkowy Jest
└── zadanie-11.md       # instrukcja i wyjaśnienie
```
