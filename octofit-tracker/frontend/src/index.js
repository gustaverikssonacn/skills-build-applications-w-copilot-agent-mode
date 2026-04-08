

import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';


// Ensure REACT_APP_CODESPACE_NAME is set from environment or fallback to window location
if (!process.env.REACT_APP_CODESPACE_NAME) {
  const match = window.location.hostname.match(/^(.*)-8000\.app\.github\.dev/);
  if (match) {
    process.env.REACT_APP_CODESPACE_NAME = match[1];
  }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
