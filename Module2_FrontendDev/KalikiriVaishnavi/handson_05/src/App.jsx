import { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5');
        if (!response.ok) throw new Error('Network error');
        const data = await response.json();

        const mappedCourses = data.map((post, index) => ({
          id: post.id,
          name: post.title.substring(0, 20),
          code: `CS10${index + 1}`,
          credits: Math.floor(Math.random() * 2) + 3,
          grade: "N/A"
        }));

        setCourses(mappedCourses);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  useEffect(() => {
    console.log('Courses updated');
  }, [courses]);

  const filteredCourses = courses.filter(course => 
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const handleEnroll = (courseName) => {
    if (!enrolledCourses.includes(courseName)) {
      setEnrolledCourses([...enrolledCourses, courseName]);
    }
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', backgroundColor: '#f4f7f6', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      <Header siteName="React Student Portal" enrolledCount={enrolledCourses.length} />

      <main style={{ padding: '40px', flex: 1 }}>
        <StudentProfile />
        <h2 style={{ color: '#2c3e50', marginBottom: '20px' }}>Available Courses</h2>

        <input 
          type="text" 
          placeholder="Search courses..." 
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          style={{ width: '100%', padding: '10px', marginBottom: '20px', borderRadius: '5px', border: '1px solid #ccc' }}
        />

        {loading && <p style={{ color: '#1abc9c', fontWeight: 'bold' }}>Loading courses...</p>}
        {error && <p style={{ color: 'red', fontWeight: 'bold' }}>Error: {error}</p>}

        {!loading && !error && (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '20px' }}>
            {filteredCourses.map(course => (
              <CourseCard 
                key={course.id} 
                name={course.name} 
                code={course.code} 
                credits={course.credits} 
                grade={course.grade}
                onEnroll={() => handleEnroll(course.name)}
              />
            ))}
          </div>
        )}
      </main>
      <Footer />
    </div>
  );
}

export default App;