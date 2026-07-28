import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useEnrollmentStore = defineStore('enrollment', () => {
  // State: The array holding the enrolled courses
  const enrolledCourses = ref([])

  // Computed: Automatically calculates the total credits
  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce((total, course) => total + course.credits, 0)
  })

  // Action: Adds a course if it isn't already in the list
  const enroll = (course) => {
    if (!enrolledCourses.value.find(c => c.id === course.id)) {
      enrolledCourses.value.push(course)
    }
  }

  // Action: Removes a course by its ID
  const unenroll = (courseId) => {
    enrolledCourses.value = enrolledCourses.value.filter(c => c.id !== courseId)
  }

  // Expose everything to the app
  return { enrolledCourses, totalCredits, enroll, unenroll }
})