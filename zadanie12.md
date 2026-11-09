# Zadanie 12

## Oryginalna funkcja

```python
def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates
```

## Czy kod można zoptymalizować?

Tak. Oryginalna funkcja porównuje elementy parami za pomocą dwóch zagnieżdżonych pętli, co daje złożoność czasową **O(n²)**. Sprawdzenie `not in duplicates` również przeszukuje listę wynikową.

## Wydajniejsza wersja

```python
def find_duplicates(list_of_items):
    duplicates = []
    seen = set()
    duplicates_seen = set()

    for item in list_of_items:
        if item in seen:
            if item not in duplicates_seen:
                duplicates.append(item)
                duplicates_seen.add(item)
        else:
            seen.add(item)

    return duplicates
```

## Co zostało usprawnione?

- Zbiory `seen` i `duplicates_seen` pozwalają przeciętnie sprawdzać obecność elementu w czasie **O(1)**, zamiast przeszukiwać listę.
- Funkcja przechodzi przez elementy tylko raz. Jej przeciętna złożoność czasowa wynosi **O(n)**, a pamięciowa **O(n)**.
- Wynik nadal jest listą, a powtarzające się wartości są zwracane tylko raz — w kolejności ich pierwszego powtórzenia. Przykładowo dla `[1, 2, 1, 2, 1]` wynikiem będzie `[1, 2]`.

**Ograniczenie:** elementy wejściowe muszą być hashowalne (np. liczby, napisy lub krotki z hashowalnymi elementami), ponieważ są przechowywane w zbiorach. Oryginalna wersja mogła porównywać także elementy niehashowalne, takie jak listy.
