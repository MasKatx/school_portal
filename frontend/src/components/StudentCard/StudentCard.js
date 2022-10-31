export default function StudentCad() {
    return (<div className="wrapper--container" id="container">
        {/* <div className="card--reload">
                    <i className="fa-solid fa-rotate-right"></i>
                </div> */}
        <div className="wrapper--flip__card">

            <div className="flip--card__created__Datetime">
                <span>
                    発行日：
                    2022/22/22
                </span>
                <span className="card--time">
                    有効期限：
                    00:00
                </span>
            </div>
            <div className="card--qr">
                <i className="fa-solid fa-qrcode"></i>
            </div>

            <div className="flip--card__inner">
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
                                <span className="card--title">分野名 <span></span> </span>
                                <p className="card--description__p">工業専門課程</p>
                            </div>
                            <div className="card--description">
                                <span className="card--title">学科名<span></span></span>
                                <p className="card--description__p">情報処理学科</p>
                            </div>
                            <div className="card--description">
                                <span className="card--title">学籍番号<span></span></span>
                                <p className="card--description__p">21 - 02108</p>
                            </div>
                            <div className="card--description">
                                <span className="card--title">氏名<span></span></span>
                                <p className="card--description__p">LE HOANG PHUC we qwe wqe wqewq e</p>
                            </div>

                        </div>
                    </div>

                    <div className="card--description no__change">上記の者は本校学生であることを証明する。</div>
                    <div className="card--description no__change">東京情報クリエイター工学院専門学校。</div>
                </div>
                <div className="back">
                    <div className="wrapper--back__infor">
                        {/* <table style="border: 1px solid #000; ">
                                    <tr style="border: 1px solid #000;">
                                        <th>発行者</th>
                                        <td>
                                            <p>東京情報クリエイター工学院専門学校</p>
                                            <p>校長 LE HOANG PHUC</p>
                                            <p>東京都千代田区神保町1-50</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <th>学生住所</th>
                                        <td>東京都千代田区神保町1</td>
                                    </tr>
                                </table> */}
                    </div>
                </div>
            </div>
        </div>
    </div>)
}