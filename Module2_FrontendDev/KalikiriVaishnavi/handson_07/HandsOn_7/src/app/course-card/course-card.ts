import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-course-card',
  standalone: true,
  template: `
    <div style="border: 1px solid #e2e8f0; padding: 20px; border-radius: 8px; background-color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
      <h3 style="color: #2c3e50; margin-bottom: 10px;">{{ name }}</h3>
      <p style="color: #64748b; font-size: 14px; margin-bottom: 5px;">Code: {{ code }}</p>
      <p style="font-weight: bold; color: #2563eb; font-size: 14px;">Credits: {{ credits }}</p>
      <p style="font-size: 14px; color: #1abc9c; margin-top: 5px;">Grade: {{ grade }}</p>
    </div>
  `
})
export class CourseCardComponent {
  // @Input() allows data to flow into this component
  @Input() name: string = '';
  @Input() code: string = '';
  @Input() credits: number = 0;
  @Input() grade: string = 'N/A';
}