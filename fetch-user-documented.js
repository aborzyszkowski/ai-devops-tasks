/**
 * Pobiera dane użytkownika z API i przekształca je do uproszczonego obiektu.
 *
 * @param {string|number} userId - Identyfikator użytkownika używany w adresie API.
 * @returns {Promise<{name: string, email: string, lastLogin: Date}|null>}
 * Obietnica z danymi użytkownika albo `null`, jeśli pobieranie lub przetwarzanie się nie powiedzie.
 */
function fetchUserData(userId) {
  return fetch(`https://api.example.com/users/${userId}`)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      return {
        name: data.name,
        email: data.email,
        lastLogin: new Date(data.lastLoginTimestamp)
      };
    })
    .catch(error => {
      console.error('Fetch error:', error);
      return null;
    });
}
