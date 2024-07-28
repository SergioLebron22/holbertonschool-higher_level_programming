document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const name = data.name;
        document.getElementById('character').textContent = name;
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});