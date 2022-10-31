import React from 'react';
import { Routes, Route, Link } from "react-router-dom"
import logo from "../../static/images/logo512.png";
import student_img from "../../static/images/21-02108.jpg";
import StudentCard from "./StudentCard/StudentCard"

export default function App() {
    console.log(logo)

    return (
        <header>
            <nav id="main-navbar" className="navbar">
                <div className="container-fluid">
                    <button className="btn navbar--list__btn">
                        <i className="navbar--icon fas fa-bars fa-lg"></i>
                    </button>
                    <div className="navbar--options__right">
                        <span className="navbar--user__name">LE HOANG PHUC</span>
                        <button type="submit" className="btn narvbar--logout__btn separate">Logout</button>
                    </div>
                    <div className="wrapper--navbar__list">
                        <div className="navbar--list__controller">

                            <div className="navbar--list__Logo">
                                {/* <img src={logo} alt="School logo" className="" /> */}
                            </div>
                            <button className="btn btn--close__mobile"><i className="fa-solid fa-circle-xmark"></i></button>
                        </div>
                        <ul className="navbar--list">
                            <li className="navbar--items active">
                                <i className="fa-solid fa-house"></i>
                                <Link to="/">ホーム</Link>
                            </li>
                            <li className="navbar--items">
                                <i className="fa-regular fa-address-card"></i>
                                <Link to="/card">学生証</Link>
                            </li>
                            <li className="navbar--items">
                                <i className="fa-solid fa-book"></i>
                                <Link to="/library">図書</Link>
                            </li>
                            <li className="navbar--items">
                                <i className="fa-regular fa-comment"></i>
                                <Link to="message">チャット</Link>
                            </li>
                            <li className="navbar--items">
                                <i className="fa-solid fa-user-group"></i>
                                <Link to="studentsmanagement">学生管理</Link>
                            </li>
                            <li className="navbar--items">
                                <i className="fa-solid fa-arrow-right-from-bracket"></i>
                                <span >ログアウト</span>
                            </li>
                        </ul>
                        <hr />
                        <ul className="navbar--list">
                            <li className="navbar--items">
                                <i className="fa-solid fa-gear"></i>
                                <Link to="/settings">設定</Link>
                            </li>
                            <li className="navbar--items">
                                <i className="fa-regular fa-circle-question"></i>
                                <Link to="/contact">ヘルプ</Link>
                            </li>
                        </ul>
                    </div>
                    <div className="navbar--list__bg"></div>

                </div>

            </nav>
            <Routes>
                {/* <Route path="/" element={<Home />} style={{
                    position: "relative",
                    top: "300px",
                }}></Route> */}
                <Route path="/card" element={<StudentCard />} ></Route>
                {/* <Route path="/news" element={<News />} ></Route> */}
            </Routes>
        </header>

    );
}