import { Routes } from '@angular/router';
import { CourseListComponent } from './course-list/course-list'; // Adjust path if needed
import { StudentProfileComponent } from './student-profile/student-profile'; // Adjust path if needed

export const routes: Routes = [
  { path: '', component: CourseListComponent }, // Default route
  { path: 'profile', component: StudentProfileComponent } // Profile route
];