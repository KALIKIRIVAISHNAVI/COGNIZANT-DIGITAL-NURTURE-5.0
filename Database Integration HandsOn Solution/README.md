# Digital Nurture 5.0 — Module 3: Database Integration
### Python Full Stack Engineer Track — Hands-On Exercise 

This README documents the completed work for all **7 Hands-On exercises** of Module 3 (Database Integration), covering **PostgreSQL, MySQL, and MongoDB**. It follows the single scenario used throughout the book — a **Student Course Registration System (`college_db`)** 

---

## Project Structure

```
Module3_DatabaseIntegration
├── hands_on_1.sql   (Schema Design & DDL)
├── hands_on_2.sql   (DML, Joins & Aggregations)
├── hands_on_3.sql   (Subqueries, Views & Transactions)
├── hands_on_4.sql   (Indexes, EXPLAIN & N+1)
├── hands_on_5/      (MongoDB — mongosh / Compass scripts)
├── orm/             (SQLAlchemy — models.py, crud.py)
└── migrations/      (Alembic migration scripts)
```

## Tools Used
PostgreSQL · MySQL Community Server 8.x · MongoDB Community Server + Compass · Python 3.10+ · VS Code · `psycopg2-binary` · `mysql-connector-python` · `pymongo` · `sqlalchemy` · `flask-sqlalchemy` · Alembic


## 🎓 Common Scenario: Student Course Registration System

A college digitising its Course Registration process. The relational schema (`college_db`) has five tables: **`departments`**, **`students`**, **`courses`**, **`enrollments`**, and **`professors`**, all pre-populated with the sample data provided in the book (4 departments, 8 students, 5 courses, 12 enrollments, 5 professors).

---

## Hands-On 1 — Schema Design & Core SQL: DDL and Normalisation 

**Topics:** Database Schema Design · Normalisation (1NF–3NF) · ER Relationships · DDL — `CREATE` / `ALTER` / `DROP` · Referential Integrity

