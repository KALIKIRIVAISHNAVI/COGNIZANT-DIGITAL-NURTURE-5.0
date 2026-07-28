import { useState } from 'react';

function StudentProfile() {
  const [profile, setProfile] = useState({ name: '', email: '', semester: '' });

  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  return (
    <div style={{ backgroundColor: 'white', padding: '20px', borderRadius: '8px', marginBottom: '20px' }}>
      <h2>Student Profile</h2>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', marginTop: '10px' }}>
        <input name="name" placeholder="Name" value={profile.name} onChange={handleChange} style={{ padding: '8px' }} />
        <input name="email" placeholder="Email" value={profile.email} onChange={handleChange} style={{ padding: '8px' }} />
        <input name="semester" placeholder="Semester" value={profile.semester} onChange={handleChange} style={{ padding: '8px' }} />
      </div>
    </div>
  );
}

export default StudentProfile;