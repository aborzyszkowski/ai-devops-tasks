# Zadanie 19

## Refleksja na temat jakości dokumentacji

Dokumentacja jasno przedstawia cel endpointu, dostępne parametry wraz z wartościami domyślnymi i limitem oraz przykłady żądania i odpowiedzi. Tabela ułatwia szybkie sprawdzenie parametrów, a przykłady pokazują, jak z nich korzystać.

Najważniejszym ograniczeniem jest skąpy opis wejściowy: nie określa on formatu odpowiedzi, pól obiektu użytkownika, formatu błędów ani sposobu walidacji parametrów. Dlatego przykładowa odpowiedź została oznaczona jako założenie, a nie gwarantowany kontrakt API. Przed wykorzystaniem dokumentacji jako specyfikacji produkcyjnej należy te szczegóły potwierdzić w implementacji.

Aby dokumentację uzupełnić, warto dodać:

- dokładny schemat odpowiedzi oraz przykłady dla pustej strony i filtra `role`;
- reguły walidacji dla `page` i `limit`, w tym zachowanie dla wartości ujemnych lub większych niż `100`;
- kody HTTP i format odpowiedzi błędów;
- informację o wymaganym uwierzytelnianiu i uprawnieniach, jeśli endpoint ich wymaga.
