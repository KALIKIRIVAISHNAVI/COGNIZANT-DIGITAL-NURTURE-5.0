# Digital Nurture 5.0 — Python Backend Frameworks
### Python Full Stack Engineer Track — Hands-On Exercise Book (Output Log)

---

## 📁 Project Structure

```
PythonBackendFrameworks/<YourName>/
├── handson_01/      (Web Framework Foundations & Django Setup)
├── handson_02/      (Django Models, ORM & Admin)
├── handson_03/      (Django REST Views, ViewSets & Routers)
├── handson_04/      (Flask App Structure, Routing & Blueprints)
├── handson_05/      (Flask + SQLAlchemy ORM Integration)
├── handson_06/      (FastAPI Setup, Pydantic & Async Basics)
├── handson_07/      (FastAPI Dependency Injection, CRUD & OpenAPI)
├── handson_08/      (RESTful API Design Best Practices)
├── handson_09/      (JWT Auth, Password Hashing & CORS)
└──  handson_10/      (Microservices Decomposition & API Gateway)

```

## Tools Used
Django · Django REST Framework · Flask · Flask-SQLAlchemy · FastAPI · Uvicorn · SQLAlchemy
(sync & async) · Pydantic · python-jose · passlib · bcrypt · Postman / Thunder Client · Python 3.10+
· VS Code · Git


## Common Scenario: Course Management API

A college digitising its course management process. The API manages **Departments, Courses,
Students, and Enrollments**, exposed through RESTful endpoints consumed by a frontend
application. The same system is built three times — once each in **Django**, **Flask**, and
**FastAPI** — to compare how each framework approaches the same problem.

---

## Hands-On 1 — Web Framework Foundations & Django Project Setup *(Beginner)*

**Topics:** Web Framework Concepts · MVC/MVT Pattern · Request-Response Cycle · WSGI vs ASGI ·
Django Project Setup · URL Routing & Middleware

Mapped the journey of a `GET /api/courses/` request through Django (URL router → View → Model →
Response) in code comments, documented where middleware sits in that cycle along with two
built-in middleware classes, and explained WSGI vs ASGI and when Django would switch between
them. Mapped the classic MVC pattern onto Django's MVT convention. Scaffolded the project with
`django-admin startproject coursemanager`, created a `courses` app with `startapp`, registered it
in `INSTALLED_APPS`, wrote a function-based `hello_view` returning a plain `HttpResponse`, and
wired it to `/api/hello/` in `urls.py`.

**Expected Outcome:** Browser shows `Course Management API is running` at `/api/hello/`; the
`courses` app is listed in `INSTALLED_APPS`.

**Output Screenshots:**

<img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/a4a78f8b-80ae-4a4e-8436-041d69aec461" />


---

## Hands-On 2 — Django Models, ORM & Admin Interface *(Beginner)*

**Topics:** Django Models · Field Types & Constraints · Migrations · Django ORM Queries · Admin
Interface Registration

Defined the `Department`, `Course`, `Student`, and `Enrollment` models with appropriate fields,
`ForeignKey` relations, `__str__` methods, and a `unique_together` constraint on `Enrollment` to
block duplicate enrollments. Ran `makemigrations`/`migrate` and verified the created tables via
`dbshell`. Used the Django shell to create sample departments, courses, and students, then
practiced ORM lookups across relationships (`department__name=...`), `.annotate()` with `Count`,
`select_related` for single-query joins, and a bulk `F()`-expression update on department budgets.
Registered all models in `admin.py` and customised `CourseAdmin` with `list_display`,
`search_fields`, and `list_filter`.

**Expected Outcome:** `showmigrations` shows all migrations applied; ORM queries return the
expected results; the admin interface supports search/filter and rejects duplicate enrollments.

**Output Screenshots:**


---

## Hands-On 3 — Django REST Views, URL Routing & Forms *(Beginner)*

