import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { createRoot } from 'react-dom/client'

// import style files
import "./../static/css/base.css";
import "./../static/css/home.css";
import "./../static/css/loginChange.css";
import "./../static/css/responsive.css";
import "./../static/font/fontawesome-free-6.0.0/css/all.min.css";

// import components
import App from './components/App';

const root = createRoot(document.getElementById('app'));
root.render(
    <React.StrictMode>
        <Router>
            <App />
        </Router>
    </React.StrictMode>
);

