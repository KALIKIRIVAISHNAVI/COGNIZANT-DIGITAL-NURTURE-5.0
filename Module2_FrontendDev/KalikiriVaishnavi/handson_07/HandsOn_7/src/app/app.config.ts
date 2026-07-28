import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http'; // 1. Import this!

export const appConfig: ApplicationConfig = {
  // 2. Add provideHttpClient() to your providers array
  providers: [provideRouter(routes), provideHttpClient()] 
};