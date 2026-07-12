<script setup>
import { useRoute, useRouter } from 'vue-router'

// Step 114: Access the current route object to get parameters
const route = useRoute()

// Step 115: Access the router instance for programmatic navigation
const router = useRouter()

const handleEnroll = () => {
  // Push the user to the profile page when they click enroll
  router.push('/profile')
}
</script>

<template>
  <div style="padding: 40px; text-align: center;">
    <h2 style="color: #2c3e50;">Course Details</h2>
    
    <p style="font-size: 20px; margin: 20px 0;">
      You are viewing details for Course ID: <strong style="color: #2563eb;">{{ route.params.id }}</strong>
    </p>
    
    <button @click="handleEnroll" style="padding: 12px 24px; background-color: #1abc9c; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; font-size: 16px;">
      Simulate Enroll & Redirect
    </button>
  </div>
</template>