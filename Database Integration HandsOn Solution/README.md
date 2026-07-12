# Digital Nurture 5.0 — Module 3: Database Integration
### Python Full Stack Engineer Track — Hands-On Exercise Book (Output Log)

This README documents the completed work for all **7 Hands-On exercises** of Module 3 (Database Integration), covering **PostgreSQL, MySQL, and MongoDB**. It follows the single scenario used throughout the book — a **Student Course Registration System (`college_db`)** — and includes the output screenshots captured for each exercise.

---

## 📁 Project Structure

```
Module3_DatabaseIntegration/<YourName>/
├── hands_on_1.sql   (Schema Design & DDL)
├── hands_on_2.sql   (DML, Joins & Aggregations)
├── hands_on_3.sql   (Subqueries, Views & Transactions)
├── hands_on_4.sql   (Indexes, EXPLAIN & N+1)
├── hands_on_5/      (MongoDB — mongosh / Compass scripts)
├── orm/             (SQLAlchemy — models.py, crud.py)
└── migrations/      (Alembic migration scripts)
```

## 🧰 Tools Used
PostgreSQL · MySQL Community Server 8.x · MongoDB Community Server + Compass · Python 3.10+ · VS Code · `psycopg2-binary` · `mysql-connector-python` · `pymongo` · `sqlalchemy` · `flask-sqlalchemy` · Alembic

## 📊 Difficulty Guide

| Level | Hands-On | Focus |
|---|---|---|
| Beginner | 1, 2 | Core SQL, schema design, basic CRUD |
| Intermediate | 3, 4, 5 | Advanced queries, MongoDB, optimisation |
| Advanced | 6, 7 | ORM integration, migrations, Python backend |

## 🎓 Common Scenario: Student Course Registration System

A college digitising its Course Registration process. The relational schema (`college_db`) has five tables: **`departments`**, **`students`**, **`courses`**, **`enrollments`**, and **`professors`**, all pre-populated with the sample data provided in the book (4 departments, 8 students, 5 courses, 12 enrollments, 5 professors).

---

## Hands-On 1 — Schema Design & Core SQL: DDL and Normalisation *(Beginner)*

**Topics:** Database Schema Design · Normalisation (1NF–3NF) · ER Relationships · DDL — `CREATE` / `ALTER` / `DROP` · Referential Integrity

Created the full `college_db` schema from scratch: `CREATE TABLE` statements for all five tables with `NOT NULL`, `UNIQUE`, `PRIMARY KEY`, and `FOREIGN KEY` constraints enforcing referential integrity (students → departments, courses → departments, enrollments → students/courses, professors → departments). Documented 1NF/2NF/3NF compliance in SQL comments, then safely extended the schema with `ALTER TABLE` — adding `phone_number` and `max_seats` columns, a `CHECK` constraint on `grade`, renaming `hod_name` → `head_of_dept`, and rolling back the `phone_number` column.

**Expected Outcome:** All 5 tables created with no errors; `DESCRIBE`/`\d` confirms columns and constraints; each `ALTER` runs cleanly and the final schema matches the plan.

**Output Screenshots:**

![Hands-On 1 — Task 1: DDL / CREATE TABLE](screenshots/handson01_task1_ddl_create.png)
![Hands-On 1 — Task 3: ALTER TABLE](screenshots/handson01_task3_alter_table.png)

---

## Hands-On 2 — Writing SQL Queries: DML, Joins & Aggregations *(Beginner)*

**Topics:** DML — `INSERT` / `UPDATE` / `DELETE` · `SELECT` with `WHERE` / `ORDER BY` · `INNER JOIN`, `LEFT JOIN`, multi-table joins · Aggregate Functions (`COUNT`, `AVG`, `SUM`, `MAX`) · `GROUP BY` and `HAVING`

Populated `college_db` with the sample data, added two extra students, updated a grade, and deleted un-graded enrollments. Wrote single-table filtering queries (`WHERE`, `ORDER BY`, `LIKE`, `BETWEEN`), multi-table joins spanning 2–4 tables (student-department, enrollment-student-course, students with no enrollments via `LEFT JOIN`, courses with zero enrollments, departments with/without professors), and aggregation reports (enrollments per course, average salary per department, department budgets over ₹600,000, grade distribution for CS101, and `HAVING`-filtered department enrollment counts).

**Expected Outcome:** `students` table has 10 rows; `enrollments` only retains non-NULL grades; join queries correctly surface unmatched rows; aggregate queries return one row per department/course as expected.

**Output Screenshots:**

