import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCardComponent } from '../course-card/course-card';
import { CourseService } from '../course'; // Updated to match your generated file name!

@Component({
  selector: 'app-course-list',
  standalone: true,
  imports: [CommonModule, FormsModule, CourseCardComponent],
  template: `
    <div style="padding: 40px; max-width: 1200px; margin: 0 auto;">
      <h2 style="color: #2c3e50; margin-bottom: 20px;">Available Courses</h2>
      
      <input 
        type="text" 
        [(ngModel)]="searchTerm" 
        placeholder="Search courses..." 
        style="width: 100%; padding: 10px; margin-bottom: 20px; border-radius: 5px; border: 1px solid #ccc;"
      />

      <div *ngIf="loading" style="text-align: center; font-size: 18px; color: #2563eb; margin: 20px 0;">
        Loading courses from API... ⏳
      </div>

      <div *ngIf="!loading">
        <div *ngIf="filteredCourses().length === 0" style="color: #e74c3c; font-weight: bold;">
          No courses found
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
          <app-course-card
            *ngFor="let course of filteredCourses()"
            [name]="course.name"
            [code]="course.code"
            [credits]="course.credits"
            [grade]="course.grade">
          </app-course-card>
        </div>
      </div>
    </div>
  `
})
export class CourseListComponent implements OnInit {
  searchTerm: string = '';
  courses: any[] = [];
  loading: boolean = true; 

  constructor(private courseService: CourseService) {}

  ngOnInit() {
    this.loading = true;
    this.courseService.getCourses().subscribe({
      next: (data) => {
        this.courses = data.map((post: any, index: number) => ({
          name: post.title.substring(0, 20),
          code: `CS10${index + 1}`,
          credits: Math.floor(Math.random() * 2) + 3,
          grade: 'N/A'
        }));
        this.loading = false;
      },
      error: (err) => {
        console.error('Error fetching courses:', err);
        this.loading = false;
      }
    });
  }

  filteredCourses() {
    return this.courses.filter(course =>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }
}