# QA Concepts, Functional Testing & Defect Lifecycle
### Hands-On 1 — Submission


---

## Task 1: Map Testing Types to a Real System

**Goal:** Classify and apply different testing types to the Course Management API.

### 1. Test Case for Each Testing Level

#### a) Unit Testing
**Test Case:** Verify the `validateCourseCode()` function correctly rejects a course code that does not match the required format (e.g., `CS-101`).

- **Scope:** A single function, tested in isolation, with no database or external dependency involved.
- **Input:** `"cs101"` (lowercase, missing hyphen)
- **Expected Result:** Function returns `false` / raises a `ValidationError`, without touching the database or any other module.

#### b) Integration Testing
**Test Case:** Verify that the `POST /api/courses/` endpoint correctly writes a new course record to the database and that the response reflects what was actually stored.

- **Scope:** Two components working together — the API layer and the database layer.
- **Steps:** Send a valid course-creation payload to the endpoint → query the database directly → compare the stored row with the API response.
- **Expected Result:** The record in the database exactly matches the data returned by the API (same course code, name, credits, timestamps).

#### c) System Testing
**Test Case:** Verify the full end-to-end flow of creating a course, from the API request through to the database and back to a confirmation response.

- **Scope:** The entire application stack (API → business logic → database → response), tested as one system, no mocking.
- **Steps:** Authenticate → send `POST /api/courses/` with valid data → verify HTTP 201 response → verify course appears in `GET /api/courses/` → verify course appears correctly in downstream reporting.
- **Expected Result:** The course flows correctly through every layer of the system end-to-end.

#### d) User Acceptance Testing (UAT)
**Test Case:** A college admin logs into the Course Management portal and adds a new course for the upcoming semester using the UI, exactly as they would in daily use.

- **Scope:** Tested from the perspective of an actual college admin user, not a QA engineer.
- **Steps:** Admin logs in → navigates to "Add Course" → fills in course name, code, credits, and instructor → submits → confirms the course appears in the course catalog.
- **Expected Result:** The admin can complete the task without confusion, errors, or needing developer assistance, and the course is usable in real scheduling workflows.

---

### 2. Functional vs Non-Functional Classification

| Test Case | Classification |
|---|---|
| a) Unit — `validateCourseCode()` | Functional (does it do what it should?) |
| b) Integration — API writes to DB correctly | Functional |
| c) System — end-to-end course creation flow | Functional |
| d) UAT — admin adds a course via UI | Functional |

**Non-Functional Test Example (Performance):**
Verify that `POST /api/courses/` responds within **500ms** when the courses table contains **100,000+ records**, under a load of **50 concurrent requests**. This does not test *what* the API does, but *how well* it performs under realistic load — a non-functional (performance) requirement.

*(Other non-functional angles that could apply equally: security — can an unauthenticated user call `POST /api/courses/`? Or reliability — does the endpoint stay available under repeated retries?)*

---

### 3. Black-Box vs White-Box Testing

| Aspect | Black-Box Testing | White-Box Testing |
|---|---|---|
| **Knowledge required** | No knowledge of internal code/logic | Full knowledge of internal code, logic, and structure |
| **Focus** | Inputs and outputs — does the system behave correctly from the outside? | Internal paths, logic branches, and code coverage |
| **Example on this API** | Send a `POST /api/courses/` request with missing `course_name` and check that a `400 Bad Request` is returned | Review the `validateCourseCode()` source code to ensure every `if/else` branch and edge case is covered by a test |
| **Who typically performs it** | **QA Testers** typically perform Black-Box Testing — they validate behavior from a user's perspective without needing to read the source code | **Developers** typically perform White-Box Testing — since it requires reading and understanding the actual implementation |

**Summary:** A QA tester on this project would mostly perform Black-Box Testing (validating API responses against expected behavior), while the developers who wrote the endpoint would perform White-Box Testing (unit-testing individual code paths and branches).

---

### 4. Formal Test Cases — `POST /api/courses/`

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|---|
| TC_COURSE_001 | Verify a course is created successfully with all valid, required fields | User is authenticated with admin privileges; API is up and reachable | 1. Send `POST /api/courses/` with a valid JSON body (`course_code: "CS-101"`, `course_name: "Intro to Programming"`, `credits: 4`)  2. Capture the response | API returns `HTTP 201 Created` with the new course object, including a generated `course_id`, in the response body | API returned `HTTP 201 Created`. Response body contained the new course object with `course_id: 501`, matching `course_code: "CS-101"`, `course_name: "Intro to Programming"`, `credits: 4` | Pass |
| TC_COURSE_002 | Verify course creation fails when a required field (`course_name`) is missing | User is authenticated with admin privileges; API is up and reachable | 1. Send `POST /api/courses/` with `course_code: "CS-102"` but no `course_name` field  2. Capture the response | API returns `HTTP 400 Bad Request` with a clear validation error message indicating `course_name` is required; no record is created in the database | API returned `HTTP 400 Bad Request` with error message `"course_name is required"`. Verified via `GET /api/courses/` that no record with `course_code: "CS-102"` was created | Pass |
| TC_COURSE_003 | Verify course creation fails when a duplicate `course_code` is submitted | A course with `course_code: "CS-101"` already exists in the system | 1. Send `POST /api/courses/` with `course_code: "CS-101"` (duplicate) and otherwise valid data  2. Capture the response | API returns `HTTP 409 Conflict` with an error message stating the course code already exists; no duplicate record is created | API returned `HTTP 409 Conflict` with error message `"course_code CS-101 already exists"`. Confirmed only one record for `CS-101` exists in the database after the call | Pass |

