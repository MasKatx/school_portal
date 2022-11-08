import { Routes, Route } from "react-router-dom";
import React from 'react';
import StudentCard from "./StudentCard/StudentCard";
import Post from "./Post/Post";
import Library from "./Library/Library";
import Chat from "./Chat/Chat";
import Navbar from "./Navbar";

function App() {
    return (
        <>
            <Navbar />
            <Routes>
                <Route extra path="/home" element={<Post />} ></Route>
                <Route path="/card" element={<StudentCard />} ></Route>
                <Route path="/library" element={<Library />} ></Route>
                <Route path="/message" element={< Chat />} ></Route>
                <Route path="/settings" element={<Post />} ></Route>
                <Route path="/studentsmanagement" element={<Post />} ></Route>
                <Route path="/help" element={<Post />} ></Route>
            </Routes>
        </>

    );
}

export default App;