import React from 'react'
import { useState, useEffect } from "react";
import Time from "./Time";
import student_img from "../../../static/images/21-02108.jpg";
import QR_img from "../../../static/images/shopee_QR.png";
export default function StudentCard() {
    const $ = document.querySelector.bind(document);
    const [mounted, setMounted] = useState(false);
    function handleClickRotate() {
        const cardFlip = $(".flip--card__inner");
        cardFlip.classList.toggle("rotate");
    }
    function handleCloseQR() {
        const QRCard = $(".modal");
        QRCard.classList.remove("open");
        setTimeout(() => {
            setMounted(!mounted)
        }, 200)
    }
    function handleOpenQR() {
        const QRCard = $(".modal");
        QRCard.classList.add("open");
        setTimeout(() => {
            setMounted(!mounted)
        }, 200)
    }

    // function handleRemoveQR() {
    //     const QRCard = $(".modal");
    //     QRCard.classList.add("open");
    //     setTimeout(() => {
    //         setMounted(!mounted)
    //     }, 200)
    // }
    return (
        <div className="wrapper--container" id="container">
            <div className="card--qr">
                <i className="fa-solid fa-qrcode" onClick={
                    handleOpenQR
                }></i>
            </div>
            <div className={`modal ${mounted ? 'open' : ""}`}>
                <div className="modal--contain">
                    {
                        mounted && <div className="modal--qr">
                            <img className="modal--qr__img" src={QR_img} alt="qr" />
                            <Time props={handleCloseQR} />
                        </div>
                    }
                    <div className="modal--qr__bg"></div>
                </div>
            </div>

            <div className="wrapper--flip__card">
                <div className="flip--card__inner" onClick={handleClickRotate}>
                    <div className="front">
                        <div className="wrapper--front__infor">
                            <figure className="flip--card__img">
                                <img src={student_img} alt="" width="150px" />
                                <figcaption>指定番号<span>東京1026</span></figcaption>
                            </figure>
                            <div className="card--user__infor">
                                <h1 className="card--title">
                                    学生証
                                </h1>
                                <div className="card--description">
                                    <span className="card--items__title">分野名 <span></span> </span>
                                    <p className="card--description__p">工業専門課程</p>
                                </div>
                                <div className="card--description">
                                    <span className="card--items__title">学科名<span></span></span>
                                    <p className="card--description__p">情報処理学科</p>
                                </div>
                                <div className="card--description">
                                    <span className="card--items__title">学籍番号<span></span></span>
                                    <p className="card--description__p">21 - 02108</p>
                                </div>
                                <div className="card--description">
                                    <span className="card--items__title">氏名<span></span></span>
                                    <p className="card--description__p">LE HOANG PHUC</p>
                                </div>
                                <div className="card--description">
                                    <span className="card--items__title">生年月日<span></span></span>
                                    <p className="card--description__p">2000年12月123日</p>
                                </div>
                                <div className="card--description">
                                    <span className="card--items__title">発行日<span></span></span>
                                    <p className="card--description__p">2022年4月1日</p>
                                </div>
                                <div className="card--description">
                                    <span className="card--items__title">有効期限<span></span></span>
                                    <p className="card--description__p">2023年3月31日</p>
                                </div>
                            </div>
                        </div>

                        <div className="card--school__description">

                            <div className="card--school__description__p">上記の者は本校学生であることを証明する。</div>
                            <div className="card--school__description__p">東京情報クリエイター工学院専門学校。</div>
                        </div>
                    </div>
                    <div className="back">
                        <div className="wrapper--back__infor">
                            <div className="table--back__infor">
                                <div className="table--back__infor__row">
                                    <div className="table--back__infor__items">
                                        <div className="table--row__header">
                                            <p className="table--row__description_p">発行者</p>
                                        </div>
                                        <div className="table--row__description">
                                            <p className="table--row__description_p">
                                                東京情報クリエイター工学院専門学校
                                            </p>
                                            <p className="table--row__description_p">
                                                校長 LE HOANG PHUC
                                            </p>
                                            <p className="table--row__description_p">
                                                東京都千代田区神保町1-50
                                            </p>
                                        </div>
                                    </div>
                                </div>
                                <div className="table--back__infor__row">
                                    <div className="table--back__infor__items">

                                        <div className="table--row__header">
                                            学生住所
                                        </div>
                                        <div className="table--row__description">
                                            <p className="table--row__description_p">東京都千代田区神保町1</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div >
    )
}