

import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Dynamically set the backend API base URL for the codespace
const codespaceName = process.env.REACT_APP_CODESPACE_NAME || window.location.hostname.split('-8000')[0];
const protocol = window.location.protocol;
const host = codespaceName ? `${protocol}//${codespaceName}-8000.app.github.dev` : '';
window.REACT_APP_CODESPACE_URL = host;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