**Topics:** Function-Based Views (FBV) · Class-Based Views (CBV) · URL Routing with `include()` ·
Django REST Framework (DRF) Basics · Serializers · Request & Response Objects

Installed DRF and created `ModelSerializer`s for all four models. Built `CourseListView`
(GET/POST) and `CourseDetailView` (GET/PUT/DELETE) using DRF's `APIView`, wired them into
`courses/urls.py`, and tested every operation in Postman/the browsable API. Refactored both views
into a single `CourseViewSet` extending `viewsets.ModelViewSet`, registered it with a
`DefaultRouter` alongside `StudentViewSet` and `EnrollmentViewSet`, and added a custom `@action`
endpoint `/api/courses/{id}/students/` returning only the students enrolled in that course.

**Expected Outcome:** All 5 HTTP methods return correct status codes (200/201/204/400/404); the
custom `/students/` action returns the correctly filtered list of enrolled students.

**Output Screenshots:**

<img width="668" height="528" alt="image" src="https://github.com/user-attachments/assets/b21ce77a-b740-41b8-a4d1-3a51bbcd4f3c" />

<img width="738" height="583" alt="image" src="https://github.com/user-attachments/assets/6735f450-9507-4b1f-b9e7-424bc5f4f390" />

<img width="690" height="542" alt="image" src="https://github.com/user-attachments/assets/2a8cebee-2683-49bf-a034-42077d3638b9" />

<img width="761" height="604" alt="image" src="https://github.com/user-attachments/assets/5270e164-b714-4cd2-a370-bf7179d47c8f" />

<img width="666" height="523" alt="image" src="https://github.com/user-attachments/assets/73945f22-ee67-449a-93cc-6aaccbde4209" />

<img width="689" height="545" alt="image" src="https://github.com/user-attachments/assets/e8b0e6ee-5c49-4b0c-b163-ec8fc4455aa0" />

---

## Hands-On 4 — Flask: App Structure, Routing, Jinja2 & Blueprints *(Intermediate)*

**Topics:** Flask App Structure · Routing & URL Rules · Jinja2 Templates · Request & Response
Objects · Blueprints for Modular Design · Flask Configuration

Structured the Flask project around the **application factory pattern** (`create_app()`), with a
`Config` class supplying `SQLALCHEMY_DATABASE_URI`, `SECRET_KEY`, and `DEBUG`. Built a
`courses_bp` Blueprint with `url_prefix='/api/courses'` and registered it in the factory. Parsed
incoming JSON with `request.get_json()`, validated required fields (`name`, `code`, `credits`),
added full CRUD routes (GET/POST/PUT/DELETE), a consistent JSON response envelope
(`{'status': 'success', 'data': ...}`), and JSON-based error handlers for 404/500 so the API never
falls back to Flask's default HTML error pages.

**Expected Outcome:** All endpoints return JSON; missing required fields return 400 with a
descriptive message; unknown course IDs return 404.

**Output Screenshots:**

<img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/b2bd1b1c-0029-431b-967b-104cd00f2140" />

<img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/d1475015-36e3-465f-9094-906a8b0c38db" />

<img width="975" height="514" alt="image" src="https://github.com/user-attachments/assets/848e1237-95b8-4b0a-b118-6f0d48f72513" />

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/8da5278b-05f7-44d6-bc36-27f0ccdc6880" />

<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/80e6a4ea-e1e8-4c38-b8c1-399ed49b6cf6" />

---

## Hands-On 5 — Flask with SQLAlchemy ORM & Database Integration *(Intermediate)*

**Topics:** Flask-SQLAlchemy Setup · Model Definition · Migrations with Flask-Migrate · ORM CRUD
Operations · Relationship Queries · Connection Pooling

