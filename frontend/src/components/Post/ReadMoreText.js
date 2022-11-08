import React, { useState, useRef, useLayoutEffect } from 'react';
import debounce from 'lodash.debounce';
var classnames = require('classnames');

const ReadMoreText = ({ text }) => {
    const [clamped, setClamped] = useState(true);
    const [showButton, setShowButton] = useState(true);
    const containerRef = useRef(null);
    const handleClick = () => setClamped(!clamped);
    useLayoutEffect(() => {
        const hasClamping = (el) => {
            const { clientHeight, scrollHeight } = el;
            return clientHeight !== scrollHeight;
        };

        const checkButtonAvailability = () => {
            if (containerRef.current) {
                // Save current state to reapply later if necessary.
                const hadClampClass = containerRef.current.classList.contains("clamp");
                // Make sure that CSS clamping is applied if aplicable.
                if (!hadClampClass) containerRef.current.classList.add("clamp");
                // Check for clamping and show or hide button accordingly.
                setShowButton(hasClamping(containerRef.current));
                // Sync clamping with local state.
                if (!hadClampClass) containerRef.current.classList.remove("clamp");
            }
        };

        const debouncedCheck = debounce(checkButtonAvailability, 50);

        checkButtonAvailability();
        window.addEventListener("resize", debouncedCheck);
        return () => {
            window.removeEventListener("resize", debouncedCheck);
        };
    }, [containerRef]);

    return (
        <div className="post--contain">
            <div

                ref={containerRef}
                className={classnames("long-text", clamped && "clamp")}
            >
                {text}
            </div>
            {showButton && (
                <button className="post--contain__btn-read-more" onClick={handleClick}>{clamped ? "もっと見る" : "簡易表示"}</button>
            )}
        </div>
    );
};

export default ReadMoreText