![Hands-On 2 — Task 1: DML (Insert/Update/Delete)](screenshots/handson02_task1_dml.png)
![Hands-On 2 — Task 2: Filtering with WHERE/ORDER BY/LIKE](screenshots/handson02_task2_filtering.png)
![Hands-On 2 — Task 3: Multi-Table Joins](screenshots/handson02_task3_joins.png)
![Hands-On 2 — Task 4: Aggregations & GROUP BY/HAVING](screenshots/handson02_task4_aggregations.png)

---

## Hands-On 3 — Advanced SQL: Subqueries, Views & Transactions *(Intermediate)*

**Topics:** Subqueries (correlated & non-correlated) · Views — creation, usage, updatable views · Stored Procedures (MySQL) / Functions (PostgreSQL) · Transactions — `COMMIT`, `ROLLBACK`, `SAVEPOINT` · Indexes and Query Plans

Used non-correlated subqueries (students enrolled above the average), correlated subqueries/`NOT EXISTS` (courses with all-A grades, top-paid professor per department), and derived-table subqueries (departments with average salary > 85,000). Built `vw_student_enrollment_summary` and `vw_course_stats` views (including a GPA conversion via `CASE`), tested view updatability, and recreated a view `WITH CHECK OPTION`. Wrote `sp_enroll_student`/`fn_enroll_student` and `sp_transfer_student` stored procedures/functions wrapped in transactions with `ROLLBACK` on failure, plus a `SAVEPOINT` test for partial rollback.

**Expected Outcome:** Subqueries return correct filtered result sets; `vw_course_stats` returns 5 rows (one per course); the transfer procedure rolls back cleanly on error; the `SAVEPOINT` test shows only the pre-savepoint insert surviving.

**Output Screenshots:**

![Hands-On 3 — Task 1: Subqueries](screenshots/handson03_task1_subqueries.png)
![Hands-On 3 — Task 2: Views](screenshots/handson03_task2_views.png)
![Hands-On 3 — Task 3: Stored Procedures & Transactions](screenshots/handson03_task3_procedures_transactions.png)

---

## Hands-On 4 — Query Optimisation: Indexes, EXPLAIN & the N+1 Problem *(Intermediate)*

**Topics:** Index Types — B-Tree, Composite, Partial · `EXPLAIN` / `EXPLAIN ANALYZE` · Query Plans — Seq Scan vs Index Scan · N+1 Query Problem · Connection Pooling (concept)

Captured a baseline `EXPLAIN`/`EXPLAIN FORMAT=JSON` plan on a 3-table join query and identified a Sequential/Full Table Scan. Added a B-Tree index on `students.enrollment_year`, a composite `UNIQUE` index on `enrollments(student_id, course_id)`, an index on `courses.course_code`, and a partial index on un-graded enrollments — then re-ran `EXPLAIN` to confirm the plan shifted from Seq Scan to Index Scan. Simulated the classic **N+1 problem** in Python (1 query + N per-row lookups), then fixed it with a single `JOIN` query, comparing round-trip counts and timing.

**Expected Outcome:** Post-index `EXPLAIN` shows an Index Scan; the composite unique index blocks duplicate enrollments; the N+1 script goes from 13 queries down to 1 query with identical results.

**Output Screenshots:**

![Hands-On 4 — Task 1: Baseline EXPLAIN Plan](screenshots/handson04_task1_baseline_explain.png)
![Hands-On 4 — Task 2: Indexes & Query Plan Comparison](screenshots/handson04_task2_indexes.png)
![Hands-On 4 — Task 3: N+1 Problem — Before/After](screenshots/handson04_task3_n_plus_1.png)

---

## Hands-On 5 — MongoDB: Document Modelling, CRUD & Aggregation *(Intermediate)*

**Topics:** Documents & Collections · BSON Types · CRUD Operations · Aggregation Pipeline · Indexes in MongoDB · Embedding vs Referencing

Modelled a `college_nosql.feedback` collection (course feedback: ratings, comments, tags, attachments) and inserted 10+ documents, including one intentionally missing the `attachments` field to demonstrate MongoDB's schema-less design. Practiced all CRUD operations: filtering by rating, array/tag queries with `$elemMatch`, field projection, `updateMany` with `$set`/`$push`, and conditional deletes. Built a multi-stage **aggregation pipeline** (`$match` → `$group` → `$sort` → `$project` with `$round`) for average rating per course, plus a `$unwind`-based tag-frequency leaderboard, and verified index usage (`IXSCAN` vs `COLLSCAN`) via `.explain('executionStats')`.

**Expected Outcome:** `db.feedback.countDocuments()` ≥ 10; tag/array queries return only matching CS101 feedback; the aggregation pipeline returns one document per course with `average_rating` rounded to 1 decimal; the tag leaderboard surfaces `'challenging'` near the top.

