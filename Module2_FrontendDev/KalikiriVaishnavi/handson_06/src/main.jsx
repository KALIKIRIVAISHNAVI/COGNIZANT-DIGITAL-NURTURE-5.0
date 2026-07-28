import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import { BrowserRouter } from 'react-router-dom'
import { EnrollmentProvider } from './EnrollmentContext.jsx' // Import the Provider

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <EnrollmentProvider> {/* Wrap it around everything! */}
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </EnrollmentProvider>
  </React.StrictMode>,
)