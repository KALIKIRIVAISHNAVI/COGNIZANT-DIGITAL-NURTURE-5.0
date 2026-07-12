import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

apiClient.interceptors.request.use(
  (config) => {
    config.headers.Authorization = 'Bearer mock-token-123';
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

apiClient.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    const customError = new Error(error.response?.data?.message || 'API Error Occurred');
    customError.statusCode = error.response?.status || 500;
    return Promise.reject(customError);
  }
);

export default apiClient;