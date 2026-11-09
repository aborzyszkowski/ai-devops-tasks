# Zadanie 29

## Plik JCasC

Konfiguracja znajduje się w pliku [`jenkins-casc.yaml`](./jenkins-casc.yaml). JCasC (Jenkins Configuration as Code) ładuje ustawienia kontrolera z YAML, dzięki czemu konfigurację można przechowywać w repozytorium i odtwarzać.

Plik ustawia liczbę executorów, tryb pracy, krótki czas oczekiwania przed buildem oraz liczbę prób checkoutu. Definiuje również instalacje Maven i Node.js, ścieżkę do Docker CLI oraz przykładowe zadanie Pipeline. Limit czasu 30 minut znajduje się w opcjach przykładowego Pipeline — standardowo timeout jest ustawiany dla zadania lub etapu, a nie jako globalny limit wszystkich buildów kontrolera.

## Wtyczki i wymagania

JCasC **konfiguruje** Jenkins, ale nie instaluje wtyczek, od których zależy konfiguracja. Przykładowy zestaw potrzebnych wtyczek to:

- `configuration-as-code` — ładowanie YAML;
- `job-dsl` — tworzenie zadania z sekcji `jobs`;
- `workflow-aggregator` — pipeline deklaratywny i workflow steps;
- `maven-plugin` — konfiguracja narzędzia Maven;
- `nodejs` — konfiguracja instalacji Node.js;
- `docker-workflow` — integracja Pipeline z Dockerem.

Wtyczki należy zainstalować przed zastosowaniem JCasC, na przykład na obrazie Jenkins:

```dockerfile
FROM jenkins/jenkins:lts-jdk21
RUN jenkins-plugin-cli --plugins \
    configuration-as-code \
    job-dsl \
    workflow-aggregator \
    maven-plugin \
    nodejs \
    docker-workflow
COPY jenkins-casc.yaml /var/jenkins_home/casc_configs/jenkins.yaml
ENV CASC_JENKINS_CONFIG=/var/jenkins_home/casc_configs/jenkins.yaml
```

Zapis w komentarzu na początku pliku YAML jest wyłącznie listą informacyjną — Jenkins nie interpretuje go jako konfiguracji ani instalatora wtyczek.

## Uruchomienie

1. Zainstaluj Docker i przygotuj obraz Jenkins z powyższymi wtyczkami albo zainstaluj wtyczki w istniejącej instancji.
2. Skopiuj `jenkins-casc.yaml` do kontrolera Jenkins. Możesz użyć zmiennej `CASC_JENKINS_CONFIG` wskazującej plik lub katalog z konfiguracją. W przykładzie Docker plik trafia do katalogu `casc_configs`.
3. Uruchom Jenkins. Przy starcie JCasC załaduje konfigurację i utworzy zadanie `example-pipeline`. Sprawdź logi kontrolera w razie błędów konfiguracji.
4. Otwórz Jenkins w przeglądarce pod skonfigurowanym adresem. Dla wdrożenia produkcyjnego zmień `http://localhost:8080/` na właściwy zewnętrzny adres.
5. Upewnij się, że agenci mają dostęp do JDK, wymaganych narzędzi, sieci i Docker daemon. Instalatory Maven/Node.js mogą potrzebować dostępu do Internetu; ścieżka Docker CLI `/usr/bin/docker` jest przykładowa i musi odpowiadać środowisku agenta.

Przykładowe uruchomienie kontenera z już zbudowanego obrazu:

```bash
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  my-jenkins-casc:latest
```

Nie udostępniaj portu Jenkins bezpośrednio niezabezpieczonego do Internetu; w produkcji skonfiguruj TLS, uwierzytelnianie, kopie zapasowe i ograniczony dostęp administratorów. Przykład pipeline używa `sh`, więc wymaga agenta Linux/macOS, a `checkout scm` wymaga zadania powiązanego z repozytorium.
