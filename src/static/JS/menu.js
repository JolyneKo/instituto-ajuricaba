const wrapper = document.querySelector('.mobile__wrapper');
const header = document.querySelector('.header');
const icon = document.querySelector('.header__menu__icon');
const menu = document.querySelector('.menu');
const category1 = document.querySelector('.category--1');
const category2 = document.querySelector('.category--2');
const category3 = document.querySelector('.category--3');

// Abrir/fechar menu quando clicar no botão de abrir menu
icon.addEventListener('click', () => {
    menu.classList.toggle('menu--open');
    wrapper.classList.toggle('menu--open');
    header.classList.toggle('menu--open--header');
});



// Quando apertar na primeira categoria do menu
category1.addEventListener('click', () => {

    const items = document.querySelectorAll('.category--items');

    items.forEach(item => {
        if (!item.classList.contains("category__items--1")) {    
            item.classList.remove('category--open')
        }
    });

    const category = document.querySelector('.category__items--1');
    category.classList.toggle('category--open');
});

// Quando apertar na segunda categoria do menu
category2.addEventListener('click', () => {
    const items = document.querySelectorAll('.category--items');

    items.forEach(item => {
        if (!item.classList.contains("category__items--2")) {
            item.classList.remove('category--open')
        }
    });

    const category = document.querySelector('.category__items--2');
    category.classList.toggle('category--open');
});

// Quando apertar na terceira categoria do menu
category3.addEventListener('click', () => {

    const items = document.querySelectorAll('.category--items');

    items.forEach(item => {
        if (!item.classList.contains("category__items--3")) {
            item.classList.remove('category--open')
        }
    });

    const category = document.querySelector('.category__items--3');
    category.classList.toggle('category--open');
});