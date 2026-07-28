import { useParams, useNavigate } from 'react-router-dom';
import { useContext } from 'react';
import { EnrollmentContext } from '../EnrollmentContext';

function CourseDetailPage() {
  const { courseId } = useParams(); 
  const navigate = useNavigate();
  // Pull the enroll function from Context
  const { enrollCourse } = useContext(EnrollmentContext); 

  const handleEnrollClick = () => {
    enrollCourse(courseId); // Actually save it!
    navigate('/profile'); 
  };

  return (
    <div style={{ padding: '40px', backgroundColor: 'white', borderRadius: '8px', textAlign: 'center', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }}>
      <h2 style={{ color: '#2c3e50' }}>Course Details</h2>
      <p style={{ fontSize: '18px', margin: '20px 0' }}>
        You are viewing the details for Course ID: <strong style={{ color: '#2563eb', fontSize: '24px' }}>{courseId}</strong>
      </p>
      
      <button 
        onClick={handleEnrollClick}
        style={{ padding: '12px 24px', backgroundColor: '#1abc9c', color: 'white', border: 'none', borderRadius: '5px', fontSize: '16px', cursor: 'pointer', fontWeight: 'bold' }}>
        Enroll in Course
      </button>
    </div>
  );
}

export default CourseDetailPage;