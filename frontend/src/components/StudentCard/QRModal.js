import React from 'react';
import QR_img from "../../../static/images/shopee_QR.png";
import { useState, useEffect, useCallback } from "react";
import Time from "./Time"

function QRModal() {
    return (
        <div className="modal">
            <div className="modal--contain">
                <div className="modal--qr">
                    <img className="modal--qr__img" src={QR_img} alt="qr" />
                    <Time />
                </div>
                <div className="modal--qr__bg"></div>
            </div>
        </div>
    )
}

export default QRModal