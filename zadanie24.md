# Zadanie 24

## Metryki serwera API — ostatnie 24 godziny

- Średni czas odpowiedzi: **230 ms**
- 95. percentyl czasu odpowiedzi (p95): **450 ms**
- 99. percentyl czasu odpowiedzi (p99): **1200 ms**
- Liczba zapytań: **15 000**
- Liczba błędów 5xx: **120**
- Użycie CPU: średnio **45%**, maksymalnie **80%**
- Użycie pamięci: średnio **2,1 GB**, maksymalnie **3,5 GB z dostępnych 4 GB**

## Interpretacja

Średni czas odpowiedzi wynosi 230 ms, ale p99 osiąga 1200 ms. Oznacza to, że część żądań obsługiwana jest znacznie wolniej niż typowe — około 1% przekracza wartość p99. Sama średnia nie pokazuje więc pełnego obrazu; warto sprawdzić, które endpointy i zależności odpowiadają za wolne żądania.

120 błędów 5xx na 15 000 zapytań to około **0,8%** wszystkich żądań, jeśli oba pomiary obejmują ten sam okres i liczą te same typy zapytań. To widoczny odsetek błędów serwera, który warto rozbić według kodu HTTP, endpointu i przyczyny.

Średnie użycie CPU (45%) nie wskazuje na stałe pełne obciążenie procesora, choć szczyty 80% mogą mieć znaczenie w okresach większego ruchu. Pamięć jest bliżej limitu: maksimum 3,5 GB z 4 GB to około **87,5%** dostępnego zasobu. Krótkie skoki lub wzrost zużycia mogą doprowadzić do braku pamięci, restartów albo spowolnienia systemu.

## Potencjalne problemy i zalecenia

1. **Zlokalizuj wolne żądania.** Mierz czasy odpowiedzi osobno dla endpointów i zależności (np. bazy danych). Użyj tracingu lub profilera, aby ustalić, czy p99 wynika z wolnych zapytań, blokad, zewnętrznych usług, czy długiej pracy aplikacji.
2. **Przeanalizuj błędy 5xx.** Rozbij je na konkretne kody i endpointy, skoreluj z logami oraz wdrożeniami. Napraw źródło błędów, zamiast ukrywać je przez automatyczne ponawianie wszystkich żądań.
3. **Zbadaj pamięć.** Sprawdź trend w czasie, pamięć procesu i kontenerów, garbage collection, cache oraz oznaki wycieków. Zostaw zapas zasobów; nie zwiększaj limitu bez sprawdzenia pamięci dostępnej na hoście.
4. **Sprawdź zachowanie podczas szczytów.** Koreluj metryki z natężeniem ruchu i testami obciążeniowymi. Jeśli CPU lub pamięć ograniczają aplikację, rozważ optymalizację, skalowanie albo zwiększenie zasobów po potwierdzeniu w pomiarach.
5. **Ustaw cele i alerty.** Monitoruj p95/p99, odsetek 5xx, CPU, pamięć i restarty. Dobierz progi do wymagań usługi i reaguj na utrzymujące się trendy, nie na pojedyncze chwilowe skoki.

Metryki z 24 godzin dają wskazówki, ale nie pokazują rozkładu ruchu, zmian w czasie ani przyczyn opóźnień i błędów. Przed zmianą infrastruktury warto zebrać dane per endpoint i skorelować je z logami oraz wykresami zasobów.
