# Zadanie 23

## Oryginalny algorytm

Oryginalna funkcja znajduje się w pliku [`find-pairs.js`](./find-pairs.js). Sprawdza każdą parę indeksów `i < j`, dlatego wykonuje **O(n²)** porównań dla tablicy długości `n`. Pamięć dodatkowa poza wynikiem wynosi **O(1)**; wraz z przechowywaną tablicą par wynosi **O(k)**, gdzie `k` to liczba znalezionych par. W najgorszym przypadku `k = O(n²)`.

## Wersja zoptymalizowana

Kod znajduje się w pliku [`find-pairs-optimized.js`](./find-pairs-optimized.js). Najpierw zapisuje indeksy elementów w mapie według ich wartości. Następnie dla każdego indeksu szuka wartości dopełniającej do `targetSum` i wyszukuje binarnie pierwszy pasujący indeks większy od bieżącego. Końcowe sprawdzenie zachowuje warunek sumy z oryginalnej funkcji.

Dla bezpiecznych liczb całkowitych JavaScript (`Number.isSafeInteger`) i sum mieszczących się w tym zakresie koszt wynosi **O(n log n + k)** czasu: `O(n)` na zbudowanie mapy, `O(log n)` wyszukiwania indeksu dla każdego elementu oraz `O(k)` na zapisanie wyników. Pamięć dodatkowa to **O(n)** na mapę indeksów, a wynik nadal wymaga **O(k)** pamięci. Algorytm zachowuje wszystkie pary, ich kolejność oraz powtórzenia z oryginału dla takich danych.

Ograniczenie: dla liczb zmiennoprzecinkowych odejmowanie `targetSum - arr[i]` nie zawsze odtworzy `arr[j]`, mimo że suma `arr[i] + arr[j]` po zaokrągleniu jest równa celowi. Dlatego ta optymalizacja zakłada bezpieczne liczby całkowite; dla dowolnych wartości JavaScript nie jest w pełni równoważna oryginalnej funkcji.

Nie można zagwarantować czasu `O(n)` niezależnie od liczby wyników, jeśli funkcja ma zwracać wszystkie pary: tablica wejściowa z wieloma powtarzającymi się wartościami może mieć **O(n²)** pasujących par, a ich utworzenie i zwrócenie wymaga co najmniej **O(k)** pracy i pamięci.

Przykład: dla `[1, 4, 2, 3, 3]` i celu `5` wynik to `[[1, 4], [2, 3], [2, 3]]`.
