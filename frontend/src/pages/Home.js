import React from 'react';
import { useTranslation } from 'react-i18next';
import { downloadTemplate } from '../utils/api';

function Home({ onStartAssessment }) {
  const { t, i18n } = useTranslation();

  const handleDownloadTemplate = async () => {
    try {
      await downloadTemplate(i18n.language);
    } catch (error) {
      console.error('Error downloading template:', error);
      alert('Error downloading template');
    }
  };

  return (
    <div className="home-page">
      <div className="hero-section">
        <h2>{t('home.welcome')}</h2>
        <p className="hero-description">{t('home.description')}</p>

        <div className="hero-actions">
          <button className="btn btn-primary" onClick={onStartAssessment}>
            {t('home.start')}
          </button>
          <button className="btn btn-secondary" onClick={handleDownloadTemplate}>
            {t('home.template')}
          </button>
        </div>
      </div>

      <div className="features-section">
        <h3>{t('home.features.title')}</h3>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">&#9745;</div>
            <p>{t('home.features.feature1')}</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">&#128200;</div>
            <p>{t('home.features.feature2')}</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">&#128161;</div>
            <p>{t('home.features.feature3')}</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">&#128190;</div>
            <p>{t('home.features.feature4')}</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">&#127757;</div>
            <p>{t('home.features.feature5')}</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">&#9889;</div>
            <p>{t('home.features.feature6')}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
