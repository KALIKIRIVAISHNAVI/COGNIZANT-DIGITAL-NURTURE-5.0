# Digital Nurture 5.0 — Module 2: Frontend Development
### Python Full Stack Engineer Track — Hands-On Exercise Book (Output Log)

This README documents the completed work for all **10 Hands-On exercises** of Module 2 (Frontend Development), covering **HTML5, CSS3, JavaScript, React, Angular, and Vue.js**. It follows the single running project used throughout the book — the **Student Portal web application** — and includes the output screenshots captured for each exercise.

---

## 📁 Project Structure

```
Module2_FrontendDev/<YourName>/
├── handson_01/   (HTML/CSS)
├── handson_02/   (CSS)
├── handson_03/   (JavaScript)
├── handson_04/   (JavaScript)
├── handson_05/   (React)
├── handson_06/   (React)
├── handson_07/   (Angular)
├── handson_08/   (Vue.js)
├── handson_09/   (Accessibility)
└── handson_10/   (Advanced State Management)
```

## 🧰 Tools Used
VS Code · Node.js (LTS) + npm · Git · Chrome/Firefox DevTools · CodePen / CodeSandbox / StackBlitz · Vue SFC Playground · Angular on StackBlitz

## 📊 Difficulty Guide

| Level | Hands-On | Focus |
|---|---|---|
| Beginner | 1, 2, 3 | HTML5 structure, CSS3 layouts, Responsive design |
| Intermediate | 4, 5, 6 | Async JS, Fetch API, React components & hooks |
| Advanced | 7, 8, 9, 10 | Angular, Vue.js, Accessibility, State management |

## 🎓 Common Scenario: Student Portal

| Page / Section | Built In | Key Elements |
|---|---|---|
| Home / Landing | HO 1 & 2 | Header, nav bar, hero section, footer |
| Course Listing | HO 2 & 3 | Card grid layout, responsive columns |
| Student Profile | HO 3 & 4 | Form, DOM interaction, async data load |
| Notifications | HO 4 | Live API fetch, dynamic DOM rendering |
| React SPA | HO 5 & 6 | Components, hooks, routing, state |
| Angular App | HO 7 | Services, DI, reactive forms, routing |
| Vue.js App | HO 8 | Composition API, Vue Router, Pinia |
| Accessible Portal | HO 9 | ARIA, keyboard nav, WCAG checks |
| State Management | HO 10 | Redux / NgRx / Pinia patterns |

---

## Hands-On 1 — HTML5 Semantic Structure & CSS3 Foundations *(Beginner)*

**Topics:** HTML5 Semantic Elements · CSS3 Selectors & Specificity · CSS Box Model · Typography & Spacing · Basic Page Layout

Built the structural skeleton of the Student Portal (`<header>`, `<main>`, `<section id="hero">`, `<section id="courses">`, `<footer>`) with semantic HTML5, validated at the W3C validator, then styled it using a CSS reset, flex-based header/nav, hero styling, and `.course-card` styling with borders, radius, and shadows.

**Expected Outcome:** Zero W3C validation errors; a visually styled header, nav, hero with button, and bordered course cards.

**Output Screenshot:**

![Hands-On 1 Output](screenshots/handson01_semantic_html_css.png)

---

## Hands-On 2 — CSS Flexbox, Grid & Responsive Design *(Beginner)*

**Topics:** CSS Flexbox · CSS Grid · Mobile-First Design · Media Queries · Viewport Units & Fluid Layouts

Refactored the header/nav/hero with Flexbox, built a responsive `.course-grid` with CSS Grid (`repeat(3, 1fr)` → `repeat(auto-fit, minmax(280px, 1fr))`), and applied mobile-first media queries at `768px` and `1024px` breakpoints along with fluid typography using `clamp()`.

**Expected Outcome:** Layout verified correct at 375px (mobile, single column), 768px (tablet, 2-column), and 1280px (desktop, 3-column, full nav).

