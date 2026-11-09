# Zadanie 27

## Zależności między etapami pipeline'u

Diagram Mermaid znajduje się w pliku [`jenkins-pipeline.md`](./jenkins-pipeline.md).

1. **Checkout kodu → budowanie aplikacji:** Jenkins pobiera źródła, a następnie buduje aplikację.
2. **Budowanie aplikacji → kontrole jakości:** po zbudowaniu uruchamiane są testy automatyczne, analiza statyczna oraz skanowanie bezpieczeństwa. Te trzy kontrole mogą działać równolegle.
3. **Kontrole jakości → bramka:** obraz Docker jest budowany tylko wtedy, gdy wszystkie kontrole zakończą się powodzeniem. W przeciwnym razie pipeline zatrzymuje się i zgłasza błąd.
4. **Obraz Docker → testy integracyjne:** testy weryfikują współpracę z zależnościami i usługami, używając zbudowanego obrazu.
5. **Testy integracyjne → staging:** poprawny obraz jest wdrażany na środowisko staging. Niepowodzenie testów blokuje wdrożenie.
6. **Staging → akceptacja → produkcja:** po testach akceptacyjnych na stagingu następuje bramka akceptacji. Dopiero jej przejście pozwala wdrożyć aplikację na produkcję.
7. **Produkcja → monitorowanie:** po wdrożeniu obserwuje się działanie aplikacji, aby szybko wykryć problemy.

W rzeczywistym Jenkinsie kontrolę bezpieczeństwa i akceptację produkcji należy skonfigurować zgodnie z polityką zespołu. Dostęp do poświadczeń wdrożeniowych powinien być ograniczony, a wdrożenie na produkcję może wymagać ręcznej zgody.
