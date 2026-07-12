<script setup>
import { useEnrollmentStore } from '../stores/enrollment'

const store = useEnrollmentStore()
</script>

<template>
  <div style="padding: 40px; max-width: 800px; margin: 0 auto;">
    <h2 style="color: #2c3e50;">Student Profile</h2>

    <div style="background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-top: 20px;">
      <h3 style="margin-top: 0; color: #2c3e50;">Your Enrolled Courses</h3>

      <p v-if="store.enrolledCourses.length === 0" style="color: #64748b; font-style: italic;">
        You have not enrolled in any courses yet. Head over to the Courses tab!
      </p>

      <ul v-else style="list-style: none; padding: 0;">
        <li v-for="course in store.enrolledCourses" :key="course.id" style="padding: 15px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center;">
          <div>
            <strong style="color: #2c3e50; font-size: 16px;">{{ course.name }}</strong> 
            <span style="color: #64748b; font-size: 14px; margin-left: 10px;">({{ course.code }}) - {{ course.credits }} Credits</span>
          </div>
          <button @click="store.unenroll(course.id)" style="background: #e74c3c; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; font-weight: bold;">
            Remove
          </button>
        </li>
      </ul>

      <div style="margin-top: 30px; text-align: right; font-size: 20px; border-top: 2px solid #f1f5f9; padding-top: 20px;">
        <strong>Total Credits: <span style="color: #2563eb;">{{ store.totalCredits }}</span></strong>
      </div>
    </div>
  </div>
</template>