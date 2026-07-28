import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormGroup, FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-student-profile',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule], // Import ReactiveFormsModule!
  template: `
    <div style="padding: 40px; max-width: 600px; margin: 40px auto; background: white; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
      <h2 style="color: #2c3e50; margin-bottom: 20px;">Student Profile Form</h2>
      
      <form [formGroup]="profileForm" (ngSubmit)="onSubmit()">
        
        <div style="margin-bottom: 15px;">
          <label style="display: block; margin-bottom: 5px; color: #64748b;">Full Name:</label>
          <input type="text" formControlName="name" style="width: 100%; padding: 10px; border-radius: 4px; border: 1px solid #ccc;">
          <div *ngIf="profileForm.get('name')?.touched && profileForm.get('name')?.invalid" style="color: #e74c3c; font-size: 12px; margin-top: 5px;">
            Name is required.
          </div>
        </div>

        <div style="margin-bottom: 15px;">
          <label style="display: block; margin-bottom: 5px; color: #64748b;">Email Address:</label>
          <input type="email" formControlName="email" style="width: 100%; padding: 10px; border-radius: 4px; border: 1px solid #ccc;">
          <div *ngIf="profileForm.get('email')?.touched && profileForm.get('email')?.invalid" style="color: #e74c3c; font-size: 12px; margin-top: 5px;">
            Enter a valid email.
          </div>
        </div>

        <div style="margin-bottom: 25px;">
          <label style="display: block; margin-bottom: 5px; color: #64748b;">Current Semester (1-8):</label>
          <input type="number" formControlName="semester" style="width: 100%; padding: 10px; border-radius: 4px; border: 1px solid #ccc;">
          <div *ngIf="profileForm.get('semester')?.touched && profileForm.get('semester')?.invalid" style="color: #e74c3c; font-size: 12px; margin-top: 5px;">
            Semester is required and must be between 1 and 8.
          </div>
        </div>

        <button type="submit" [disabled]="profileForm.invalid" 
                style="width: 100%; padding: 12px; border: none; border-radius: 4px; font-weight: bold; cursor: pointer;"
                [style.backgroundColor]="profileForm.valid ? '#1abc9c' : '#ccc'"
                [style.color]="profileForm.valid ? 'white' : '#666'">
          Update Profile
        </button>
      </form>
    </div>
  `
})
export class StudentProfileComponent {
  
  // Step 103: Build the FormGroup and validations
  profileForm = new FormGroup({
    name: new FormControl('', Validators.required),
    email: new FormControl('', [Validators.required, Validators.email]),
    semester: new FormControl('', [Validators.required, Validators.min(1), Validators.max(8)])
  });

  // Step 106: Log on submit
  onSubmit() {
    if (this.profileForm.valid) {
      console.log('Form Submitted Successfully!', this.profileForm.value);
      alert('Profile Updated! Check the browser console.');
      this.profileForm.reset(); // Clear the form after successful submission
    }
  }
}