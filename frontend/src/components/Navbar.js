import React from 'react';
import { NavLink } from "react-router-dom";
import { useCallback } from "react";
import logo from "../../static/images/logo512.png";
function Navbar() {
    const $ = document.querySelector.bind(document);
    const $$ = document.querySelectorAll.bind(document);

    const handleCloseNavbar = useCallback(function () {
        const navbar = $('.wrapper--navbar__list');
        navbar.classList.remove('navbar--list__toggle');
    }, []);

    const handleOpenNavbar = useCallback(function () {
        const navbar = $('.wrapper--navbar__list');
        navbar.classList.add('navbar--list__toggle');
    }, []);

    const handleActive = () => {
        const items = $$('.navbar--items')
        items.forEach(item => {
            item.onclick = function () {
                handleCloseNavbar();
            }
        })
    }
    const itemsList = [
        {
            icon: <i className="fa-solid fa-house"></i>,
            path: "/home",
            path_name: "ホーム"
        },
        {
            icon: <i className="fa-regular fa-address-card"></i>,
            path: "/card",
            path_name: "プロファイル"
        },
        {
            icon: <i className="fa-solid fa-book"></i>,
            path: "/library",
            path_name: "図書"
        },
        {
            icon: <i className="fa-regular fa-comment"></i>,
            path: "/message",
            path_name: "チャット"
        },
        {
            icon: <i className="fa-solid fa-user-group"></i>,
            path: "/studentsmanagement",
            path_name: "学生管理"
        },

        {
            icon: <i className="fa-solid fa-arrow-right-from-bracket"></i>,
            path: "/logout",
            path_name: "ログアウト"
        },
    ]
    const OrtherList = [
        {
            icon: <i className="fa-solid fa-gear"></i>,
            path: "/settings",
            path_name: "設定"
        },
        {
            icon: <i className="fa-regular fa-circle-question"></i>,
            path: "/help",
            path_name: "ヘルプ"
        },
    ]
    return (
        <header>
            <nav id="main-navbar" className="navbar">
                <div className="container-fluid">
                    <button className="btn navbar--list__btn" onClick={handleOpenNavbar}>
                        <i className="navbar--icon fas fa-bars fa-lg"></i>
                    </button>
                    <div className="navbar--options__right">
                        <span className="navbar--user__name">LE HOANG PHUC</span>
                        <button type="submit" className="btn narvbar--logout__btn separate">Logout</button>
                    </div>
                    <div className="wrapper--navbar__list">
                        <div className="navbar--list__controller">

                            <div className="navbar--list__Logo">
                                <img src={logo} alt="School logo" className="" />
                            </div>
                            <button className="btn btn--close__mobile" onClick={handleCloseNavbar}><i className="fa-solid fa-circle-xmark"></i></button>
                        </div>
                        <ul className="navbar--list" onClick={handleActive}>
                            {itemsList.map((item, index) => (
                                <li key={index}>

                                    <NavLink to={item.path} className={({ isActive }) => (isActive ? 'navbar--items active' : 'navbar--items')}>
                                        <div className="navbar--items__content" >
                                            {item.icon}
                                            <span className="navbar--items__link">{item.path_name}</span>
                                        </div>
                                    </NavLink>
                                </li>
                            ))}
                        </ul>
                        <hr />
                        <ul className="navbar--list" >
                            {OrtherList.map((item, index) => (
                                <li key={index}>

                                    <NavLink to={item.path} className={({ isActive }) => (isActive ? 'navbar--items active' : 'navbar--items')}>
                                        <div className="navbar--items__content" >
                                            {item.icon}
                                            <span className="navbar--items__link" >{item.path_name}</span>
                                        </div>
                                    </NavLink>
                                </li>
                            ))}
                        </ul>
                    </div>
                    <div className="navbar--list__bg" onClick={handleCloseNavbar}></div>
                </div>
            </nav>
        </header>
    );
}

export default React.memo(Navbar);