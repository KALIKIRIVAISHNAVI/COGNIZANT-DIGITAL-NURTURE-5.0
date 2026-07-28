import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CoursesView from '../views/CoursesView.vue'
import CourseDetailView from '../views/CourseDetailView.vue'
import ProfileView from '../views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: HomeView },
    { path: '/courses', component: CoursesView },
    { path: '/courses/:id', component: CourseDetailView },
    { path: '/profile', component: ProfileView }
  ]
})

// Step 116: The Navigation Guard!
router.beforeEach((to, from, next) => {
  console.log(`Navigating to: ${to.path}`)
  next() // You MUST call next() or the routing will freeze completely!
})

export default router