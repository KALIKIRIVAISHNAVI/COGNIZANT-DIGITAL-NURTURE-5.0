import { coursesData } from './data.js';

// DOM Elements
const courseGrid = document.querySelector('.course-grid');
const courseLoading = document.getElementById('course-loading');
const notificationList = document.getElementById('notification-list');
const loadingSpinner = document.getElementById('loading-spinner');
const errorMessage = document.getElementById('error-message');
const retryBtn = document.getElementById('retry-btn');

// Helper to render courses
const renderCourses = (coursesToRender) => {
    courseGrid.innerHTML = '';
    coursesToRender.forEach(course => {
        const article = document.createElement('article');
        article.className = 'course-card';
        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Course Code: ${course.code}</p>
            <span>Credits: ${course.credits}</span>
        `;
        courseGrid.appendChild(article);
    });
};

// ==========================================
// TASK 1: Promises and async/await
// ==========================================

// Step 45: Promise chaining
const fetchUser = (id) => {
    fetch('https://jsonplaceholder.typicode.com/users/' + id)
        .then(response => response.json())
        .then(user => console.log(`Step 45 (Promise Chaining) User: ${user.name}`));
};
fetchUser(1);

// Step 46: Rewrite using async/await
const fetchUserAsync = async (id) => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/users/' + id);
        const user = await response.json();
        console.log(`Step 46 (Async/Await) User: ${user.name}`);
    } catch (error) {
        console.error("Error:", error);
    }
};
fetchUserAsync(2);

// Step 47 & 48: Simulated delay for courses
const fetchAllCourses = () => {
    return new Promise(resolve => {
        setTimeout(() => resolve(coursesData), 1000);
    });
};

const loadCourses = async () => {
    courseLoading.style.display = 'block'; // Show "Loading courses..."
    const data = await fetchAllCourses();
    courseLoading.style.display = 'none'; // Hide message
    renderCourses(data);
};
loadCourses();

// Step 49: Promise.all()
const p1 = fetch('https://jsonplaceholder.typicode.com/users/3').then(res => res.json());
const p2 = fetch('https://jsonplaceholder.typicode.com/users/4').then(res => res.json());

Promise.all([p1, p2]).then(users => {
    console.log(`Step 49 (Promise.all): Both loaded - ${users[0].name} & ${users[1].name}`);
});


// ==========================================
// TASK 2: Fetch API with Error Handling
// ==========================================

// Step 50: Reusable apiFetch using native fetch
const apiFetchNative = async (url) => {
    const response = await fetch(url);
    if (!response.ok) { // Crucial step: checking response.ok
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
};


// ==========================================
// TASK 3: Introduction to Axios
// ==========================================

// Step 59: Compare fetch and axios (Side-by-side comment)
/*
  --- FETCH vs AXIOS DIFFERENCES ---
  1. Fetch requires manual JSON parsing (res.json()) and manual error checking (res.ok). Axios automatically parses JSON and throws errors for non-2xx responses.
  2. Fetch is built into modern browsers natively. Axios is an external library we had to import via CDN.
  3. Axios has convenient built-in features like request timeouts (timeout: 5000), while fetch requires setting up complex AbortControllers for timeouts.
*/

// Step 58: Request Interceptor
axios.interceptors.request.use(config => {
    console.log(`Step 58: API call started to -> ${config.url}`);
    return config;
});

// Step 56 & 57: Rewrite apiFetch using Axios and add params
const apiFetchAxios = async (url) => {
    const response = await axios.get(url, { params: { userId: 1 } });
    return response.data; 
};

// Step 51 - 54: The UI fetching logic (Using our new Axios function)
const loadNotifications = async (url) => {
    loadingSpinner.style.display = 'block';
    errorMessage.style.display = 'none';
    retryBtn.style.display = 'none';
    notificationList.innerHTML = '';
    
    try {
        const posts = await apiFetchAxios(url); // Calling the Axios version
        loadingSpinner.style.display = 'none';
        
        posts.slice(0, 3).forEach(post => {
            const li = document.createElement('li');
            li.style.padding = '10px';
            li.style.borderBottom = '1px solid #eee';
            li.innerHTML = `<strong>${post.title}</strong><br><small>${post.body}</small>`;
            notificationList.appendChild(li);
        });
    } catch (error) {
        loadingSpinner.style.display = 'none';
        errorMessage.style.display = 'block';
        errorMessage.textContent = `Oops! Failed to load notifications. Error: ${error.message}`;
        retryBtn.style.display = 'block';
    }
};

// Initial API Call
loadNotifications('https://jsonplaceholder.typicode.com/posts');

// Step 54: Retry button listener
retryBtn.addEventListener('click', () => {
    loadNotifications('https://jsonplaceholder.typicode.com/posts');
});

// Step 53: Simulate a 404 bad URL
window.testBadUrl = () => {
    loadNotifications('https://jsonplaceholder.typicode.com/nonexistent');
};