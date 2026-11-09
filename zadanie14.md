# Zadanie 14

## Logi

```text
May 19 10:15:32 server dockerd[1234]: time="2025-05-19T10:15:32.123456789Z" level=info msg="Container 78a2b3c4 health status changed from starting to healthy"
May 19 10:16:45 server dockerd[1234]: time="2025-05-19T10:16:45.987654321Z" level=info msg="Container 78a2b3c4 failed to connect to 172.17.0.3:5432: connection refused"
May 19 10:16:47 server dockerd[1234]: time="2025-05-19T10:16:47.246813579Z" level=warning msg="Container 78a2b3c4 health status changed from healthy to unhealthy"
```

## Analiza

1. O **10:15:32** kontener `78a2b3c4` zmienił status zdrowia z `starting` na `healthy`. W tym momencie kontrola kondycji uznała go za działający poprawnie.
2. O **10:16:45** kontener nie mógł połączyć się z adresem `172.17.0.3` na porcie `5432`. Komunikat `connection refused` zwykle oznacza, że pod tym adresem nie ma procesu przyjmującego połączenia na tym porcie albo połączenie jest aktywnie odrzucane.
3. Dwie sekundy później, o **10:16:47**, stan zdrowia kontenera zmienił się z `healthy` na `unhealthy`. To wskazuje, że problem z połączeniem mógł spowodować niepowodzenie kontroli kondycji.

### Możliwe problemy

- Usługa, z którą kontener próbuje się połączyć (prawdopodobnie baza danych, ponieważ port `5432` jest domyślnym portem PostgreSQL), nie działa albo nie nasłuchuje na właściwym porcie.
- Adres IP może być nieaktualny lub wskazywać niewłaściwy kontener. W Dockerze lepiej zwykle łączyć się przez nazwę usługi w tej samej sieci zamiast polegać na zmiennym adresie IP kontenera.
- Kontenery mogą nie znajdować się we wspólnej sieci albo usługa docelowa może jeszcze nie być gotowa do przyjmowania połączeń.
- Konfiguracja adresu, portu, zapory sieciowej albo samej usługi może odrzucać połączenie.

### Co sprawdzić

Zweryfikuj, czy usługa docelowa działa, sprawdź jej logi oraz konfigurację sieci i portu. W Dockerze można też sprawdzić stan kontenerów poleceniem `docker ps` i przejrzeć logi konkretnej usługi poleceniem `docker logs NAZWA_LUB_ID`. Jeśli używany jest Docker Compose, odwołuj się do bazy po nazwie usługi, a nie po adresie IP. Sprawdź również, czy test zdrowia wykonuje się dopiero po uruchomieniu i gotowości wszystkich wymaganych usług.

Same logi nie przesądzają, dlaczego połączenie zostało odrzucone ani czy wskazany adres należy do bazy — to prawdopodobne tropy wymagające weryfikacji w konfiguracji i logach pozostałych usług.
