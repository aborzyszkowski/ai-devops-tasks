# Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

Wysokie zużycie pamięci może wynikać z wycieku w aplikacji, dużego obciążenia, zbyt wielu procesów roboczych albo nieograniczonego cache. Nie należy zaczynać od samego restartowania kontenera ani arbitralnego obniżania limitu — najpierw trzeba zebrać dane i ustalić przyczynę.

## 1. Sprawdź zużycie pamięci i limit kontenera

```bash
docker stats --no-stream
docker inspect --format='OOMKilled={{.State.OOMKilled}} MemoryLimit={{.HostConfig.Memory}}' NAZWA_LUB_ID
```

`docker stats` pozwala porównać kontenery i obserwować zużycie w czasie. Na Linuksie wyświetlana wartość uwzględnia odjęcie cache, dlatego w razie wątpliwości sprawdź też metryki cgroup lub narzędzia monitorujące hosta. `OOMKilled=true` oznacza, że kontener został zakończony przez system z powodu braku pamięci.

## 2. Znajdź źródło problemu

- Sprawdź logi oraz metryki aplikacji w czasie, w którym pamięć rośnie.
- Użyj profilera właściwego dla używanego języka, aby wykryć wycieki, niezwalniane obiekty lub nadmierne alokacje.
- Zweryfikuj konfigurację cache, pul połączeń, rozmiarów zadań i liczbę procesów roboczych.
- Sprawdź również obciążenie oraz wolną pamięć hosta — kilka kontenerów może łącznie wyczerpać zasoby.

Jeśli zużycie rośnie stopniowo przy podobnym obciążeniu, podejrzewaj wyciek lub nieograniczony cache. Jeśli skok pojawia się tylko podczas dużych zadań, aplikacja może potrzebować więcej pamięci albo przetwarzania porcjami.

## 3. Usuń przyczynę i ustaw uzasadniony limit

Po poprawce aplikacji można ograniczyć maksymalne zużycie pamięci, by awaria jednego kontenera nie pozbawiła jej całego hosta:

```bash
docker run --memory=512m --memory-swap=768m nazwa-obrazu
```

To przykładowe wartości, które należy dobrać na podstawie pomiarów, typowego obciążenia i dostępnych zasobów. Limit nie zmniejsza zapotrzebowania aplikacji: po jego przekroczeniu kontener może zostać zakończony przez mechanizm OOM. Opcję swap należy dobrać świadomie, ponieważ intensywne korzystanie ze swapu może znacząco spowolnić aplikację.

W Docker Compose można określić analogiczny limit dla usługi, np. `mem_limit: 512m`. Po wdrożeniu zmiany monitoruj zużycie, błędy OOM, opóźnienia i stabilność pod typowym oraz szczytowym obciążeniem. Na Docker Desktop uwzględnij także limit pamięci przydzielonej maszynie wirtualnej Docker.

**Podsumowanie:** zmierz, zdiagnozuj, napraw przyczynę, a następnie ustaw i zweryfikuj limit. Restart jest działaniem doraźnym, nie rozwiązaniem problemu.

