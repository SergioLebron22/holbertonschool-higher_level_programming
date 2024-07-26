document.getElementById('add_item').addEventListener('click', function() {
    const ulElement = document.querySelector('.my_list');
    
    const liElement = document.createElement('li');
    liElement.textContent = 'Item';

    ulElement.appendChild(liElement)
})