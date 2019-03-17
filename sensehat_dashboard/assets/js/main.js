let colorPicker = document.getElementById('color');
let button = document.getElementById('button');

button.addEventListener('click', () => {
    document.write(colorPicker.value);
});