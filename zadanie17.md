# Zadanie 17

## Rozwiązanie

Funkcja `getCompletedTaskTitles` znajduje się w pliku [`task-filter.js`](./task-filter.js). Filtruje zadania o statusie `completed`, sortuje je rosnąco po numerycznym `id` i zwraca tablicę ich tytułów.

```js
function getCompletedTaskTitles(tasks) {
  return tasks
    .filter(task => task.status === 'completed')
    .sort((a, b) => a.id - b.id)
    .map(task => task.title);
}

module.exports = getCompletedTaskTitles;
```

`filter` wybiera ukończone zadania, `sort` ustawia je według identyfikatora rosnąco, a `map` tworzy wynikową tablicę tytułów. Sortowanie działa na nowej tablicy utworzonej przez `filter`, więc nie zmienia kolejności elementów w tablicy przekazanej do funkcji.

## Przykład użycia

```js
const getCompletedTaskTitles = require('./task-filter');

const tasks = [
  { id: 3, title: 'Wdrożenie', status: 'completed' },
  { id: 1, title: 'Konfiguracja', status: 'completed' },
  { id: 2, title: 'Testy', status: 'in progress' }
];

console.log(getCompletedTaskTitles(tasks));
// ['Konfiguracja', 'Wdrożenie']
```

Przykład zakłada, że `id` jest liczbą. Jeśli nie ma zadań ze statusem `completed`, funkcja zwraca pustą tablicę.