Initialised `db = SQLAlchemy()` / `db.init_app(app)` and defined `Department`, `Course`,
`Student`, and `Enrollment` as `db.Model` subclasses with `db.relationship()` links mirroring the
Django schema. Set up Flask-Migrate (`flask db init/migrate/upgrade`) and inserted sample data via
the Flask shell. Replaced the in-memory route data from Hands-On 4 with real queries
(`Course.query.all()`, `Course.query.get_or_404(id)`), added a `to_dict()` serialization helper on
each model, and wired a JOIN-based `/api/courses/<id>/students/` route.

**Expected Outcome:** `flask db upgrade` creates all tables; CRUD endpoints read from and write to
the database; the `/students/` route returns the correct enrolled students via a JOIN.

**Output Screenshots:**

---

## Hands-On 6 — FastAPI: Path Parameters, Pydantic & Async Endpoints *(Intermediate)*

**Topics:** FastAPI Project Setup · Path & Query Parameters · Pydantic Models for Validation ·
Async/Await in FastAPI · Automatic OpenAPI/Swagger Docs · Response Models

Scaffolded `main.py` with `FastAPI(title='Course Management API', version='1.0')` and a root `/`
route. Defined Pydantic schemas — `CourseCreate`, `CourseUpdate` (optional fields), and
`CourseResponse` — plus a nested `DepartmentResponse` to demonstrate nested models. Built
`POST /api/courses/` with automatic request validation (422 on bad input) and explored the
auto-generated Swagger UI at `/docs`. Added a typed path parameter on
`GET /api/courses/{course_id}` and pagination/filter query parameters (`skip`, `limit`,
`department_id`) on the list endpoint, backed by an async SQLAlchemy engine and a `get_db()`
dependency.

**Expected Outcome:** `/docs` shows the `CourseCreate` schema; invalid payloads return 422 with
field-level errors; `GET /api/courses/?skip=&limit=` returns the correctly paginated subset.

**Output Screenshots:**

---

## Hands-On 7 — FastAPI: Dependency Injection, CRUD & OpenAPI Documentation *(Intermediate)*

**Topics:** FastAPI Dependency Injection · CRUD Operations · Response Models & Status Codes ·
Background Tasks · OpenAPI Customisation · Error Handling with `HTTPException`

Completed `PUT`/`DELETE` on courses using `response_model=CourseResponse`,
`status_code=201` on create, and `status_code=204` (no body) on delete, raising
`HTTPException(status_code=404, ...)` for missing resources. Added a JOIN-based
`/api/courses/{id}/students/` endpoint and full CRUD for Students and Enrollments. Attached a
`BackgroundTasks` parameter to `POST /api/enrollments/` to simulate an async confirmation email
without blocking the response, then customised the OpenAPI metadata (title, description, version,
contact) and grouped endpoints with `tags` for a cleaner `/docs` page.

**Expected Outcome:** POST returns 201 immediately while the background task logs afterward in the
console; `/docs` shows grouped, well-documented endpoints.

**Output Screenshots:**

<img width="668" height="670" alt="image" src="https://github.com/user-attachments/assets/8667e10f-9853-4322-8cb0-522dd4899137" />

<img width="634" height="481" alt="image" src="https://github.com/user-attachments/assets/c1d9e94d-875c-42ef-ae0c-900c16caaac3" />

---

## Hands-On 8 — RESTful API Design Best Practices *(Advanced)*

**Topics:** REST Principles · HTTP Methods & Status Codes · Resource Naming Conventions · API
Versioning · Pagination & Filtering · Error Response Standards

Audited existing endpoints for REST naming violations (plural nouns, no verbs, hyphens instead of
underscores) and added a `PATCH /api/courses/{id}/` endpoint alongside the existing `PUT`. Verified
status codes across the board (200/201/204/400/401/404/422) and added a `Location` header to POST
responses. Introduced URL-based versioning (`/api/v1/...`), implemented offset pagination
(`page`, `page_size`) with a DRF-style envelope (`count`/`next`/`previous`/`results`), added a
case-insensitive `search=` filter on course name/code, and standardised all error responses to a
single `{'error': {'code', 'message', 'field'}}` shape.