**Output Screenshot:** *(No separate screenshot captured for this hands-on — responsive behavior was verified live in DevTools' device toolbar across breakpoints.)*

---

## Hands-On 3 — JavaScript ES6+ & DOM Manipulation *(Beginner)*

**Topics:** `let` / `const` / `var` · Arrow Functions & Template Literals · Array Methods (`map`, `filter`, `reduce`) · DOM Selection & Modification · Event Listeners · ES6 Modules

Practiced ES6+ syntax (destructuring, template literals, `map`/`filter`/`reduce`) on a course data array, then dynamically rendered the course grid from JavaScript (replacing hardcoded HTML), and added a live search input, a "Sort by Credits" button, and click-based course selection using **event delegation**.

**Expected Outcome:** Console logs formatted course strings, filtered lists, and total credits; the course grid renders fully from JS data with working search, sort, and click interactions.

**Output Screenshot:**

![Hands-On 3 Output](screenshots/handson03_js_dom_render.png)

---

## Hands-On 4 — Async JavaScript, Fetch API & API Integration *(Intermediate)*

**Topics:** Promises & `async`/`await` · Fetch API · Error Handling (`try`/`catch`) · Loading States · Axios (introduction) · Dynamic DOM from API Data

Used the **JSONPlaceholder API** to fetch live data. Built `fetchUser()` with both Promise chaining and `async`/`await`, simulated network delay with a "Loading courses..." state, and demonstrated `Promise.all()` for concurrent requests. Built a reusable `apiFetch()` layer with proper `response.ok` checks, a loading spinner, a friendly 404 error message, and a **Retry** button. Finally compared Fetch with **Axios**, including interceptors and query params.

**Expected Outcome:** Loading indicator shows for ~1s before rendering; `Promise.all` logs both users together; a bad URL shows a friendly error + working Retry button; Axios interceptor logs every request.

**Output Screenshots:**

![Hands-On 4 — Promises & Async/Await (1)](screenshots/handson04_promises_asyncawait_1.png)
![Hands-On 4 — Promises & Async/Await (2)](screenshots/handson04_promises_asyncawait_2.png)
![Hands-On 4 — Loading State](screenshots/handson04_fetch_loading_state.png)
![Hands-On 4 — Fetch Error Handling & Retry](screenshots/handson04_fetch_error_handling.png)

---

## Hands-On 5 — React Fundamentals: Components, Props, State & Hooks *(Intermediate)*

**Topics:** JSX Syntax · Functional Components · Props & Prop Types · `useState` Hook · `useEffect` Hook · Conditional Rendering & Lists

Scaffolded the project with **Vite + React**, built `Header.jsx`, `Footer.jsx`, and `CourseCard.jsx` as reusable components. Used `useState` to manage a `courses` array, rendered dynamic lists with stable `key` props, added a live search filter, an "Enroll" button that lifts state up to `App.jsx`, and displayed the enrolled count in the Header. Replaced hardcoded data with a `useEffect`-driven fetch from JSONPlaceholder, added `loading`/`error` states, and built a `StudentProfile.jsx` with local form state.

**Expected Outcome:** Courses load from the API on mount with a brief loading message; search filters courses live; Enroll updates the header count; the profile form updates on typing.

**Output Screenshots:**

![Hands-On 5 — Project Setup & Components (Task 1)](screenshots/handson05_react_setup_task1.png)
![Hands-On 5 — useState & Dynamic Lists (Task 2)](screenshots/handson05_react_state_task2.png)

---

## Hands-On 6 — React Routing & State Management *(Intermediate)*

**Topics:** React Router v6 · `useNavigate` & `useParams` · `useContext` Hook · Context API for Global State · Introduction to Redux Toolkit

Added **React Router** (`/`, `/courses`, `/profile`, `/courses/:courseId`) with `<Link>`, `useParams()`, and `useNavigate()` for post-enroll redirects. Built `EnrollmentContext.jsx` with the Context API to share enrolled-courses state across `Header` and `ProfilePage` without prop drilling, including a "Remove"/un-enroll action. Finally refactored enrollment state to **Redux Toolkit** — `configureStore`, `createSlice` with `enroll`/`unenroll` reducers, and `useSelector` — verified live via Redux DevTools.

**Expected Outcome:** Clicking a course navigates to `/courses/1` and enrolling redirects to `/profile`; enrolling from any page instantly updates the Header count and Profile list via Context, then via Redux; Redux DevTools shows correct action/state diffs.

**Output Screenshots:**

![Hands-On 6 — React Router (Task 1)](screenshots/handson06_router_task1.png)
![Hands-On 6 — Context API (1)](screenshots/handson06_context_api_1.png)
![Hands-On 6 — Context API (2)](screenshots/handson06_context_api_2.png)
![Hands-On 6 — Redux Toolkit](screenshots/handson06_redux_toolkit.png)

---

## Hands-On 7 — Angular: Components, Services, DI, Routing & Forms *(Advanced)*

**Topics:** Angular CLI · Components & Modules · Services & Dependency Injection · RxJS & `HttpClient` · Angular Router · Reactive Forms

Generated `HeaderComponent`, `CourseListComponent`, `CourseCardComponent`, and `StudentProfileComponent` via Angular CLI, using `@Input()`, `*ngFor`, `[(ngModel)]` two-way binding, and `*ngIf`. Built a `CourseService` injecting `HttpClient` (constructor-based DI, `providedIn: 'root'`) to centralize data fetching from JSONPlaceholder, with a loading spinner driven by `*ngIf`. Configured Angular Router (`/`, `/profile`) with `router-outlet` and `[routerLink]`, and built a **Reactive Form** (`FormGroup`/`FormControl`) with validators for name, email, and semester, including inline error messages and a submit button disabled until valid.

**Expected Outcome:** Course list renders and filters via search; courses load through the injected service with a brief spinner; the `/profile` reactive form shows validation errors and stays disabled until valid.

**Output Screenshots:**

![Hands-On 7 — Angular Components & Data Binding (1)](screenshots/handson07_angular_components_1.png)
![Hands-On 7 — Angular Components & Data Binding (2)](screenshots/handson07_angular_components_2.png)
![Hands-On 7 — Services & Dependency Injection](screenshots/handson07_angular_service_di.png)
![Hands-On 7 — Routing & Reactive Forms (1)](screenshots/handson07_angular_routing_forms_1.png)
![Hands-On 7 — Routing & Reactive Forms (2)](screenshots/handson07_angular_routing_forms_2.png)

---

## Hands-On 8 — Vue.js: Composition API, Vue Router & Pinia *(Advanced)*

**Topics:** Vue 3 Template Syntax · Reactivity (`ref`, `reactive`) · Components & Props · Composition API (`setup`) · Vue Router · Pinia State Management

Built `CourseCard.vue` and `Header.vue` as Single File Components using `<script setup>` and `defineProps`, with a reactive `courses` array (`ref([])`) populated in `onMounted`, plus a `computed()` filtered list bound to a `v-model` search input. Configured **Vue Router** (`/`, `/courses`, `/courses/:id`, `/profile`) with `<RouterLink>`/`<RouterView>`, `useRoute()`, `useRouter()`, and a `beforeEach` navigation guard. Implemented a **Pinia** store (`defineStore('enrollment', ...)`) with reactive state, a `totalCredits` computed value, and `enroll`/`unenroll` actions — verified via Vue DevTools' Pinia tab.

**Expected Outcome:** Courses render and filter reactively; all four routes work correctly with redirects on enroll; Pinia state updates are reflected instantly across `Header`, `CoursesView`, and `ProfileView`.

**Output Screenshots:**

![Hands-On 8 — Vue Components & Reactivity](screenshots/handson08_vue_components.png)
![Hands-On 8 — Vue Router](screenshots/handson08_vue_router.png)
![Hands-On 8 — Pinia State Management](screenshots/handson08_vue_pinia.png)

---

## Hands-On 9 — Web Accessibility (a11y) & Cross-Browser Compatibility *(Advanced)*

**Topics:** WCAG 2.1 Guidelines · ARIA Attributes · Semantic HTML for Accessibility · Keyboard Navigation · Colour Contrast · Feature Detection & Polyfills · Cross-Browser Testing Tools

Ran a **Lighthouse** accessibility audit on the Student Portal, then fixed missing `alt` attributes, missing form `<label>`s, and heading-hierarchy violations. Added `aria-label`, `aria-current`, `tabindex="0"` with keyboard `Enter` handling on course cards, `aria-live="polite"` for the live search-results count, and `aria-expanded` for expandable elements — verifying full keyboard reachability. Checked colour contrast (WCAG AA 4.5:1) using the WebAIM contrast checker, tested the portal across Chrome/Firefox/Safari, checked feature support on **caniuse.com**, and added a CSS polyfill (`css-vars-ponyfill`) for older browsers.

**Expected Outcome:** Lighthouse accessibility score improves; all interactive elements are keyboard-reachable; all text/background pairs pass 4.5:1 contrast; layout is consistent across browsers.

**Output Screenshots:**

![Hands-On 9 — Accessibility Audit](screenshots/handson09_a11y_audit.png)
![Hands-On 9 — ARIA & Keyboard Navigation](screenshots/handson09_aria_keyboard_nav.png)
![Hands-On 9 — Colour Contrast Check (1)](screenshots/handson09_color_contrast_1.png)
![Hands-On 9 — Colour Contrast Check (2)](screenshots/handson09_color_contrast_2.png)
![Hands-On 9 — Cross-Browser Testing](screenshots/handson09_crossbrowser_test.png)

---

## Hands-On 10 — API Integration & Advanced State Management *(Advanced)*

**Topics:** Fetch API vs Axios (comparison) · Centralised API Layer · Redux Toolkit (advanced — `createAsyncThunk`) · NgRx (Angular) · Pinia (Vue) — Advanced Patterns · Error Boundaries & Global Error Handling

Built a centralised `apiClient.js` (single Axios instance with `baseURL`, headers, timeout) and `courseApi.js` (`getAllCourses`, `getCourseById`, `enrollStudent`), with response/request interceptors standardising errors and attaching an `Authorization` header. In React, added `createAsyncThunk('courses/fetchAll', ...)` with `pending`/`fulfilled`/`rejected` handling in `extraReducers`, dispatched from `useEffect`, and read via dedicated selectors (`selectCourses`, `selectCoursesLoading`). Documented the equivalent **NgRx** flow (Actions → Effect → API → Reducer → State → Selector) for Angular, and advanced **Pinia** patterns for Vue (`fetchAndEnroll`, `$reset()`, `storeToRefs`). Implemented a global error handler (React Error Boundary / Angular `ErrorHandler` / Vue `app.config.errorHandler`) and documented a framework state-management comparison (React+Redux vs Angular+NgRx vs Vue+Pinia).

**Expected Outcome:** All API calls flow through the centralised client; async thunks correctly manage loading/error state via selectors; the global error handler catches and displays a graceful fallback UI.

**Output Screenshots:**

![Hands-On 10 — Centralised API Layer](screenshots/handson10_api_layer.png)
![Hands-On 10 — Redux Toolkit Async Thunk](screenshots/handson10_redux_thunk.png)
![Hands-On 10 — NgRx / Pinia Advanced Patterns](screenshots/handson10_ngrx_pinia_advanced.png)

---

## ✅ Summary

| Hands-On | Topic | Framework/Tech |
|---|---|---|
| 1 | Semantic HTML5 & CSS3 Foundations | HTML/CSS |
| 2 | Flexbox, Grid & Responsive Design | CSS |
| 3 | ES6+ JavaScript & DOM Manipulation | Vanilla JS |
| 4 | Async JS, Fetch API & Axios | Vanilla JS |
| 5 | React Fundamentals — Props, State, Hooks | React |
| 6 | React Routing, Context API & Redux Toolkit | React |
| 7 | Angular Components, Services, DI, Routing, Forms | Angular |
| 8 | Vue Composition API, Router & Pinia | Vue.js |
| 9 | Accessibility (a11y) & Cross-Browser Compatibility | HTML/CSS/JS |
| 10 | Centralised API Layer & Advanced State Management | React/Angular/Vue |

*Submitted under: `Module2_FrontendDev/<YourName>/` — Digital Nurture 5.0, Python Full Stack Engineer Track.*