**Output Screenshots:**

![Hands-On 5 — Task 1: Collection & Document Inserts](screenshots/handson05_task1_mongo_insert.png)
![Hands-On 5 — Task 2: CRUD Operations](screenshots/handson05_task2_mongo_crud.png)
![Hands-On 5 — Task 3: Aggregation Pipeline](screenshots/handson05_task3_aggregation_pipeline.png)

---

## Hands-On 6 — ORM Integration: SQLAlchemy & Django ORM *(Advanced)*

**Topics:** SQLAlchemy Core & ORM · Django ORM (models, queries) · Defining Models and Relationships · CRUD via ORM · Sessions and Connection Pooling · Avoiding N+1 with `joinedload` / `select_related`

Defined `Department`, `Student`, `Course`, `Enrollment`, and `Professor` ORM model classes in `models.py` mirroring the SQL schema, with `relationship()` mappings (many-to-one Student→Department, Enrollment→Student/Course), and auto-created tables in `college_db_orm` via `Base.metadata.create_all(engine)`. Performed full CRUD through a SQLAlchemy `Session` (`crud.py`) — inserts, filtered reads via `.join()`, updates, and deletes — enabling `echo=True` to reveal an N+1 query pattern on the enrollment/student/course read. Fixed it using `joinedload()` (dropping query count from 13 to 1), and noted the equivalent Django `select_related()` approach.

**Expected Outcome:** `python models.py` creates all 5 tables in `college_db_orm`; CRUD operations commit/query correctly; `echo=True` logs confirm the N+1 pattern is eliminated after adding `joinedload`.

**Output Screenshots:**

![Hands-On 6 — Task 1: SQLAlchemy Models & Engine (1)](screenshots/handson06_task1_sqlalchemy_models_1.png)
![Hands-On 6 — Task 1: SQLAlchemy Models & Engine (2)](screenshots/handson06_task1_sqlalchemy_models_2.png)
![Hands-On 6 — Task 2: CRUD via ORM Session](screenshots/handson06_task2_orm_crud.png)
![Hands-On 6 — Task 3: Eager Loading (joinedload) Fixing N+1](screenshots/handson06_task3_eager_loading.png)

---

## Hands-On 7 — Migrations & Versioning: Alembic and Django Migrations *(Advanced)*

**Topics:** Migration Concepts · Alembic for SQLAlchemy · Django Migrations · Migration History and Version Control · Rollback Strategies

Initialised Alembic (`alembic init migrations`), pointed it at `college_db_orm`, and generated a baseline migration via `--autogenerate`, applying it with `alembic upgrade head` and confirming the `alembic_version` table. Added incremental schema changes — an `is_active` column on `Student` and a new `CourseSchedule` table — each as its own autogenerated, inspected, and applied migration, then reviewed the full chain with `alembic history --verbose`. Practiced safe rollback: `alembic downgrade -1` (removes `is_active`), `alembic downgrade base` (removes all migrations), and re-applying with `alembic upgrade head` to confirm full recovery — with a bonus note on the equivalent Django `makemigrations`/`migrate` rollback workflow.

**Expected Outcome:** `alembic history` shows 3 revisions; `is_active` and `course_schedules` exist after upgrades; `downgrade -1` removes `is_active` and `upgrade head` restores it, matching the expected head hash.

**Output Screenshots:**

![Hands-On 7 — Task 1: Alembic Init & Baseline Migration](screenshots/handson07_task1_alembic_baseline.png)
![Hands-On 7 — Task 3: Rollback & Recovery](screenshots/handson07_task3_rollback_recovery.png)

*(No separate screenshot was captured for Task 2 — Incremental Migrations; the `is_active` column and `course_schedules` table additions were verified directly against the applied migration chain shown in Tasks 1 and 3.)*

---

## ✅ Summary

| Hands-On | Topic | Technology |
|---|---|---|
| 1 | Schema Design & Core SQL (DDL, Normalisation) | PostgreSQL / MySQL |
| 2 | DML, Joins & Aggregations | PostgreSQL / MySQL |
| 3 | Subqueries, Views & Transactions | PostgreSQL / MySQL |
| 4 | Query Optimisation — Indexes, EXPLAIN, N+1 | PostgreSQL / MySQL + Python |
| 5 | Document Modelling, CRUD & Aggregation | MongoDB |
| 6 | ORM Integration | SQLAlchemy (Python) |
| 7 | Migrations & Versioning | Alembic / Django Migrations |

*Submitted under: `Module3_DatabaseIntegration/<YourName>/` — Digital Nurture 5.0, Python Full Stack Engineer Track.*
