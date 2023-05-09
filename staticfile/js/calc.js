// Necessary HTML Tags or Buttons
const preview = document.getElementById('preview');
const result = document.getElementById('result');
const buttons = document.querySelectorAll('button');

// All Functions
for (let button of buttons) {
    button.addEventListener('click', function (e) {
        let myInput = e.target.innerText;
        if (myInput == 'AC') {
            preview.innerText = '';
            result.innerText = '';
        } else if (myInput == '⌫') {
            const previousNumber = preview.innerText;
            preview.innerText = previousNumber.substring(0, previousNumber.length - 1);
            result.innerText = '';
        } else if (myInput == '%') {
            result.innerText = Number(preview.innerText) / 100;
            preview.innerText = Number(result.innerText);
        } else if (myInput == '×') {
            myInput = '*';
            preview.innerText += '*';
        } else if (myInput == '÷') {
            myInput = '/';
            preview.innerText += '/';
        } else if (myInput == '=') {
            const evalConvert = eval(preview.innerText);
            if (typeof(evalConvert) != 'number') {
                alert('Something is happening wrong !!!')
            } else {
            result.innerText = evalConvert;
        }
        } else {
            preview.innerText += myInput;
        }
    });
};