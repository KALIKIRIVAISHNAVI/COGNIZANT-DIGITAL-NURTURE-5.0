import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchAllCourses, selectCourses, selectCoursesLoading, selectCoursesError } from './store/courseSlice';

const CoursesPage = () => {
  const dispatch = useDispatch();
  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  throw new Error("Intentional crash to test the boundary!");

  if (loading) {
    return <p>Loading courses...</p>;
  }

  if (error) {
    return <p>Error loading courses: {error}</p>;
  }

  return (
    <div>
      <h2>Course List</h2>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>{course.name || course.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default CoursesPage;