Created the full `college_db` schema from scratch: `CREATE TABLE` statements for all five tables with `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, and `FOREIGN KEY` constraints enforcing referential integrity (students → departments, courses → departments, enrollments → students/courses, professors → departments). Documented 1NF/2NF/3NF compliance in SQL comments, then safely extended the schema with `ALTER TABLE` — adding `phone_number` and `max_seats` columns, a `CHECK` constraint on `grade`, renaming `hod_name` → `head_of_dept`, and rolling back the `phone_number` column.

**Expected Outcome:** All 5 tables created with no errors; `DESCRIBE`/`\d` confirms columns and constraints; each `ALTER` runs cleanly and the final schema matches the plan.

**Output Screenshots:**

<img width="975" height="519" alt="image" src="https://github.com/user-attachments/assets/ad993e3b-4cf1-4b55-9aee-c16a4f5472e6" />

<img width="975" height="522" alt="image" src="https://github.com/user-attachments/assets/21bf22b2-db27-4564-8d3c-de218a2b5ec3" />


---

## Hands-On 2 — Writing SQL Queries: DML, Joins & Aggregations 

**Topics:** DML — `INSERT` / `UPDATE` / `DELETE` · `SELECT` with `WHERE` / `ORDER BY` · `INNER JOIN`, `LEFT JOIN`, multi-table joins · Aggregate Functions (`COUNT`, `AVG`, `SUM`, `MAX`) · `GROUP BY` and `HAVING`

Populated `college_db` with the sample data, added two extra students, updated a grade, and deleted un-graded enrollments. Wrote single-table filtering queries (`WHERE`, `ORDER BY`, `LIKE`, `BETWEEN`), multi-table joins spanning 2–4 tables (student-department, enrollment-student-course, students with no enrollments via `LEFT JOIN`, courses with zero enrollments, departments with/without professors), and aggregation reports (enrollments per course, average salary per department, department budgets over ₹600,000, grade distribution for CS101, and `HAVING`-filtered department enrollment counts).

**Expected Outcome:** `students` table has 10 rows; `enrollments` only retains non-NULL grades; join queries correctly surface unmatched rows; aggregate queries return one row per department/course as expected.

**Output Screenshots:**

<img width="975" height="514" alt="image" src="https://github.com/user-attachments/assets/9b5d0d25-a03d-4859-b2a9-f42feb890c5b" />

<img width="975" height="520" alt="image" src="https://github.com/user-attachments/assets/825547ce-2659-425c-8a08-c247171ecac7" />

<img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/6d15549b-e30b-41b0-a14e-5a22408708a7" />

<img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/b8c3eb2d-01bd-4d0a-9554-d44112f6ddbe" />

---

## Hands-On 3 — Advanced SQL: Subqueries, Views & Transactions 

**Topics:** Subqueries (correlated & non-correlated) · Views — creation, usage, updatable views · Stored Procedures (MySQL) / Functions (PostgreSQL) · Transactions — `COMMIT`, `ROLLBACK`, `SAVEPOINT` · Indexes and Query Plans

Used non-correlated subqueries (students enrolled above the average), correlated subqueries/`NOT EXISTS` (courses with all-A grades, top-paid professor per department), and derived-table subqueries (departments with average salary > 85,000). Built `vw_student_enrollment_summary` and `vw_course_stats` views (including a GPA conversion via `CASE`), tested view updatability, and recreated a view `WITH CHECK OPTION`. Wrote `sp_enroll_student`/`fn_enroll_student` and `sp_transfer_student` stored procedures/functions wrapped in transactions with `ROLLBACK` on failure, plus a `SAVEPOINT` test for partial rollback.

**Expected Outcome:** Subqueries return correct filtered result sets; `vw_course_stats` returns 5 rows (one per course); the transfer procedure rolls back cleanly on error; the `SAVEPOINT` test shows only the pre-savepoint insert surviving.

**Output Screenshots:**

<img width="975" height="523" alt="image" src="https://github.com/user-attachments/assets/cf38faa2-782b-4f0d-a938-b4823e1d5fab" />

<img width="975" height="517" alt="image" src="https://github.com/user-attachments/assets/3b801774-453a-4069-a0c2-6af198069b21" />

<img width="975" height="522" alt="image" src="https://github.com/user-attachments/assets/69a4bd39-b2b6-4260-b74f-a5f341b8d90a" />

---

## Hands-On 4 — Query Optimisation: Indexes, EXPLAIN & the N+1 Problem 

**Topics:** Index Types — B-Tree, Composite, Partial · `EXPLAIN` / `EXPLAIN ANALYZE` · Query Plans — Seq Scan vs Index Scan · N+1 Query Problem · Connection Pooling (concept)

Captured a baseline `EXPLAIN`/`EXPLAIN FORMAT=JSON` plan on a 3-table join query and identified a Sequential/Full Table Scan. Added a B-Tree index on `students.enrollment_year`, a composite `UNIQUE` index on `enrollments(student_id, course_id)`, an index on `courses.course_code`, and a partial index on un-graded enrollments — then re-ran `EXPLAIN` to confirm the plan shifted from Seq Scan to Index Scan. Simulated the classic **N+1 problem** in Python (1 query + N per-row lookups), then fixed it with a single `JOIN` query, comparing round-trip counts and timing.

**Expected Outcome:** Post-index `EXPLAIN` shows an Index Scan; the composite unique index blocks duplicate enrollments; the N+1 script goes from 13 queries down to 1 query with identical results.

**Output Screenshots:**

<img width="975" height="519" alt="image" src="https://github.com/user-attachments/assets/7934590e-7477-4bd8-bdca-4d5dfd56efc3" />

<img width="975" height="523" alt="image" src="https://github.com/user-attachments/assets/882565a9-cc6c-4d48-9186-c06848cb67a0" />

<img width="975" height="498" alt="image" src="https://github.com/user-attachments/assets/b986f244-c2a4-4460-80e9-e8fe0fddfbf3" />

---

## Hands-On 5 — MongoDB: Document Modelling, CRUD & Aggregation 

**Topics:** Documents & Collections · BSON Types · CRUD Operations · Aggregation Pipeline · Indexes in MongoDB · Embedding vs Referencing

Modelled a `college_nosql.feedback` collection (course feedback: ratings, comments, tags, attachments) and inserted 10+ documents, including one intentionally missing the `attachments` field to demonstrate MongoDB's schema-less design. Practiced all CRUD operations: filtering by rating, array/tag queries with `$elemMatch`, field projection, `updateMany` with `$set`/`$push`, and conditional deletes. Built a multi-stage **aggregation pipeline** (`$match` → `$group` → `$sort` → `$project` with `$round`) for average rating per course, plus a `$unwind`-based tag-frequency leaderboard, and verified index usage (`IXSCAN` vs `COLLSCAN`) via `.explain('executionStats')`.

**Expected Outcome:** `db.feedback.countDocuments()` ≥ 10; tag/array queries return only matching CS101 feedback; the aggregation pipeline returns one document per course with `average_rating` rounded to 1 decimal; the tag leaderboard surfaces `'challenging'` near the top.

**Output Screenshots:**

<img width="607" height="491" alt="image" src="https://github.com/user-attachments/assets/a626e3e4-3f83-4f34-aacc-6ea2dc655b63" />

<img width="609" height="494" alt="image" src="https://github.com/user-attachments/assets/a247da02-292f-4e33-9f35-88b22f05ca42" />

<img width="623" height="504" alt="image" src="https://github.com/user-attachments/assets/d277e4f1-0a88-46de-b759-bfd5a26062ab" />


---

## Hands-On 6 — ORM Integration: SQLAlchemy & Django ORM 

**Topics:** SQLAlchemy Core & ORM · Django ORM (models, queries) · Defining Models and Relationships · CRUD via ORM · Sessions and Connection Pooling · Avoiding N+1 with `joinedload` / `select_related`

Defined `Department`, `Student`, `Course`, `Enrollment`, and `Professor` ORM model classes in `models.py` mirroring the SQL schema, with `relationship()` mappings (many-to-one Student→Department, Enrollment→Student/Course), and auto-created tables in `college_db_orm` via `Base.metadata.create_all(engine)`. Performed full CRUD through a SQLAlchemy `Session` (`crud.py`) — inserts, filtered reads via `.join()`, updates, and deletes — enabling `echo=True` to reveal an N+1 query pattern on the enrollment/student/course read. Fixed it using `joinedload()` (dropping query count from 13 to 1), and noted the equivalent Django `select_related()` approach.

**Expected Outcome:** `python models.py` creates all 5 tables in `college_db_orm`; CRUD operations commit/query correctly; `echo=True` logs confirm the N+1 pattern is eliminated after adding `joinedload`.

**Output Screenshots:**

<img width="975" height="792" alt="image" src="https://github.com/user-attachments/assets/80e2e211-7f72-4b28-8177-7a081053729e" />

<img width="975" height="772" alt="image" src="https://github.com/user-attachments/assets/aef4f94d-c758-4661-9bc3-8721536213c5" />

<img width="674" height="552" alt="image" src="https://github.com/user-attachments/assets/e49a5d35-dec7-4ef1-991c-bbe75014b269" />

<img width="667" height="548" alt="image" src="https://github.com/user-attachments/assets/a5154d12-eef2-4bb0-a7d5-386b5f60a8c3" />

---

## Hands-On 7 — Migrations & Versioning: Alembic and Django Migrations 

**Topics:** Migration Concepts · Alembic for SQLAlchemy · Django Migrations · Migration History and Version Control · Rollback Strategies

Initialised Alembic (`alembic init migrations`), pointed it at `college_db_orm`, and generated a baseline migration via `--autogenerate`, applying it with `alembic upgrade head` and confirming the `alembic_version` table. Added incremental schema changes — an `is_active` column on `Student` and a new `CourseSchedule` table — each as its own autogenerated, inspected, and applied migration, then reviewed the full chain with `alembic history --verbose`. Practiced safe rollback: `alembic downgrade -1` (removes `is_active`), `alembic downgrade base` (removes all migrations), and re-applying with `alembic upgrade head` to confirm full recovery — with a bonus note on the equivalent Django `makemigrations`/`migrate` rollback workflow.

**Expected Outcome:** `alembic history` shows 3 revisions; `is_active` and `course_schedules` exist after upgrades; `downgrade -1` removes `is_active` and `upgrade head` restores it, matching the expected head hash.

**Output Screenshots:**

<img width="603" height="488" alt="image" src="https://github.com/user-attachments/assets/99bff59f-2bc1-44e8-922e-b6fd42317fda" />

<img width="702" height="569" alt="image" src="https://github.com/user-attachments/assets/6009d62b-5062-4b81-adea-d47b7d2f70a1" />

---

## Summary

| Hands-On | Topic | Technology |
|---|---|---|
| 1 | Schema Design & Core SQL (DDL, Normalisation) | PostgreSQL / MySQL |
| 2 | DML, Joins & Aggregations | PostgreSQL / MySQL |
| 3 | Subqueries, Views & Transactions | PostgreSQL / MySQL |
| 4 | Query Optimisation — Indexes, EXPLAIN, N+1 | PostgreSQL / MySQL + Python |
| 5 | Document Modelling, CRUD & Aggregation | MongoDB |
| 6 | ORM Integration | SQLAlchemy (Python) |
| 7 | Migrations & Versioning | Alembic / Django Migrations |

## Submitted By : KALIKIRI VAISHNAVI
