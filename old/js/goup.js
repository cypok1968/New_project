// получить доступ к кнопке
const topBtn = document.querySelector(".go-top");

// Скроллинг окна
window.addEventListener("scroll", trackScroll);
// Реакция на нажатие
topBtn.addEventListener("click", goTop);

function trackScroll() {
    // положение от верхушки окна
    const scrolled = window.pageYOffset;
    // console.log(scrolled);
    // высота окна браузера
    const wh = document.documentElement.clientHeight;
    // console.log(wh);
    // в прокрутке вышли за пределы одного экрана
    if(scrolled > wh) {
    // должна показаться кнопка
    //topBtn.classList.add("go-top--show");
    topBtn.style.display = 'block';
    } else {
    // или исчезает
    //topBtn.classList.remove("go-top--show");
    topBtn.style.display = 'none';
    }
}

function goTop() {
    // пока не дошли до верха
    if (window.pageYOffset > 0) {
    // скроллим к верху
    window.scrollBy(0, -500); // по Y на 28 px
    setTimeout(goTop, 0); // рекурсивный вызов через задержку
    }
}