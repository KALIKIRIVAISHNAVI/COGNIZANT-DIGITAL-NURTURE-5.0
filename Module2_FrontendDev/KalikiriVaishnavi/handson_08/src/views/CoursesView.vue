<script setup>
import { ref, computed, onMounted } from 'vue';
import CourseCard from '../components/CourseCard.vue';
import { useEnrollmentStore } from '../stores/enrollment'; // Import store

const store = useEnrollmentStore(); // Initialize store

const courses = ref([]);
const searchTerm = ref('');

onMounted(() => {
  courses.value = [
    { id: 1, name: 'Vue Fundamentals', code: 'CS101', credits: 3, grade: 'A' },
    { id: 2, name: 'Composition API', code: 'CS102', credits: 4, grade: 'B+' },
    { id: 3, name: 'Vue Router Navigation', code: 'CS103', credits: 3, grade: 'A-' },
    { id: 4, name: 'State Management with Pinia', code: 'CS104', credits: 4, grade: 'A' },
    { id: 5, name: 'Advanced Vue Patterns', code: 'CS105', credits: 3, grade: 'B' }
  ];
});

const filteredCourses = computed(() => {
  return courses.value.filter(course =>
    course.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});
</script>

<template>
  <div style="padding: 40px; max-width: 1200px; margin: 0 auto;">
    <h2 style="color: #2c3e50; margin-bottom: 20px;">Available Courses</h2>
    <input type="text" v-model="searchTerm" placeholder="Search courses..." style="width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: 1px solid #ccc;"/>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
      <!-- Listen for @enroll and trigger store.enroll() -->
      <CourseCard 
        v-for="course in filteredCourses" 
        :key="course.id"
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
        @enroll="store.enroll(course)" 
      />
    </div>
  </div>
</template>