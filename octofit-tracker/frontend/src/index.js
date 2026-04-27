import React from 'react';
import ReactDOM from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const codespace = process.env.REACT_APP_CODESPACE_NAME;
const backendOrigin = codespace
  ? `https://${codespace}-8000.app.github.dev`
  : 'http://localhost:8000';

console.log('REACT_APP_CODESPACE_NAME:', codespace);
console.log('Backend origin set to:', backendOrigin);

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
