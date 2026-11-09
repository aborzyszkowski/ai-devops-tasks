# Zadanie 20

## Wyrażenie regularne

```regex
^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(?![\s\S])
```

Walidator używający tego wyrażenia znajduje się w pliku [`ipv4-validator.js`](./ipv4-validator.js). Funkcja `isValidIPv4(address)` zwraca `true` dla napisu w postaci czterech dziesiętnych oktetów IPv4, a `false` dla pozostałych wartości.

## Jak działa wyrażenie?

- `^` wymaga początku tekstu.
- `(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])` dopasowuje jeden oktet z zakresu `0–255`:
  - `25[0-5]` obejmuje `250–255`;
  - `2[0-4][0-9]` obejmuje `200–249`;
  - `1[0-9]{2}` obejmuje `100–199`;
  - `[1-9]?[0-9]` obejmuje `0–99` bez wiodących zer.
- `(?: ... )` grupuje alternatywy, a `\.` dopasowuje dosłowną kropkę między oktetami.
- `{3}` wymaga trzech pierwszych oktetów zakończonych kropką; końcowa grupa dopasowuje czwarty oktet.
- `(?![\s\S])` sprawdza, że nie ma już żadnego znaku. Dzięki temu dopasowanie obejmuje cały napis, również nie akceptuje dodatkowej końcowej nowej linii.

Wzorzec celowo nie akceptuje wiodących zer, np. `001`, aby uniknąć niejednoznacznych zapisów. Sprawdza wyłącznie składnię adresu IPv4 — nie określa, czy adres jest osiągalny ani do jakiej sieci należy.

## Przykładowe testy

| Adres | Wynik | Uzasadnienie |
|---|---|---|
| `192.168.1.1` | Poprawny | Cztery oktety w zakresie `0–255`. |
| `0.0.0.0` | Poprawny | Każdy oktet może mieć wartość `0`. |
| `255.255.255.255` | Poprawny | Maksymalna wartość każdego oktetu. |
| `192.168.1` | Niepoprawny | Zawiera tylko trzy oktety. |
| `256.1.2.3` | Niepoprawny | Oktet `256` przekracza zakres. |
| `192.168.01.1` | Niepoprawny | Oktet `01` ma wiodące zero. |
| `192.168.1.1abc` | Niepoprawny | Zawiera dodatkowe znaki po adresie. |
| `192.168.1.1` z końcową nową linią | Niepoprawny | Cały napis musi być poprawnym adresem. |
