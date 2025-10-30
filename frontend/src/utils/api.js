import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getQuestions = async (lang = 'fr') => {
  const response = await api.get(`/questions?lang=${lang}`);
  return response.data;
};

export const submitQuestionnaire = async (data) => {
  const response = await api.post('/submit', data);
  return response.data;
};

export const downloadTemplate = async (lang = 'fr', appName = null) => {
  const params = new URLSearchParams({ lang });
  if (appName) params.append('app_name', appName);

  const response = await api.get(`/export/template?${params.toString()}`, {
    responseType: 'blob',
  });

  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', `security_questionnaire_${lang}_${Date.now()}.xlsx`);
  document.body.appendChild(link);
  link.click();
  link.remove();
};

export const downloadResults = async (data, lang = 'fr') => {
  const response = await api.post('/export/results', data, {
    responseType: 'blob',
  });

  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement('a');
  link.href = url;
  const appName = data.app_info?.name || 'application';
  link.setAttribute('download', `security_assessment_${appName}_${Date.now()}.xlsx`);
  document.body.appendChild(link);
  link.click();
  link.remove();
};

export const getStats = async () => {
  const response = await api.get('/stats');
  return response.data;
};

export default api;
