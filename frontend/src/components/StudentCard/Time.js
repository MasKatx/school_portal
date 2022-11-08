import React from 'react';
import { useState, useLayoutEffect, useCallback } from "react";
function Time({ props }) {
    const [time_m, setTime_m] = useState(5);
    const [time_sec, setTime_sec] = useState(0);
    const handleReloadQR = useCallback(function () {
        setTime_m(5)
        setTime_sec(0)
    }, [])
    useLayoutEffect(() => {
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
        }, 1000)
        return () => clearInterval(timerID)
    }, []);
    return (
        <div className="flip--card__created__Datetime">
            <span className="card--time">
                <span>有効期限：
                    {time_m < 10 && 0}{time_m}:{time_sec < 10 && 0}{time_sec}</span>
                {time_m === 0 && time_sec === 0 ? (<span className="card--time__expdate">有効期限が切れています</span>) : ("")}
            </span>
            <div className="modal--qr__controller">
                <i className="btn--close__mobile fa-solid fa-circle-xmark" onClick={props}></i>
                <i className="btn--update fa-solid fa-rotate-right" onClick={handleReloadQR}></i>
            </div>
        </div>)
}
export default React.memo(Time);
