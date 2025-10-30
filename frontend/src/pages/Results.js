import React from 'react';
import { useTranslation } from 'react-i18next';
import { downloadResults } from '../utils/api';

function Results({ results, onNewAssessment, onGoHome }) {
  const { t, i18n } = useTranslation();

  const handleExport = async () => {
    try {
      await downloadResults(
        {
          responses: results.responses || {},
          app_info: results.app_info || {},
          lang: i18n.language
        },
        i18n.language
      );
    } catch (error) {
      console.error('Error exporting results:', error);
      alert('Error exporting results');
    }
  };

  const getRiskColor = (level) => {
    const colors = {
      'LOW': '#10b981',
      'MEDIUM': '#f59e0b',
      'HIGH': '#ef4444',
      'CRITICAL': '#dc2626'
    };
    return colors[level] || '#6b7280';
  };

  const getPriorityColor = (priority) => {
    const colors = {
      'LOW': '#10b981',
      'MEDIUM': '#f59e0b',
      'HIGH': '#ef4444'
    };
    return colors[priority] || '#6b7280';
  };

  if (!results || !results.score) {
    return (
      <div className="error-container">
        <p>No results available</p>
        <button className="btn btn-primary" onClick={onGoHome}>
          {t('common.back')}
        </button>
      </div>
    );
  }

  const { score, recommendations, app_info } = results;

  return (
    <div className="results-page">
      <div className="results-header">
        <h2>{t('results.title')}</h2>
        {app_info?.name && <p className="app-name">{app_info.name}</p>}
      </div>

      <div className="results-summary">
        <div className="score-card main-score">
          <h3>{t('results.overallScore')}</h3>
          <div
            className="score-value"
            style={{ color: getRiskColor(score.risk_level.level) }}
          >
            {score.percentage}%
          </div>
          <div className="score-details">
            {score.total_score} / {score.max_score} points
          </div>
        </div>

        <div className="score-card">
          <h3>{t('results.riskLevel')}</h3>
          <div
            className="risk-badge"
            style={{
              backgroundColor: getRiskColor(score.risk_level.level),
              color: 'white'
            }}
          >
            {score.risk_level[i18n.language]}
          </div>
        </div>

        <div className="score-card">
          <h3>{t('results.recommendation')}</h3>
          <div
            className="recommendation-badge"
            style={{
              backgroundColor: getPriorityColor(score.audit_recommendation.priority),
              color: 'white'
            }}
          >
            {score.audit_recommendation[i18n.language]}
          </div>
        </div>
      </div>

      <div className="category-breakdown-section">
        <h3>{t('results.categoryBreakdown')}</h3>
        <div className="categories-grid">
          {Object.entries(score.category_scores).map(([catId, catScore]) => {
            let categoryName = catId;

            // This would ideally come from the questions data
            const categoryNames = {
              'iam': {
                'fr': 'Gestion des Identités et des Accès',
                'en': 'Identity and Access Management'
              },
              'network_architecture': {
                'fr': 'Architecture Réseau',
                'en': 'Network Architecture'
              },
              'interconnections': {
                'fr': 'Flux et Interconnexions',
                'en': 'Flows and Interconnections'
              },
              'hosting_infrastructure': {
                'fr': 'Hébergement et Infrastructure',
                'en': 'Hosting and Infrastructure'
              },
              'data_security': {
                'fr': 'Sécurité des Données',
                'en': 'Data Security'
              },
              'application_security': {
                'fr': 'Sécurité Applicative',
                'en': 'Application Security'
              },
              'logging_monitoring': {
                'fr': 'Journalisation et Surveillance',
                'en': 'Logging and Monitoring'
              }
            };

            if (categoryNames[catId]) {
              categoryName = categoryNames[catId][i18n.language];
            }

            const percentage = catScore.percentage;
            const barColor = percentage >= 80 ? '#10b981' :
                           percentage >= 60 ? '#f59e0b' :
                           percentage >= 40 ? '#ef4444' : '#dc2626';

            return (
              <div key={catId} className="category-score-card">
                <div className="category-score-header">
                  <h4>{categoryName}</h4>
                  <span className="category-percentage">{percentage}%</span>
                </div>
                <div className="category-score-bar">
                  <div
                    className="category-score-fill"
                    style={{
                      width: `${percentage}%`,
                      backgroundColor: barColor
                    }}
                  ></div>
                </div>
                <div className="category-score-details">
                  {catScore.score} / {catScore.max_score}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {recommendations && recommendations.length > 0 && (
        <div className="recommendations-section">
          <h3>{t('results.recommendations')}</h3>
          <div className="recommendations-list">
            {recommendations.map((rec, idx) => (
              <div key={idx} className="recommendation-card">
                <div className="recommendation-header">
                  <span
                    className="severity-badge"
                    style={{
                      backgroundColor: rec.severity === 'high' ? '#ef4444' : '#f59e0b'
                    }}
                  >
                    {rec.severity === 'high' ? t('results.high') : t('results.medium')}
                  </span>
                  <span className="recommendation-category">{rec.category}</span>
                </div>
                <p className="recommendation-text">{rec.question}</p>
                <div className="recommendation-standards">
                  <span className="standards-label">{t('results.standards')}:</span>
                  {rec.standard.map((std, i) => (
                    <span key={i} className="standard-tag">{std}</span>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {(!recommendations || recommendations.length === 0) && (
        <div className="no-recommendations">
          <p>{t('results.noRecommendations')}</p>
        </div>
      )}

      <div className="results-actions">
        <button className="btn btn-secondary" onClick={onGoHome}>
          {t('common.back')}
        </button>
        <button className="btn btn-secondary" onClick={handleExport}>
          {t('results.exportExcel')}
        </button>
        <button className="btn btn-primary" onClick={onNewAssessment}>
          {t('results.newAssessment')}
        </button>
      </div>
    </div>
  );
}

export default Results;
