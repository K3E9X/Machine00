import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import './styles/App.css';
import Home from './pages/Home';
import Questionnaire from './pages/Questionnaire';
import Results from './pages/Results';

function App() {
  const { t, i18n } = useTranslation();
  const [currentPage, setCurrentPage] = useState('home');
  const [results, setResults] = useState(null);

  const toggleLanguage = () => {
    const newLang = i18n.language === 'fr' ? 'en' : 'fr';
    i18n.changeLanguage(newLang);
  };

  const handleStartAssessment = () => {
    setCurrentPage('questionnaire');
    setResults(null);
  };

  const handleSubmitResults = (resultData) => {
    setResults(resultData);
    setCurrentPage('results');
  };

  const handleNewAssessment = () => {
    setResults(null);
    setCurrentPage('questionnaire');
  };

  const handleGoHome = () => {
    setCurrentPage('home');
  };

  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1>{t('app.title')}</h1>
          <div className="header-actions">
            <button className="lang-button" onClick={toggleLanguage}>
              {i18n.language === 'fr' ? 'EN' : 'FR'}
            </button>
          </div>
        </div>
      </header>

      <main className="app-main">
        {currentPage === 'home' && (
          <Home onStartAssessment={handleStartAssessment} />
        )}
        {currentPage === 'questionnaire' && (
          <Questionnaire
            onSubmit={handleSubmitResults}
            onBack={handleGoHome}
          />
        )}
        {currentPage === 'results' && results && (
          <Results
            results={results}
            onNewAssessment={handleNewAssessment}
            onGoHome={handleGoHome}
          />
        )}
      </main>

      <footer className="app-footer">
        <p>Security Assessment Tool - Based on OWASP Top 10, ISO 27001, ANSSI</p>
      </footer>
    </div>
  );
}

export default App;
