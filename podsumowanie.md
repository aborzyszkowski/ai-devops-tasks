# Podsumowanie 29 zadań: AI w praktykach DevOps

## Kluczowe wnioski z pracy z AI

Seria zadań pokazała, że AI może szybko przekształcać krótkie polecenia w użyteczne pierwsze wersje skryptów, konfiguracji, testów i dokumentacji. Wykorzystano je między innymi przy Dockerze, Node.js, Pythonie, Jenkinsie, analizie logów i metryk oraz tworzeniu diagramów.

Najważniejszy wniosek jest jednak taki, że wygenerowany wynik to punkt wyjścia, a nie automatycznie sprawdzone rozwiązanie. Jakość zależy od kontekstu: wersji narzędzi, systemu operacyjnego, konfiguracji projektu, kontraktów API i przyjętych założeń. W zadaniach dotyczących API czy pipeline'ów brak implementacji wymagał wyraźnego oznaczania propozycji jako przykładów, a nie faktów.

## Mocne strony AI w kontekście DevOps

- **Szybkie tworzenie szkiców:** przykładowe skrypty Bash/PowerShell, testy, walidatory, pliki konfiguracyjne i diagramy można przygotować od razu do przeglądu.
- **Wyjaśnianie złożonych tematów:** AI potrafi przełożyć logi, metryki i składnię konfiguracji na uporządkowane kroki diagnostyczne.
- **Usprawnianie dokumentacji:** pomaga tworzyć README, opisy endpointów, instrukcje uruchamiania i wyjaśnienia dla osób początkujących.
- **Przegląd typowych ryzyk:** może zwrócić uwagę na sekrety, uprawnienia kontenerów, brak limitów, błędy YAML czy niepełne sprawdzanie kodów wyjścia.
- **Wsparcie nauki i refaktoryzacji:** przykłady oraz porównanie podejść pomagają zrozumieć złożoność algorytmów i strukturę pipeline'ów.

## Słabe strony i ograniczenia

- **Może dopowiadać nieznane szczegóły.** Jeśli opis nie definiuje schematu odpowiedzi, endpointów, statusów czy struktury projektu, AI może zaproponować wiarygodnie brzmiący, ale niepotwierdzony wariant.
- **Konfiguracje zależą od wersji i wtyczek.** Jenkinsfile lub JCasC może wyglądać poprawnie, a mimo to wymagać konkretnej wersji wtyczki, poprawnej nazwy pola, agenta z właściwymi narzędziami i konfiguracji poświadczeń.
- **Kod wymaga testów w docelowym środowisku.** Parsowanie składni nie potwierdza działania wobec prawdziwego API, rejestru, demona Docker czy danych produkcyjnych.
- **Optymalizacja może zmienić zakres obsługiwanych danych.** Na przykład podejście wykorzystujące mapę lub zbiory może mieć ograniczenia dla typów danych, których wersja pierwotna nie miała.
- **Ogólne porady nie zastępują diagnozy.** Same metryki lub pojedynczy wpis logu pozwalają wskazać hipotezy, ale zwykle nie dowodzą przyczyny problemu.

## Scenariusze, w których AI może szczególnie usprawnić pracę

1. **Wstępna diagnostyka incydentu:** streszczenie logów i metryk, wskazanie możliwych przyczyn, brakujących danych oraz bezpiecznej kolejności sprawdzeń.
2. **Tworzenie i przegląd pipeline'ów CI/CD:** przygotowanie etapów build/test/scan/deploy, bramek jakości, obsługi sekretów oraz dokumentacji, a następnie walidacja w rzeczywistym Jenkinsie.
3. **Automatyzacja powtarzalnych operacji:** szkice skryptów do backupu, kontroli usług i obsługi API, wraz z parametrami, komunikatami błędów i przykładami uruchomienia.
4. **Przygotowanie dokumentacji operacyjnej:** README, instrukcje dla zespołu, przykłady żądań API, diagramy przepływu i materiały onboardingowe.
5. **Szybkie prototypowanie i testy:** przykładowe testy jednostkowe, walidatory, refaktoryzacje oraz analiza złożoności, zanim rozwiązanie zostanie włączone do większego projektu.

## Wskazówki na przyszłość

- Podawaj **kontekst i ograniczenia**: wersje narzędzi, system operacyjny, strukturę projektu, format wejścia/wyjścia, oczekiwane zachowanie przy błędach.
- Rozdzielaj **fakty od założeń**. Poproś o oznaczenie niepotwierdzonych nazw endpointów, zmiennych, wtyczek i schematów.
- Traktuj kod wygenerowany przez AI jak kod z zewnętrznego wkładu: przejrzyj go, uruchom formatter/linter i testy, sprawdź różnice oraz wykonaj próbę w środowisku testowym.
- W przypadku konfiguracji infrastruktury sprawdzaj ją narzędziami właściwymi dla systemu: walidatorem YAML, `docker compose config`, Jenkins Configuration as Code/Job DSL albo stagingiem.
- Nie przekazuj sekretów. Używaj zmiennych środowiskowych, menedżera sekretów i minimalnych uprawnień, a przykładowe tokeny pozostawiaj fikcyjne.
- Proś o konkretne kryteria akceptacji: zachowanie dla błędnych danych, wartości graniczne, format wyników, wymagania dotyczące wydajności i kompatybilność.
- Przy diagnostyce najpierw zbieraj pomiary i reprodukcję; dopiero potem zmieniaj limity, skalę lub konfigurację.
- Zachowuj krótkie, czytelne commity i dokumentuj, co zostało rzeczywiście zweryfikowane, a co pozostaje przykładem.

## Moje przemyślenia

Największą wartością AI w tej serii było przyspieszenie przejścia od pytania do konkretnego artefaktu: skryptu, dokumentu albo konfiguracji, którą można dalej omawiać. AI szczególnie dobrze porządkowało odpowiedzi i wyjaśniało, dlaczego dany objaw — na przykład konflikt portu albo wysoki p99 — zasługuje na dalszą diagnostykę.

Jednocześnie zadania pokazały, że wiarygodny wygląd nie jest równoznaczny z poprawnością. Jenkins zależy od wtyczek i środowiska agenta, a przykładowe endpointy i odpowiedzi nie wynikają automatycznie z krótkiego opisu wymagań. Dlatego traktowałbym AI jako sprawnego partnera do szkicowania i przeglądu, ale odpowiedzialność za kontrakt, bezpieczeństwo i wdrożenie pozostawiłbym zespołowi. Najlepszy rezultat daje pętla: **opisz problem → wygeneruj propozycję → zweryfikuj założenia → uruchom testy → przejrzyj wynik → wdrażaj stopniowo**.
