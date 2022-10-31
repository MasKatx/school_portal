import { useState, useEffect } from "react";


export default function StudentCard() {
    const date = new Date();
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate()
    const [time_m, setTime_m] = useState(5);
    const [time_sec, setTime_sec] = useState(0);

    const handleReloadQR = function () {

        setTime_m(5)
    };

    useEffect(() => {

        const timerID = setInterval(() => {
            setTime_sec(prevSec => {
                if (prevSec <= 0) {
                    setTime_m(prevMin => {
                        if (prevMin <= 0) {
                            setTime_sec(0)
                            return 0
                        }
                        else if (prevSec === 0 && prevMin === 0) {
                            return 0
                        }
                        return prevMin - 1
                    })
                    return prevSec = 59
                }
                return prevSec - 1;
            });
        }, 10)

        return () => clearInterval(timerID)
    }, [])

    function handleClick() {
        const card = document.querySelector(".flip-card-inner")
        card.classList.toggle("rotate")
    }
    return (
        <>
            <div className="wrapper-flip-card" >
                <div className="flip-card-created-Datetime">
                    <span>Date Created: </span>
                    <span>{year + "/" + month + "/" + day}</span>
                    <div className="card-time"> Expiration Time {time_m < 10 && 0}{time_m}:{time_sec < 10 && 0}{time_sec}</div>
                </div>
                <div className="card-reload" onClick={handleReloadQR} style={time_m === 0 && time_sec === 0 ? { display: 'flex' } : { display: 'none' }}>{time_m === 0 && time_sec === 0 ? (<i className="fa-solid fa-rotate-right"></i>) : ('')}</div>
                <div className="flip-card-inner" onClick={handleClick}>
                    <div className="front" >
                        <span>Font</span>
                    </div>
                    <div className="back" >
                        <span>Back</span>
                    </div>
                </div>
            </div>
        </>
    )
}