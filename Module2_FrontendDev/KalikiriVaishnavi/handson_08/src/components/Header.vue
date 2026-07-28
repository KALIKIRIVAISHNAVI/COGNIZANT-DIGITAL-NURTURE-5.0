<script setup>
import { RouterLink } from 'vue-router'
import { useEnrollmentStore } from '../stores/enrollment'

// Access the Pinia store
const store = useEnrollmentStore()
</script>

<template>
  <header style="background-color: #2c3e50; padding: 20px; display: flex; justify-content: space-between; align-items: center;">
    <h2 style="color: white; margin: 0;">Vue Portal</h2>
    <nav style="display: flex; gap: 20px; align-items: center;">
      <RouterLink to="/" style="color: white; text-decoration: none; font-weight: bold;">Home</RouterLink>
      <RouterLink to="/courses" style="color: white; text-decoration: none; font-weight: bold;">Courses</RouterLink>
      <RouterLink to="/profile" style="color: white; text-decoration: none; font-weight: bold;">
        Profile 
        <!-- Dynamic Count Badge -->
        <span v-if="store.enrolledCourses.length > 0" style="background-color: #1abc9c; color: white; padding: 2px 8px; border-radius: 12px; font-size: 12px; margin-left: 5px;">
          {{ store.enrolledCourses.length }}
        </span>
      </RouterLink>
    </nav>
  </header>
</template>

<style scoped>
.router-link-active {
  color: #1abc9c !important; 
}
</style>