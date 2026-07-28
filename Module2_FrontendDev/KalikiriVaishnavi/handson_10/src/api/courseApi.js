import apiClient from './apiClient.js';

export const getAllCourses = () => {
  return apiClient.get('/courses');
};

export const getCourseById = (id) => {
  return apiClient.get(`/courses/${id}`);
};

export const enrollStudent = (studentId, courseId) => {
  return apiClient.post('/enrollments', {
    studentId,
    courseId
  });
};