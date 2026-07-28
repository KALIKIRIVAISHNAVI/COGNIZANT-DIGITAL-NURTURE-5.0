import { createContext, useState } from 'react';

// 1. Create the Context (the actual "cloud" storage)
export const EnrollmentContext = createContext();

// 2. Create the Provider (the component that wraps around your app to give it access)
export function EnrollmentProvider({ children }) {
  const [enrolledCourses, setEnrolledCourses] = useState([]);

  // Function to add a course
  const enrollCourse = (courseId) => {
    if (!enrolledCourses.includes(courseId)) {
      setEnrolledCourses([...enrolledCourses, courseId]);
    }
  };

  // Function to remove a course (Step 84 requirement)
  const unenrollCourse = (courseIdToRemove) => {
    setEnrolledCourses(enrolledCourses.filter(id => id !== courseIdToRemove));
  };

  // 3. Provide the state and functions to whoever asks for them
  return (
    <EnrollmentContext.Provider value={{ enrolledCourses, enrollCourse, unenrollCourse }}>
      {children}
    </EnrollmentContext.Provider>
  );
}