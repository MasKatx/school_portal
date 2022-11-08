import React, { useState, useRef, useEffect, useLayoutEffect } from 'react';
import student_img from "../../../static/images/21-02108.jpg";
import ReadMoreText from "./ReadMoreText";

export default function Post() {
    const postAPI = "http://localhost:3000/posts"
    const [posts, setPosts] = useState([])
    useLayoutEffect(() => {
        fetch(postAPI)
            .then(function (response) {
                return response.json();
            })
            .then((dataObject) => {
                setPosts(dataObject)
            })
    }, []);



    return (
        <div className="wrapper--post__container">
            {posts.map((post, index) => (
                <div key={index} className="post--container">
                    <div className="post--header">
                        <div className="post--header__img">
                            <img className="post--user__avatar" src={student_img} alt="" width="150px" />
                        </div>
                        <div className="post--header__info">
                            <span className="post--header__username">{post.poster}</span>
                            <span className="post--header__datetime">{post.created_at}</span>
                        </div>
                        <div className="post--header__pin"><i className="fa-solid fa-thumbtack"></i></div>
                    </div>
                    <ReadMoreText text={post.post_contain} />

                </div>
            ))}
        </div>
    )
}