function Header({ siteName, enrolledCount }) {
  return (
    <header style={{ backgroundColor: '#2c3e50', color: 'white', padding: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
      <h2>{siteName}</h2>
      <nav>
        <ul style={{ display: 'flex', gap: '15px', listStyle: 'none', padding: 0, margin: 0, alignItems: 'center' }}>
          <li style={{ cursor: 'pointer' }}>Home</li>
          <li style={{ cursor: 'pointer' }}>Courses</li>
          <li style={{ cursor: 'pointer' }}>Profile</li>
          <li style={{ backgroundColor: '#1abc9c', padding: '5px 10px', borderRadius: '5px', fontWeight: 'bold' }}>
            Enrolled: {enrolledCount}
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;