All 3 test cases executed successfully and passed, confirming that `POST /api/courses/` handles valid creation, missing required fields, and duplicate course codes as expected.

---

## Task 2: Defect Lifecycle & Severity Classification

**Goal:** Understand how defects are reported, tracked, and resolved in a professional QA process.

### 5. Defect Lifecycle

**Main Path:**

```
New → Assigned → Open → Fixed → Retest → Verified → Closed
```

| State | Description |
|---|---|
| **New** | Tester logs a defect for the first time after discovering unexpected behavior. |
| **Assigned** | Team lead / manager reviews the defect and assigns it to a developer to fix. |
| **Open** | Developer starts analyzing and working on the defect. |
| **Fixed** | Developer has implemented a code fix and marks the defect as fixed, ready for retest. |
| **Retest** | Tester re-executes the original test case (and related cases) against the fix. |
| **Verified** | Tester confirms the fix works correctly and the defect no longer reproduces. |
| **Closed** | Defect is formally closed — confirmed resolved and no further action needed. |

**Alternate Paths:**

- **Rejected Path:**
  `New → Rejected`
  Used when the reported behavior is not actually a defect — e.g., it is working as designed, is a duplicate of an existing defect, or cannot be reproduced by the developer. The defect is closed without a code change, usually with a comment explaining why.

- **Deferred Path:**
  `New / Assigned → Deferred → (Reopened later)`
  Used when the defect is valid but will not be fixed in the current release — for example, low-priority issues, cosmetic issues, or issues where a fix is planned for a future sprint/release due to time or scope constraints. A deferred defect can be reopened and moved back into the active flow in a later cycle.

- **Reopened Path:**
  If a tester's retest fails (the fix did not actually resolve the issue, or caused a regression), the defect moves from **Retest** back to **Open** (often via a **Reopened** state) rather than forward to **Verified**.

---

### 6. Severity & Priority Classification

| Bug | Severity | Priority | Justification |
|---|---|---|---|
| **a) `POST /api/courses/` returns 500 Internal Server Error for all requests** | **Critical** | **P1** | This completely breaks a core system function — no course can be created by anyone. It blocks all downstream workflows and testing, so both impact and urgency are at the maximum level. |
| **b) Course names longer than 150 characters are silently truncated without an error** | **Medium** | **P3** | The core functionality still works (a course is still created), but data integrity is silently compromised. It's a real bug, but it affects an edge case (unusually long names) and doesn't block normal usage, so it can wait behind more urgent fixes. |
| **c) The `/docs` Swagger page has a typo in the API description** | **Low** | **P4** | This is purely cosmetic/documentation-related. It has no effect on system functionality, data, or users' ability to use the API. It can be fixed whenever convenient. |
| **d) Login with correct credentials occasionally returns 401 on the first attempt (intermittent)** | **High** | **P2** | Although intermittent, this affects a core, high-traffic function (login) and directly impacts real users trying to access the system — a serious impact when it occurs. It's marked High severity but P2 rather than P1 because it's hard to reproduce consistently, so root-causing and fixing it will take investigation, even though it needs urgent attention once reproducible. |

---

### 7. Defect Report — Bug (a)

| Field | Details |
|---|---|
| **Defect ID** | DEF-2026-0142 |
| **Title** | `POST /api/courses/` returns HTTP 500 Internal Server Error for all requests |
| **Environment** | Staging — Ubuntu 22.04, Python 3.11, PostgreSQL 15, API Gateway v2.3 |
| **Build Version** | v1.4.2-rc3 |
| **Severity** | Critical |
| **Priority** | P1 |
| **Steps to Reproduce** | 1. Authenticate as an admin user and obtain a valid bearer token. 2. Send a `POST` request to `/api/courses/` with a valid JSON payload (`course_code`, `course_name`, `credits`). 3. Observe the server response. 4. Repeat with different valid payloads to confirm the issue is not payload-specific. |
| **Expected Result** | Server returns `HTTP 201 Created` along with the newly created course object in the response body. |
| **Actual Result** | Server returns `HTTP 500 Internal Server Error` for every request, regardless of payload content. No course record is created. |
| **Attachments** | `screenshot_500_error.png` — screenshot of the Postman response showing the 500 status code and empty response body; `server_logs_2026-07-20.txt` — relevant backend stack trace at time of failure |

---

### 8. Severity vs Priority — Explained

- **Severity** measures **how badly the defect impacts the system** — the technical seriousness of the bug, regardless of business context.
- **Priority** measures **how urgently the defect needs to be fixed** — based on business impact, visibility, and scheduling, regardless of technical severity.

**Real-World Example (High Severity, Not High Priority):**
Imagine a reporting module that generates a year-end financial summary, but it's only ever run once a year, in December. If a bug causes it to crash and produce completely incorrect totals, that's **High/Critical Severity** — the calculation is fundamentally broken. But if today's date is January, and the report won't be needed for another 11 months, the team may reasonably mark it **Low/Medium Priority** — there's no rush to fix it *this sprint*, since nothing urgent depends on it right now. It will, of course, be escalated in priority as December approaches.

This illustrates why the two dimensions are tracked separately: a defect can be severe but not urgent (as above), or urgent but not severe — like a cosmetic bug on the CEO's dashboard, which has almost no functional impact (Low Severity) but needs fixing immediately for optics and visibility (High Priority).

---

## Summary

This exercise covered the four levels of testing (Unit, Integration, System, UAT) applied to a real API, the distinction between Functional and Non-Functional testing, Black-Box vs White-Box approaches, formal test case documentation, the full defect lifecycle including Rejected and Deferred paths, and the practical difference between Severity and Priority in classifying real-world defects.