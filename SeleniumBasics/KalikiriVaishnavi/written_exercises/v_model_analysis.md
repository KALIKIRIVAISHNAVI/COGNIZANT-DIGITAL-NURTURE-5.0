# SDLC vs TDLC — V-Model & Agile QA Integration
### Hands-On 2 — Submission

---

## Task 1: V-Model Mapping

**Goal:** Create a complete V-Model diagram mapping each SDLC phase to its corresponding TDLC phase.

### 9. The V-Model — Course Management API

The V-Model places development phases on the left (descending) side and their corresponding testing phases on the right (ascending) side, joined at the bottom by Coding — visually forming a "V".

```
   SDLC (Left / Down)                          TDLC (Right / Up)

   Requirements  ─────────────────────────▶   Acceptance Testing
        │                                             ▲
        ▼                                             │
   System Design  ────────────────────────▶   System Testing
        │                                             ▲
        ▼                                             │
   Architecture Design  ───────────────────▶  Integration Testing
        │                                             ▲
        ▼                                             │
   Module Design  ─────────────────────────▶  Unit Testing
        │                                             ▲
        └──────────────────▶  Coding  ────────────────┘
```

Each horizontal line represents a direct relationship: the development artifact produced on the left defines exactly what will be verified on the right, at the same level.

---

### 10. SDLC Phase → TDLC Phase → Artifact Produced

| SDLC Phase (Development) | Corresponding TDLC Phase (Testing) | Artifact Produced During Development Phase |
|---|---|---|
| **Requirements Analysis** | Acceptance Testing | Business Requirements Document (BRD) / User Stories — e.g., "College admin must be able to create, update, and list courses" — used to prepare the **Acceptance Test Plan**. |
| **System Design** | System Testing | High-Level Design (HLD) Document — describes overall system behavior, API contracts, and data flow — used to prepare the **System Test Plan**. |
| **Architecture Design** | Integration Testing | Low-Level Design (LLD) Document — describes how modules (API layer, service layer, database layer) interact — used to prepare the **Integration Test Plan**. |
| **Module Design** | Unit Testing | Detailed function/class-level design specs (e.g., pseudocode for `validateCourseCode()`) — used to prepare the **Unit Test Plan**. |

**Example:** Just as the Requirements phase produces the BRD *before* any code is written, the Acceptance Test Plan is also prepared during that same phase — not after Coding — so that testing artifacts are ready the moment the corresponding development phase completes.

---

### 11. Entry & Exit Criteria — All Four Testing Levels

| Testing Level | Entry Criteria (must be true BEFORE testing begins) | Exit Criteria (must be true BEFORE testing is considered complete) |
|---|---|---|
| **Unit Testing** | Module/function code is complete and compiles; Unit Test Plan and test cases are ready; developer has access to a test environment/framework (e.g., PyTest) | All planned unit test cases executed; code coverage meets the agreed threshold (e.g., ≥80%); no open Critical/High defects in the unit; results documented |
| **Integration Testing** | All individual units/modules to be integrated have passed Unit Testing; Integration Test Plan is ready; test environment with required modules/stubs/mocks is available | All planned integration test cases executed; interfaces between modules (e.g., API layer ↔ database layer) verified as working; no open Critical/High defects; defect count below agreed threshold |
| **System Testing** | Integration Testing is complete and signed off; full system build is deployed to a stable test environment; System Test Plan is ready | All planned system test cases executed, covering full end-to-end flows; no open Critical/High severity defects; system meets functional and non-functional requirements; test summary report signed off |
| **User Acceptance Testing (UAT)** | System Testing is complete and signed off; UAT environment mirrors production; Acceptance Test Plan/criteria are ready; business/end users are available | All acceptance criteria met from the end user's (college admin's) perspective; business stakeholders formally sign off; no open Critical/High defects; system is approved for release |

---

### 12. Two Points Where QA Should Engage Early (Beyond Testing Phases)

1. **During Requirements Analysis (before any code is written):**
   QA should review the requirements documents for the Course Management API — e.g., "a course code must be unique" — and flag ambiguities early. For example, does "unique" mean unique across the whole system, or per department? Catching this kind of ambiguity during requirements review is far cheaper than discovering it after the API is already coded and tested, when a misunderstanding could mean re-doing design, code, and tests.

2. **During System/Architecture Design (before Module Design/Coding begins):**
   QA should participate in design reviews for the API architecture — for example, reviewing how the `POST /api/courses/` endpoint is expected to handle duplicate course codes (409 vs. silent overwrite). By raising testability and edge-case questions at design time, QA ensures the system is being built in a way that's verifiable and that important edge cases are considered before a single line of code is written — rather than being discovered as a defect in System Testing.

---

## Task 2: Agile QA and Shift-Left Testing

**Goal:** Understand how QA integrates into Agile sprints and the Shift-Left principle.

### 13. Problems with Traditional Waterfall Testing (Course Management API)

