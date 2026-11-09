# Zadanie 10

## Prompt

Dlaczego ważne jest ignorowanie tych plików?

## Odpowiedź

Plik `.gitignore` informuje Git, których plików i folderów nie należy dodawać do repozytorium. Jest to ważne z kilku powodów:

- **Ochrona sekretów:** pliki `.env` często zawierają hasła, klucze API i dane dostępowe. Ich opublikowanie może umożliwić nieuprawniony dostęp do usług.
- **Mniejsze repozytorium:** `node_modules/`, pliki budowania (`dist/`, `build/`) i lokalne dane MongoDB mogą zajmować dużo miejsca. Zależności można odtworzyć z plików manifestu, a lokalną bazę utworzyć ponownie.
- **Brak zbędnych zmian:** logi, pliki tymczasowe i konfiguracje edytora różnią się między komputerami i nie powinny zaśmiecać historii zmian.
- **Bezpieczniejsza praca z bazą:** lokalne pliki MongoDB mogą zawierać dane prywatne lub testowe, a ich przypadkowe dodanie do repozytorium może naruszyć prywatność.

Do repozytorium warto dodać pliki potrzebne do odtworzenia projektu, np. `package.json`, lockfile, `Dockerfile` i `docker-compose.yml`, ale nie dane lokalne ani sekrety. Można udostępnić `.env.example` z nazwami wymaganych zmiennych i przykładowymi, niesekretnymi wartościami.

**Uwaga:** `.gitignore` działa na pliki, które nie zostały jeszcze dodane do śledzenia przez Git. Jeśli plik z sekretem został już zatwierdzony, samo dopisanie go do `.gitignore` nie usuwa go z historii — należy usunąć go z indeksu i unieważnić ujawnione dane dostępowe.
