// dark - light switcher

const block = document.getElementsByClassName('dark-light-switch')
const switcher = document.getElementsByClassName('switcher');
let count_clicker = 0;

//
// Анимации туда-сюда
//

const keyframes_right = [
  { left: '.25em', backgroundColor: 'black'},
  { left: '2.25em', backgroundColor: 'white'}
];

const keyframes_left = [
  { left: '2.25em', backgroundColor: 'white'},
  { left: '.25em', backgroundColor: 'black' }
];

//
// Тайминги
//

const animate_timing = {
  duration: 150,
};

//
// Event
//

block[0].addEventListener('click', function () {
    if (count_clicker % 2 == 0){
        switcher[0].style.backgroundColor = '#fff';
        switcher[0].animate(keyframes_right, animate_timing);
        switcher[0].style.left = '2.25em';
        //
        // смена страницы на Светлую
        document.body.style.color = '#000000';
        document.getElementsByClassName('header')[0].style.backgroundColor = '#fff';
        document.getElementsByClassName('header')[0].style.color = '#000000';
        document.getElementsByClassName('main-content')[0].style.backgroundColor = '#ECF3F5';
    }
    else {
        switcher[0].style.backgroundColor = '#1f1f1f';
        switcher[0].animate(keyframes_left, animate_timing);
        switcher[0].style.left = '.25em';
        //
        // смена страницы на Темную
        document.body.style.color = '#888888';
        document.getElementsByClassName('header')[0].style.backgroundColor = '#383838';
        document.getElementsByClassName('header')[0].style.color = '#000';
        document.getElementsByClassName('main-content')[0].style.backgroundColor = '#1f1f1f';
    }

    count_clicker = count_clicker + 1;
});
