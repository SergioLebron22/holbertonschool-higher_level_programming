document.addEventListener('DOMContentLoaded', function() {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    fetch(url)
    .then(response => response.json())
    .then(data => {
        const movies = data.results;
        const ulElement = document.getElementById('list_movies');
        movies.forEach(movie => {
            const liElement = document.createElement('li');
            liElement.textContent = movie.title;
            ulElement.appendChild(liElement);
        });
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
});