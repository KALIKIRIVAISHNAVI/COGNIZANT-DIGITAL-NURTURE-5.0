import { useState, useContext } from 'react';
import { EnrollmentContext } from '../EnrollmentContext';

function StudentProfile() {
  const [profile, setProfile] = useState({ name: '', email: '', semester: '' });
  // Pull both the array and the remove function
  const { enrolledCourses, unenrollCourse } = useContext(EnrollmentContext);

  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  return (
    <div style={{ backgroundColor: 'white', padding: '40px', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)' }}>
      <h2 style={{ color: '#2c3e50', marginBottom: '20px' }}>Student Profile</h2>
      
      {/* ... keep the inputs the same as before ... */}
      
      <h3 style={{ color: '#2c3e50', marginTop: '30px', marginBottom: '15px' }}>Your Enrolled Courses</h3>
      {enrolledCourses.length === 0 ? (
        <p style={{ color: '#64748b' }}>You are not enrolled in any courses yet.</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {enrolledCourses.map(id => (
            <li key={id} style={{ display: 'flex', justifyContent: 'space-between', padding: '10px', borderBottom: '1px solid #eee' }}>
              <span>Course ID: {id}</span>
              <button 
                onClick={() => unenrollCourse(id)}
                style={{ backgroundColor: '#e74c3c', color: 'white', border: 'none', padding: '5px 10px', borderRadius: '4px', cursor: 'pointer' }}>
                Remove
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default StudentProfile;