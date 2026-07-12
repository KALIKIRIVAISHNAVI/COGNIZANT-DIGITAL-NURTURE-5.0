import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root' // This makes it a singleton available everywhere
})
export class CourseService {
  
  // Inject HttpClient via the constructor
  constructor(private http: HttpClient) { }

  // Method to fetch data, returning an Observable
  getCourses(): Observable<any[]> {
    return this.http.get<any[]>('https://jsonplaceholder.typicode.com/posts?_limit=5');
  }
}