import { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';

// Components
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';
import CourseDetailPage from './components/CourseDetailPage'; // Import the new page!

function Home() {
  return (
    <div style={{ textAlign: 'center', padding: '40px', backgroundColor: 'white', borderRadius: '8px' }}>
      <h1 style={{ color: '#2c3e50' }}>Welcome to your Digital Campus</h1>
      <p style={{ color: '#64748b', marginTop: '10px' }}>Use the navigation bar above to view courses or update your profile.</p>
    </div>
  );
}

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts?_limit=5');
        const data = await response.json();
        const mappedCourses = data.map((post, index) => ({
          id: post.id, // IMPORTANT: We need the ID for our dynamic links!
          name: post.title.substring(0, 20),
          code: `CS10${index + 1}`,
          credits: Math.floor(Math.random() * 2) + 3,
          grade: "N/A"
        }));
        setCourses(mappedCourses);
        setLoading(false);
      } catch (err) {
        console.error(err);
        setLoading(false);
      }
    };
    fetchCourses();
  }, []);

  const filteredCourses = courses.filter(course => 
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', backgroundColor: '#f4f7f6', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>
      
      <Header siteName="React Student Portal" />
      
      <main style={{ padding: '40px', flex: 1, maxWidth: '1200px', margin: '0 auto', width: '100%' }}>
        
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/profile" element={<StudentProfile />} />
          
          <Route path="/courses" element={
            <>
              <h2 style={{ color: '#2c3e50', marginBottom: '20px' }}>Available Courses</h2>
              <input 
                type="text" 
                placeholder="Search courses..." 
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                style={{ width: '100%', padding: '10px', marginBottom: '20px', borderRadius: '5px', border: '1px solid #ccc' }}
              />
              {loading ? <p>Loading courses...</p> : (
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '20px' }}>
                  {filteredCourses.map(course => (
                    <CourseCard 
                      key={course.id} 
                      id={course.id} // Pass the ID down to the card
                      name={course.name} 
                      code={course.code} 
                      credits={course.credits} 
                      grade={course.grade}
                    />
                  ))}
                </div>
              )}
            </>
          } />

          {/* NEW ROUTE: The dynamic course detail page! */}
          <Route path="/courses/:courseId" element={<CourseDetailPage />} />

        </Routes>
        
      </main>
      <Footer />
    </div>
  );
}

export default App;