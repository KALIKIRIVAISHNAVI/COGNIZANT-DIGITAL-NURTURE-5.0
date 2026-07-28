import { Link } from 'react-router-dom';
import { useContext } from 'react'; // Import useContext
import { EnrollmentContext } from '../EnrollmentContext'; // Import our specific context

function Header({ siteName }) {
  // Grab the array directly from Context!
  const { enrolledCourses } = useContext(EnrollmentContext);

  return (
    <header style={{ backgroundColor: '#2c3e50', color: 'white', padding: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
      <h2>{siteName}</h2>
      <nav>
        <ul style={{ display: 'flex', gap: '15px', listStyle: 'none', padding: 0, margin: 0, alignItems: 'center' }}>
          <li><Link to="/" style={{ color: 'white', textDecoration: 'none', fontWeight: '500' }}>Home</Link></li>
          <li><Link to="/courses" style={{ color: 'white', textDecoration: 'none', fontWeight: '500' }}>Courses</Link></li>
          <li><Link to="/profile" style={{ color: 'white', textDecoration: 'none', fontWeight: '500' }}>Profile</Link></li>
          
          <li style={{ backgroundColor: '#1abc9c', padding: '5px 10px', borderRadius: '5px', fontWeight: 'bold', marginLeft: '10px' }}>
            {/* Display the length of the array! */}
            Enrolled: {enrolledCourses.length}
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;