**Expected Outcome:** `GET /api/v1/courses/?page=1&page_size=2` returns the correct paginated
envelope; all error responses follow the standardised format.

**Output Screenshots:**


---

## Hands-On 9 — Authentication & Security: JWT, OAuth2 & OWASP *(Advanced)*

**Topics:** JWT Token Structure · Token-Based Auth vs Session-Based Auth · Password Hashing with
bcrypt · OAuth2 Flow (concept) · CORS Configuration · OWASP Top 10 Awareness

Created a `User` model and `security.py` helpers (`get_password_hash`, `verify_password`) using
passlib's `CryptContext` with the bcrypt scheme. Built `POST /api/v1/auth/register/` — validating
email format, checking for duplicates (409 Conflict), hashing the password, and never storing or
logging plain text. Built `POST /api/v1/auth/login/` to verify credentials and issue a 30-minute
JWT via `python-jose`, plus a `get_current_user()` dependency that decodes/validates the token
(401 on invalid/expired) and protects the course-mutation endpoints. Configured CORS for
`http://localhost:3000` and documented the OAuth2 Authorization Code flow against the simpler JWT
login implemented here.

**Expected Outcome:** Login returns a valid JWT; unauthenticated POST/DELETE requests on
`/api/v1/courses/` return 401; CORS allows the `localhost:3000` frontend origin.

**Output Screenshots:**

<img width="759" height="389" alt="image" src="https://github.com/user-attachments/assets/e9515104-0098-4641-9c08-7930b834da2c" />

<img width="600" height="450" alt="image" src="https://github.com/user-attachments/assets/ad9b4926-0a23-49be-8e13-32f249fd8f8f" />

<img width="655" height="506" alt="image" src="https://github.com/user-attachments/assets/db4b843b-7511-4d9d-9973-94a0d16240f4" />

---

## Hands-On 10 — Microservices Architecture: Concepts & Decomposition *(Advanced)*

**Topics:** Monolith vs Microservices · Service Decomposition · Inter-Service Communication · API
Gateway Pattern · Service Discovery (concept)

Identified 3–4 bounded contexts in the existing API — Student Service, Course Service, Auth
Service, Notification Service — and documented each as `Service Name | Responsibility | Endpoints
it owns | Database it owns` in a `README.md`. Built two minimal, independently-running Flask apps:
`course_service/` (port 5001) and `student_service/` (port 5002), each with its own SQLite
database. Added `POST /api/students/{id}/enroll` on Student Service, which calls Course Service's
`GET /api/courses/{id}/` via `requests` to confirm the course exists, catching `ConnectionError`
and returning 503 if Course Service is unreachable. Built a minimal API Gateway (`gateway/`, port
5000) proxying `/api/courses/*` and `/api/students/*` to the correct backend service, and
documented the trade-offs of synchronous (HTTP) vs asynchronous (message queue) inter-service
communication.

**Expected Outcome:** A request through the gateway successfully routes Student Service → Course
Service; stopping Course Service causes the enrollment endpoint to return 503.

**Output Screenshots:**


---

## Summary

| Hands-On | Topic | Technology |
|---|---|---|
| 1 | Web Framework Foundations & Django Project Setup | Django |
| 2 | Django Models, ORM & Admin Interface | Django |
| 3 | Django REST Views, URL Routing & ViewSets | Django + DRF |
| 4 | Flask App Structure, Routing & Blueprints | Flask |
| 5 | Flask + SQLAlchemy ORM Integration | Flask |
| 6 | FastAPI Setup, Pydantic & Async Basics | FastAPI |
| 7 | FastAPI Dependency Injection, CRUD & OpenAPI Docs | FastAPI |
| 8 | RESTful API Design Best Practices | Django / Flask / FastAPI |
| 9 | JWT Auth, Password Hashing & CORS | Django / Flask / FastAPI |
| 10 | Microservices Decomposition & API Gateway | Flask |

## Submitted By: KALIKIRI VAISHNAVI
