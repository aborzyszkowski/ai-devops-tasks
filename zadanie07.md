# Zadanie 7

## Wygenerowany skrypt

Skrypt został zapisany w pliku [`check_docker.sh`](./check_docker.sh). Jest przeznaczony dla systemu Linux korzystającego z `systemd`. Do uruchomienia usługi potrzebne są uprawnienia administratora; skrypt używa do tego polecenia `sudo`.

## Wyjaśnienie linia po linii

1. `#!/usr/bin/env bash` — informuje system, że skrypt należy uruchomić za pomocą interpretera Bash.
2. Pusta linia — oddziela nagłówek od właściwych instrukcji i poprawia czytelność.
3. `if ! command -v systemctl >/dev/null 2>&1; then` — sprawdza, czy polecenie `systemctl` jest dostępne. Znak `!` oznacza „jeśli nie”, a przekierowania ukrywają wynik sprawdzenia.
4. `echo "Błąd: ..."` — wyświetla informację, że skrypt wymaga systemu z `systemd`.
5. `exit 1` — kończy skrypt kodem błędu, bo bez `systemctl` nie może on sprawdzić ani uruchomić usługi.
6. `fi` — kończy pierwszy blok warunkowy.
7. Pusta linia — oddziela sprawdzenie dostępności narzędzia od sprawdzenia usługi.
8. `if systemctl is-active --quiet docker; then` — sprawdza, czy usługa `docker` działa. Opcja `--quiet` nie wypisuje statusu; wynik jest przekazywany do warunku.
9. `echo "Usługa Docker już działa."` — informuje, że nie trzeba podejmować żadnych działań.
10. `exit 0` — kończy skrypt kodem sukcesu.
11. `fi` — kończy warunek sprawdzający, czy Docker już działa.
12. Pusta linia — oddziela kontrolę stanu od próby uruchomienia usługi.
13. `echo "Usługa Docker nie działa. Próbuję ją uruchomić..."` — informuje o podjęciu próby uruchomienia.
14. `if ! sudo systemctl start docker; then` — próbuje uruchomić usługę z uprawnieniami administratora. Jeśli polecenie się nie powiedzie, wykonywany jest blok błędu.
15. `echo "Błąd: nie udało się uruchomić usługi Docker."` — wyświetla komunikat o nieudanej próbie.
16. `exit 1` — kończy skrypt kodem błędu.
17. `fi` — kończy blok obsługujący nieudaną próbę uruchomienia.
18. Pusta linia — oddziela uruchomienie usługi od ponownego sprawdzenia jej stanu.
19. `if systemctl is-active --quiet docker; then` — ponownie sprawdza, czy usługa faktycznie działa po próbie uruchomienia.
20. `echo "Usługa Docker została uruchomiona."` — potwierdza powodzenie.
21. `exit 0` — kończy skrypt kodem sukcesu.
22. `fi` — kończy warunek ponownego sprawdzenia.
23. Pusta linia — oddziela ścieżkę sukcesu od końcowego komunikatu o błędzie.
24. `echo "Błąd: polecenie start zakończyło się, ale usługa Docker nadal nie działa."` — informuje, że mimo wykonania polecenia usługa nie przeszła do stanu aktywnego.
25. `exit 1` — kończy skrypt kodem błędu.

Kod wyjścia `0` oznacza sukces (usługa już działa lub została uruchomiona), a kod `1` — błąd. Skrypt można uruchomić poleceniem `bash check_docker.sh`; przy uruchamianiu usługi `sudo` może poprosić o hasło.
