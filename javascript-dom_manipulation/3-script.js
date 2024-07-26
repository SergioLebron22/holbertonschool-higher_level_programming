document.getElementById('toggle_header').addEventListener('click', function() {
    const element = document.querySelector('header');

    if (element.classList.contains('red')){
        element.classList.remove('red');
        element.classList.add('green');
    }
    else {
        element.classList.remove('green');
        element.classList.add('red')
    }
})