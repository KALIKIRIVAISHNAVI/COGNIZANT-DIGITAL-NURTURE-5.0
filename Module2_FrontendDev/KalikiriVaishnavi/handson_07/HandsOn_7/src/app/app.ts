import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; // Required for router-outlet and routerLink

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterModule], // Import RouterModule here!
  template: `
    <div style="font-family: Arial, sans-serif; background-color: #f4f7f6; min-height: 100vh;">
      
      <nav style="background-color: #2c3e50; padding: 20px; text-align: center;">
        <a routerLink="/" style="color: white; margin-right: 20px; text-decoration: none; font-weight: bold;">Home/Courses</a>
        <a routerLink="/profile" style="color: white; text-decoration: none; font-weight: bold;">Student Profile</a>
      </nav>

      <main>
        <router-outlet></router-outlet>
      </main>

    </div>
  `
})
export class AppComponent {}