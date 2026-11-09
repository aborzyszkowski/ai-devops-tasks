# Zadanie 16

## Pliki

- [`backup-db.sh`](./backup-db.sh) — oryginalny skrypt Bash.
- [`backup-db.ps1`](./backup-db.ps1) — odpowiednik dla PowerShell w systemie Windows.

Oba skrypty tworzą skompresowany zrzut bazy `app_database` w pliku z datą i godziną w nazwie. Skrypt PowerShell zapisuje kopię w podkatalogu `db-backups` w katalogu wskazywanym przez zmienną systemową `ProgramData`.

## Główne różnice

- **Zmienne:** Bash używa składni `$NAZWA` i podstawiania `$(...)`; PowerShell również używa `$NAZWA`, ale datę pobiera poleceniem `Get-Date`, a ścieżkę buduje przez `Join-Path`.
- **Katalogi i ścieżki:** Bash tworzy katalog przez `mkdir -p` i używa ścieżki `/var/backups/db`. PowerShell używa `New-Item` i ścieżki właściwej dla Windows.
- **Potoki i kompresja:** Bash przekazuje standardowe wyjście `mysqldump` przez potok do programu `gzip`. Skrypt PowerShell uruchamia `mysqldump` jako proces i przekazuje jego wyjście do .NET `GZipStream`, dzięki czemu nie wymaga osobnego programu `gzip`.
- **Obsługa błędów:** Bash sprawdza `$?` po potoku, co bez `set -o pipefail` sprawdza przede wszystkim kod zakończenia ostatniego polecenia, czyli `gzip`. PowerShell sprawdza kod wyjścia samego `mysqldump`; przy błędzie usuwa niekompletny plik kopii.
- **Hasło:** opcja `-p` powoduje, że `mysqldump` poprosi o hasło użytkownika `root`. Program `mysqldump` musi być zainstalowany i dostępny w `PATH`; należy też mieć uprawnienia do zapisu w katalogu kopii.

W środowisku produkcyjnym warto użyć dedykowanego użytkownika bazy z minimalnymi uprawnieniami zamiast `root` oraz zadbać o bezpieczne przechowywanie kopii zapasowych.
