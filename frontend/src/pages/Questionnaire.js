import React, { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import { getQuestions, submitQuestionnaire } from '../utils/api';

function Questionnaire({ onSubmit, onBack }) {
  const { t, i18n } = useTranslation();
  const [loading, setLoading] = useState(true);
  const [questionsData, setQuestionsData] = useState(null);
  const [responses, setResponses] = useState({});
  const [appInfo, setAppInfo] = useState({
    name: '',
    owner: '',
    contact: '',
    environment: 'Production',
    description: ''
  });
  const [currentCategoryIndex, setCurrentCategoryIndex] = useState(0);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadQuestions();
  }, [i18n.language]);

  const loadQuestions = async () => {
    try {
      setLoading(true);
      const data = await getQuestions(i18n.language);
      setQuestionsData(data);
      setLoading(false);
    } catch (err) {
      console.error('Error loading questions:', err);
      setError('Failed to load questions');
      setLoading(false);
    }
  };

  const handleResponseChange = (questionId, value) => {
    setResponses(prev => ({
      ...prev,
      [questionId]: value
    }));
  };

  const handleAppInfoChange = (field, value) => {
    setAppInfo(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const calculateProgress = () => {
    if (!questionsData) return 0;

    let totalQuestions = 0;
    let answeredQuestions = 0;

    questionsData.categories.forEach(category => {
      category.questions.forEach(question => {
        totalQuestions++;
        if (responses[question.id] !== undefined) {
          answeredQuestions++;
        }
      });
    });

    return totalQuestions > 0 ? (answeredQuestions / totalQuestions) * 100 : 0;
  };

  const isCurrentCategoryComplete = () => {
    if (!questionsData || !questionsData.categories[currentCategoryIndex]) return false;

    const currentCategory = questionsData.categories[currentCategoryIndex];
    return currentCategory.questions.every(q => responses[q.id] !== undefined);
  };

  const handleNext = () => {
    if (currentCategoryIndex < questionsData.categories.length - 1) {
      setCurrentCategoryIndex(prev => prev + 1);
    }
  };

  const handlePrevious = () => {
    if (currentCategoryIndex > 0) {
      setCurrentCategoryIndex(prev => prev - 1);
    }
  };

  const handleSubmit = async () => {
    const progress = calculateProgress();
    if (progress < 100) {
      alert(t('questionnaire.required'));
      return;
    }

    try {
      setLoading(true);
      const result = await submitQuestionnaire({
        responses,
        app_info: appInfo,
        lang: i18n.language
      });
      setLoading(false);
      onSubmit(result);
    } catch (err) {
      console.error('Error submitting questionnaire:', err);
      alert('Error submitting questionnaire');
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>{t('common.loading')}</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-container">
        <p>{error}</p>
        <button className="btn btn-primary" onClick={onBack}>
          {t('common.back')}
        </button>
      </div>
    );
  }

  if (!questionsData) return null;

  const currentCategory = questionsData.categories[currentCategoryIndex];
  const progress = calculateProgress();
  const isLastCategory = currentCategoryIndex === questionsData.categories.length - 1;

  return (
    <div className="questionnaire-page">
      <div className="questionnaire-header">
        <button className="btn-back" onClick={onBack}>
          ← {t('common.back')}
        </button>
        <h2>{t('questionnaire.title')}</h2>

        <div className="progress-container">
          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
          <span className="progress-text">{Math.round(progress)}%</span>
        </div>
      </div>

      <div className="app-info-section">
        <h3>{t('questionnaire.appInfo')}</h3>
        <div className="form-grid">
          <div className="form-field">
            <label>{t('questionnaire.appName')}</label>
            <input
              type="text"
              value={appInfo.name}
              onChange={(e) => handleAppInfoChange('name', e.target.value)}
              placeholder={t('questionnaire.appNamePlaceholder')}
            />
          </div>
          <div className="form-field">
            <label>{t('questionnaire.owner')}</label>
            <input
              type="text"
              value={appInfo.owner}
              onChange={(e) => handleAppInfoChange('owner', e.target.value)}
              placeholder={t('questionnaire.ownerPlaceholder')}
            />
          </div>
          <div className="form-field">
            <label>{t('questionnaire.contact')}</label>
            <input
              type="text"
              value={appInfo.contact}
              onChange={(e) => handleAppInfoChange('contact', e.target.value)}
              placeholder={t('questionnaire.contactPlaceholder')}
            />
          </div>
          <div className="form-field">
            <label>{t('questionnaire.environment')}</label>
            <select
              value={appInfo.environment}
              onChange={(e) => handleAppInfoChange('environment', e.target.value)}
            >
              <option value="Production">Production</option>
              <option value="Staging">Staging</option>
              <option value="Development">Development</option>
            </select>
          </div>
        </div>
        <div className="form-field">
          <label>{t('questionnaire.description')}</label>
          <textarea
            value={appInfo.description}
            onChange={(e) => handleAppInfoChange('description', e.target.value)}
            placeholder={t('questionnaire.descriptionPlaceholder')}
            rows={3}
          />
        </div>
      </div>

      <div className="category-navigation">
        {questionsData.categories.map((cat, idx) => (
          <button
            key={cat.id}
            className={`category-tab ${idx === currentCategoryIndex ? 'active' : ''} ${
              cat.questions.every(q => responses[q.id] !== undefined) ? 'complete' : ''
            }`}
            onClick={() => setCurrentCategoryIndex(idx)}
          >
            {cat.name[i18n.language]}
          </button>
        ))}
      </div>

      <div className="questions-section">
        <h3 className="category-title">{currentCategory.name[i18n.language]}</h3>

        {currentCategory.questions.map((question, idx) => (
          <div key={question.id} className="question-card">
            <div className="question-header">
              <span className="question-number">Q{idx + 1}</span>
              <div className="question-text">
                {question.text[i18n.language]}
              </div>
            </div>

            <div className="question-standards">
              {question.standard.map((std, i) => (
                <span key={i} className="standard-tag">{std}</span>
              ))}
            </div>

            <div className="options-list">
              {question.options.map((option) => (
                <label
                  key={option.value}
                  className={`option-item ${
                    responses[question.id] === option.value ? 'selected' : ''
                  }`}
                >
                  <input
                    type="radio"
                    name={question.id}
                    value={option.value}
                    checked={responses[question.id] === option.value}
                    onChange={() => handleResponseChange(question.id, option.value)}
                  />
                  <span className="option-label">{option.label[i18n.language]}</span>
                </label>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="questionnaire-actions">
        <button
          className="btn btn-secondary"
          onClick={handlePrevious}
          disabled={currentCategoryIndex === 0}
        >
          {t('questionnaire.previous')}
        </button>

        {!isLastCategory ? (
          <button
            className="btn btn-primary"
            onClick={handleNext}
            disabled={!isCurrentCategoryComplete()}
          >
            {t('questionnaire.next')}
          </button>
        ) : (
          <button
            className="btn btn-primary"
            onClick={handleSubmit}
            disabled={progress < 100}
          >
            {t('questionnaire.submit')}
          </button>
        )}
      </div>
    </div>
  );
}

export default Questionnaire;
