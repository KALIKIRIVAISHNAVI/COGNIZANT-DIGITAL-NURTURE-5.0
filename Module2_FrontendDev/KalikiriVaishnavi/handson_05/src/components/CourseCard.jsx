function CourseCard({ name, code, credits, grade, onEnroll }) {
  return (
    <div style={{ border: '1px solid #e2e8f0', padding: '20px', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.05)', backgroundColor: 'white', display: 'flex', flexDirection: 'column' }}>
      <h3 style={{ color: '#2c3e50', marginBottom: '10px' }}>{name}</h3>
      <p style={{ color: '#64748b', fontSize: '14px', marginBottom: '5px' }}>Code: {code}</p>
      <p style={{ fontWeight: 'bold', color: '#2563eb', fontSize: '14px' }}>Credits: {credits}</p>
      <p style={{ fontSize: '14px', color: '#1abc9c', marginTop: '5px', marginBottom: '15px' }}>Grade: {grade}</p>
      <button 
        onClick={onEnroll} 
        style={{ marginTop: 'auto', padding: '10px', backgroundColor: '#2c3e50', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
        Enroll
      </button>
    </div>
  );
}

export default CourseCard;