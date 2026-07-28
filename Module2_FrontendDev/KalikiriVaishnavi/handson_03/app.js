// Import the data from our data file
import { coursesData } from './data.js';

// --- TASK 1: ES6+ Syntax Practice (Check your browser console!) ---
// 1. Array.map() - Format strings
const formattedCourses = coursesData.map(course => `${course.code} ${course.name} (${course.credits} credits)`);
console.log("Formatted Courses:", formattedCourses);

// 2. Array.filter() - Get heavy courses
const heavyCourses = coursesData.filter(course => course.credits >= 4);
console.log("Number of courses with 4+ credits:", heavyCourses.length);

// --- TASK 2 & 3: DOM Selection & Interactivity ---
const courseGrid = document.querySelector('.course-grid');
const searchInput = document.getElementById('search-courses');
const sortButton = document.getElementById('sort-credits');
const totalCreditsText = document.getElementById('total-credits');
const courseCountText = document.getElementById('course-count');

// Function to render the courses to the screen
const renderCourses = (coursesToRender) => {
    // Clear the grid first so we don't duplicate cards
    courseGrid.innerHTML = '';
    
    // Calculate total credits using Array.reduce()
    const totalCredits = coursesToRender.reduce((sum, course) => sum + course.credits, 0);

    // Loop through the data and create an article for each
    coursesToRender.forEach(course => {
        // Destructuring the course object
        const { name, code, credits, grade } = course;

        const article = document.createElement('article');
        article.className = 'course-card';
        // Using Template Literals for dynamic HTML
        article.innerHTML = `
            <h3>${name}</h3>
            <p>Course Code: ${code}</p>
            <span>Credits: ${credits}</span>
        `;
        // Append the new card to the grid
        courseGrid.appendChild(article);
    });

    // Update the UI text
    totalCreditsText.textContent = `Total Credits Enrolled: ${totalCredits}`;
    courseCountText.textContent = coursesToRender.length;
};

// Initial render when the page first loads
renderCourses(coursesData);

// --- Event Listeners ---

// Search functionality
searchInput.addEventListener('input', (event) => {
    const searchTerm = event.target.value.toLowerCase();
    const filteredCourses = coursesData.filter(course => 
        course.name.toLowerCase().includes(searchTerm)
    );
    renderCourses(filteredCourses);
});

// Sort functionality
sortButton.addEventListener('click', () => {
    // Create a copy of the array and sort it descending by credits
    const sortedCourses = [...coursesData].sort((a, b) => b.credits - a.credits);
    renderCourses(sortedCourses);
});

// Event Delegation: Listen for clicks on the whole grid, but only react to cards
courseGrid.addEventListener('click', (event) => {
    const clickedCard = event.target.closest('.course-card');
    if (clickedCard) {
        // Find the course name inside the clicked card to show in the alert
        const courseName = clickedCard.querySelector('h3').textContent;
        alert(`You selected: ${courseName}\nCheck the console for more details!`);
    }
});