1. **Late Defect Discovery:** In Waterfall, testing only starts after the entire Course Management API is coded. A fundamental design flaw — such as the API not handling duplicate course codes correctly — might only surface during System Testing, months after the design decision was made, making it expensive and disruptive to fix.

2. **No Fast Feedback Loop:** Since testing happens in one big phase at the end, developers get no feedback on quality until far after they've moved on to other modules. If the `POST /api/courses/` endpoint has a validation bug, the developer who wrote it may have already moved to unrelated work by the time it's reported, making context-switching costly and slow.

3. **Compressed Testing Timeline Under Schedule Pressure:** If development for the Course Management API overruns its schedule (which is common), the testing phase is usually the one that gets squeezed to hit the release date — since it's the last phase before delivery. This leads to rushed, incomplete testing and a higher risk of defects reaching production.

---

### 14. QA's Role in Each Agile Ceremony

| Ceremony | QA's Role |
|---|---|
| **Sprint Planning** | QA works with the Product Owner and dev team to **define acceptance criteria** for each user story before it's committed to the sprint — e.g., clarifying exactly what "successfully create a course" means for the Course Management API, including edge cases. |
| **Daily Standup** | QA reports testing progress and **flags blocking issues** — e.g., "I can't test the course creation story because the staging API is returning 500 errors" — so the team can react immediately instead of losing days. |
| **Sprint Review** | QA helps **demo tested functionality** to stakeholders, confirming that what's being shown has actually been verified against the acceptance criteria, not just "looks like it works." |
| **Retrospective** | QA contributes to **process improvement** discussions — e.g., suggesting that test data setup should be automated because it slowed testing down this sprint, or that acceptance criteria need to be written earlier. |

---

### 15. Four Shift-Left Practices for the Course Management API

Shift-Left means moving testing activities **earlier** in the SDLC, rather than waiting until code is complete.

**(a) Reviewing Requirements for Testability**
Before development starts, QA reviews user stories like "Admin can create a course" and asks testability questions: What are the valid/invalid inputs for `course_code`? What HTTP status should be returned on failure? This ensures requirements are precise enough to test against, and catches ambiguity before it becomes a coded assumption.

**(b) Writing Test Cases Before Code (TDD/BDD)**
Test cases (or even automated test scripts) for `POST /api/courses/` are written based on the acceptance criteria *before* the developer writes the implementation. The developer then codes against these tests, which immediately clarifies expected behavior and catches deviations the moment code is written, rather than in a later testing phase.

**(c) Static Code Analysis**
Tools (e.g., linters, SonarQube) automatically scan the Course Management API's codebase for code smells, security vulnerabilities, and style violations as soon as code is committed — long before it ever reaches a QA environment, catching classes of bugs without needing to execute the application at all.

**(d) API Contract Testing Before Integration**
Before the Course Management API is integrated with consumer services (e.g., a front-end or a scheduling service), its contract (request/response schema, status codes) is validated against an agreed specification (e.g., OpenAPI/Swagger spec). This confirms the API honors its contract *before* another team builds against it, preventing integration failures from being discovered late.

---

### 16. Acceptance Criteria — Given-When-Then (Gherkin)

**User Story:** As a college admin, I want to create a new course, so that students can enroll in it.

```gherkin
Feature: Course Creation

  Scenario: Successfully create a new course (Happy Path)
    Given I am logged in as a college admin
    And the course code "CS-101" does not already exist
    When I submit a request to create a course with a valid course code, name, and credits
    Then the course should be created successfully
    And the response should return HTTP 201 Created
    And the new course should appear in the course catalog

  Scenario: Reject creation with a duplicate course code
    Given I am logged in as a college admin
    And a course with the code "CS-101" already exists
    When I submit a request to create a course using the course code "CS-101"
    Then the course should not be created
    And the response should return HTTP 409 Conflict
    And an error message should indicate the course code already exists

  Scenario: Reject creation when required fields are missing
    Given I am logged in as a college admin
    When I submit a request to create a course without providing a course name
    Then the course should not be created
    And the response should return HTTP 400 Bad Request
    And an error message should indicate that the course name is required
```

This acceptance criteria is written directly in Given-When-Then format so it can be executed as automated tests using BDD tools like **Behave** (Python) or **Cucumber** (Java/JS) — meaning QA and developers can collaborate on the exact same artifact, from requirement to automated test, with no translation gap between them.

---

## Summary

This exercise mapped the complete V-Model for the Course Management API — connecting each SDLC phase to its corresponding TDLC phase, documenting the artifacts produced at each stage, and defining entry/exit criteria across all four testing levels. It also identified two points for QA to engage before formal testing begins. On the Agile side, it examined three real problems with Waterfall testing, defined QA's role across all four Agile ceremonies, outlined four concrete Shift-Left practices, and expressed acceptance criteria in executable Given-When-Then format — reinforcing that Shift-Left is about early collaboration between QA and developers, not about developers testing alone.