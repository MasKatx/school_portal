const $ = document.querySelector.bind(document);
const $$ = document.querySelectorAll.bind(document);

function App() {
    const navbarBtn = $('.btn.navbar--list__btn');
    const navbar = $('.wrapper--navbar__list');
    const navbarBackground = $('.navbar--list__bg');
    const navbarItems = $$('.navbar--items');
    const CloseBtn = $('.btn--close__mobile');
    const StudentCard = document.querySelector(".flip--card__inner");

    const handleCloseNavbar = function () {
        navbar.classList.remove('navbar--list__toggle')
    }

    const handleOpenNavbar = function () {
        navbar.classList.add('navbar--list__toggle')
    }

    const handleActive = function () {

        if ($(".navbar--items.active")) {
            $(".navbar--items.active").classList.remove("active")
        }
        this.classList.add("active")

    }
    function handleClick() {
        StudentCard.classList.toggle("rotate")
    }


    CloseBtn.onclick = handleCloseNavbar;
    navbarBackground.onclick = handleCloseNavbar;
    navbarBtn.onclick = handleOpenNavbar;
    navbarItems.forEach((item, index) => {
        item.onclick = handleActive
    });
    StudentCard.onclick = handleClick;
};

App();