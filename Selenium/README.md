# Digital Nurture 5.0 — QA Concepts & Selenium Basics
### Python Full Stack Engineer Track | Hands-On Exercise Submission

This repository contains solutions for the 7 hands-on exercises of the QA
Concepts & Test Automation module — beginning with QA theory and the
testing lifecycle, moving through test automation strategy, and culminating
in a full Selenium WebDriver + pytest + Page Object Model automation suite.

**Practice application used for all Selenium exercises:**
[LambdaTest Selenium Playground](https://www.lambdatest.com/selenium-playground/)
— chosen because it requires no login, is always available, and exposes
forms, checkboxes, dropdowns, alerts, and tables covering every major
Selenium interaction pattern.

**Tech stack:** Python 3.10+, Selenium WebDriver, webdriver-manager, pytest,
pytest-html, Chrome/ChromeDriver.

---

## Repository Structure

```
Selenium
├── qa_concepts.md          # Hands-On 1
├── v_model_analysis.md     # Hands-On 2
└── automation_strategy.md  # Hands-On 3
├── HandsOn-4/
│   ├── setup_test.py
│   └── task2.py
├── HandsOn-5/
│   ├── task1_locators.py
│   └── task2_waits.py
├── HandsOn-6/
│   ├── conftest.py
│   └── test_playground.py
└── HandsOn-7/
├── pages/
│   ├── base_page.py
│   ├── simple_form_page.py
│   ├── checkbox_page.py
│   ├── dropdown_page.py
│   └── input_form_page.py
└── tests/
│   └── test_playground_pom.py
├── requirements.txt
└── README.md
```

---

## Difficulty Guide

| Level | Hands-On | What to Expect |
|---|---|---|
| Beginner | 1, 2 | QA concepts, defect lifecycle, SDLC vs TDLC |
| Intermediate | 3, 4, 5 | Test automation theory, Selenium setup, locators |
| Advanced | 6, 7 | Selenium waits, pytest integration, Page Object Model |

---

## Hands-On 1 — QA Concepts, Functional Testing & Defect Lifecycle
**Level:** Beginner | **Type:** Written Exercise | **Submission:** `written_exercises/qa_concepts.md`

**Topics covered:** QA roles & responsibilities · functional vs
non-functional testing · test levels (unit, integration, system, UAT) ·
black-box vs white-box testing · defect lifecycle & management · test case
writing.

**Task 1 — Map Testing Types to a Real System**
Applied to the Course Management API:
- Wrote one concrete test case for each test level: a **unit test** for a
  single function in isolation, an **integration test** for the API
  endpoint working with the database, a **system test** covering the full
  request → database round trip, and a **UAT** scenario written from a
  college admin's perspective.
- Classified each case as **Functional** ("does it do what it should?") or
  **Non-Functional** ("how well does it do it?"), with a performance/
  security/reliability example for the non-functional case.
- Explained **black-box** (no knowledge of internal code — typically the QA
  tester's job) vs **white-box** testing (code-aware — typically the
  developer's job).
- Wrote 3 formal test cases for `POST /api/courses/` in a table with
  columns: Test Case ID, Description, Preconditions, Test Steps, Expected
  Result, Actual Result, Pass/Fail.

**Task 2 — Defect Lifecycle & Severity Classification**
- Documented the full defect lifecycle: **New → Assigned → Open → Fixed →
  Retest → Verified → Closed**, plus the **Rejected** and **Deferred**
  branch paths.
- Classified 4 hypothetical API bugs by **Severity** (Critical/High/Medium/
  Low) and **Priority** (P1–P4) — including a 500 error on all requests, a
  silent truncation bug, a cosmetic Swagger typo, and an intermittent 401
  on login — with justification for each.
- Wrote a full defect report for the 500-error bug using standard fields
  (Defect ID, Title, Environment, Build Version, Severity, Priority, Steps
  to Reproduce, Expected/Actual Result, Attachments).
- Explained **Severity vs Priority** with a real example where high
  severity does not imply high priority (and vice versa).

**Key takeaway:** Severity measures impact on the system; Priority measures
urgency to fix. A cosmetic bug on an executive's dashboard can be Low
Severity but High Priority.

---

## Hands-On 2 — SDLC vs TDLC — V-Model & Agile QA Integration
**Level:** Beginner | **Type:** Written Exercise | **Submission:** `written_exercises/v_model_analysis.md`

**Topics covered:** SDLC phases · TDLC phases · V-Model mapping · entry &
exit criteria · Agile QA integration · Shift-Left testing.

**Task 1 — V-Model Mapping**
- Drew the V-Model: left side (Requirements → System Design → Architecture
  Design → Module Design → Coding) mapped against the right side
  (Acceptance → System → Integration → Unit Testing), meeting at Coding.
- Documented the test artifact produced at each development phase (e.g.
  Requirements phase → Acceptance Test plan drafted in parallel).
- Defined **Entry** and **Exit Criteria** for all four testing levels.
- Identified two points in the V-Model where QA should engage *before* the
  testing phases begin — e.g. reviewing requirements for ambiguity, which
  is far cheaper than catching the same issue during system testing.

**Task 2 — Agile QA and Shift-Left Testing**
- Listed 3 problems caused by testing-after-development in a traditional
  Waterfall approach to the Course Management API.
- Described the QA engineer's role in each Agile ceremony: **Sprint
  Planning** (defining acceptance criteria), **Daily Standup** (surfacing
  blockers), **Sprint Review** (demo testing), **Retrospective** (process
  improvement).
- Detailed 4 Shift-Left practices applied to the API: testability review of
  requirements, TDD/BDD (tests before code), static code analysis, and API
  contract testing before integration.
- Wrote **Given-When-Then** acceptance criteria for "As a college admin, I
  want to create a new course" — covering the happy path, duplicate course
  code, and missing required fields.

**Key takeaway:** Shift-Left doesn't mean developers do all the testing —
it means QA and developers collaborate earlier to *prevent* defects instead
of just finding them later.

---

## Hands-On 3 — Test Automation Process, Lifecycle & Framework Types
**Level:** Intermediate | **Type:** Written Exercise | **Submission:** `written_exercises/automation_strategy.md`

**Topics covered:** when to automate · automation test lifecycle · test
case selection · framework types (Linear, Modular, Data-Driven,
Keyword-Driven, Hybrid) · automation ROI.

**Task 1 — Automation Decision and Test Case Selection**
- Listed and applied 5 criteria for deciding whether to automate a test,
  using `POST /api/courses/` returning 201 as the running example.
- Classified 6 Course Management API test cases as **Automate** or
  **Manual** (regression suite, exploratory search testing, 100-concurrent-
  user performance test, login UI test, Swagger accuracy check, deployment
  smoke test) with justification for each.
- Defined **automation ROI** and calculated the break-even point: automating
  a regression test takes 4 hours vs 30 minutes manually, with a 20%
  maintenance overhead applied after the 10th run.
- Defined a **flaky test**, gave a concrete example, and listed 3
  mitigation strategies (e.g. explicit waits over sleeps, isolating test
  data, retry-with-diagnostics rather than blind retries).

**Task 2 — Compare Automation Framework Types**
- Compared all 5 framework architectures (Linear, Modular, Data-Driven,
  Keyword-Driven, Hybrid) — one paragraph description, one advantage, one
  disadvantage, and a usage example for each, applied to the Course
  Management system.
- Recommended a framework combination for a scenario requiring 50
  username/password combinations, reusable login steps across 20 tests, and
  support for both technical and non-technical contributors — landing on a
  **Hybrid (Data-Driven + Modular)** approach.
- Designed the folder structure for a Hybrid framework: test data files,
  page object files, utility files, test files, and configuration.

**Key takeaway:** Good automation candidates are repetitive, high-risk,
regression-prone, and data-driven. Poor candidates are exploratory,
UI-heavy, one-time, or rapidly-changing tests — automating those burns more
time in maintenance than it saves.

---

## Hands-On 4 — Selenium WebDriver Setup, Browser Drivers & Basic Commands
**Level:** Intermediate | **Type:** Coding Exercise | **Scripts:** `automation_scripts/HandsOn-4/`

**Topics covered:** Selenium architecture (WebDriver / Grid / IDE) ·
ChromeDriver setup · `webdriver-manager` for automatic driver management ·
WebDriver commands (navigate, get, close, quit) · window & frame handling ·
screenshots.

**Install:** `pip install selenium webdriver-manager`

### Task 1 — Selenium Architecture and Environment Setup (`setup_test.py`)
- Documented the three core Selenium components in a header comment:
  **WebDriver** (talks directly to the browser via the browser's native
  driver), **Selenium Grid** (enables parallel execution across multiple
  machines/browsers), and **Selenium IDE** (record-and-playback + code
  generation for quick script scaffolding).
- Installed Selenium and `webdriver-manager`, then wrote a minimal script
  that imports `ChromeDriverManager`, launches Chrome, navigates to the
  Selenium Playground, prints the page title, and quits.
- Added `driver.implicitly_wait(10)` and documented in a comment why a
  *global* implicit wait is discouraged versus scoped explicit waits (it
  silently slows every `find_element` call and can mask genuine timing
  bugs).
- Converted the script to headless mode via
  `options.add_argument('--headless')` and confirmed the title still prints
  with no visible browser window.

![Hands-On 4 Task 1 — setup_test.py running in VS Code](screenshots/ho4_t1_setup_test.png)
*`setup_test.py` — Chrome driver auto-installed via `ChromeDriverManager().install()`, headless option applied, implicit wait set, and page title ("Selenium Grid Online | Run Selenium Test On Cloud") printed to the terminal.*

### Task 2 — WebDriver Navigation and Window Commands (`task2.py`)
- Navigated from the Playground home to the Simple Form Demo page and
  asserted the URL contains `simple-form-demo`, then navigated back with
  `driver.back()`.
- Opened a second tab via `driver.execute_script('window.open(...)')`,
  listed handles with `driver.window_handles`, and switched to the new tab
  with `driver.switch_to.window(driver.window_handles[1])` to print the
  Google tab's title.
- Switched back to the original tab and saved a screenshot with
  `driver.save_screenshot('playground_screenshot.png')`.
- Demonstrated `get_window_size()` / `set_window_size(1280, 800)`, noting in
  comments why a consistent viewport matters for responsive-UI automation
  (locators and layouts can shift at different breakpoints).

![Hands-On 4 Task 2 — task2.py terminal output](screenshots/ho4_t2_task2_terminal.png)
*`task2.py` — second tab opened and switched to, "Google" printed as the tab title, window size confirmed as `{'width': 1051, 'height': 798}` after `set_window_size`.*

![Hands-On 4 Task 2 — Selenium Playground in browser](screenshots/ho4_t2_playground_browser.png)
*Automated Chrome session (banner: "Chrome is being controlled by automated test software") on the Selenium Playground home page, listing all available practice components.*

---

## Hands-On 5 — Locators & Explicit Waits
**Level:** Intermediate | **Type:** Coding Exercise | **Scripts:** `automation_scripts/HandsOn-5/`

**Topics covered:** locator strategies (ID, Name, Class, Tag, XPath, CSS) ·
writing robust XPath · CSS selector patterns · `WebDriverWait` & expected
conditions · implicit vs explicit vs fluent waits · avoiding hard-coded
`sleep()`.

### Task 1 — Locator Strategies, Simple to Robust (`task1_locators.py`)
- On the Simple Form Demo message input, located the same element 6 ways:
  `By.ID`, `By.NAME`, `By.CLASS_NAME`, `By.TAG_NAME`, absolute `By.XPATH`,
  and relative `By.XPATH` — logging pass/fail for each.
- Wrote 3 CSS selector variants for the same element: by ID (`#id`), by
  attribute (`[name='value']`), and by parent-child relationship
  (`div > input`).
- On the Checkbox Demo, used `//label[text()='Option 1']` for an exact-text
  match and `//label[contains(text(),'Option')]` to match all option
  labels (verified count = 8).
- Ranked all 6 strategies from most to least preferred, with justification
  based on uniqueness, brittleness to markup changes, and readability.

![Hands-On 5 Task 1 — locator strategy results](screenshots/ho5_t1_locators_terminal.png)
*`task1_locators.py` — `By.ID` found (True), `By.NAME`/`By.CLASS_NAME` not present on this element (False), relative XPath found (True) while absolute XPath failed after a DOM change, CSS-by-ID and CSS-by-tag+id both found, `contains()` matched all 8 checkbox options, and the full preference ranking is printed: **1. ID → 2. Name → 3. CSS Selector → 4. Class Name → 5. Relative XPath → 6. Absolute XPath** (least preferred — it hardcodes the full DOM path and breaks on any structural change).*

### Task 2 — WebDriverWait and Expected Conditions (`task2_waits.py`)
- On the Bootstrap Alerts demo, clicked "Success Message" then waited with
  `WebDriverWait(driver, 10).until(EC.visibility_of_element_located(...))`
  and asserted the alert text contains "successfully."
- Timed the same test using `time.sleep(3)` vs an explicit wait to
  demonstrate the reliability/speed tradeoff.
- Added `EC.element_to_be_clickable()` before clicking, with a comment
  distinguishing it from `visibility_of_element_located` (visible **and**
  enabled **and** not obscured, vs merely present/visible in the DOM).
- Implemented a **FluentWait** — 500ms polling interval, 10s timeout,
  ignoring `NoSuchElementException` — to wait for a dynamically-loaded
  table row.

![Hands-On 5 Task 2 — Bootstrap Alert Messages demo](screenshots/ho5_t2_bootstrap_alerts.png)
*Bootstrap Alerts page ("Autoclosable Success Message", "Normal Success Message", etc.) used to validate `visibility_of_element_located` and `element_to_be_clickable` waits against the live alert banner.*

**Terminal evidence (also shown in Hands-On 6 Task 1 screenshot below, same script):**
`time.sleep(3)` took **4.01s** vs the explicit wait's **1.28s** — a concrete
demonstration that explicit waits proceed as soon as the condition is met
instead of always burning the full sleep duration.

---

## Hands-On 6 — Running Selenium Tests with pytest
**Level:** Advanced | **Type:** Coding Exercise | **Scripts:** `automation_scripts/HandsOn-6/`

**Topics covered:** pytest test discovery & fixtures · `conftest.py` shared
fixtures · pytest assertions · parameterised tests · HTML reports ·
screenshot-on-failure.

**Install:** `pip install pytest pytest-html`

### Task 1 — Organise Scripts into pytest Tests
- Renamed script functions to `test_*` so pytest auto-discovers them:
  `test_simple_form_submission()`, `test_checkbox_interaction()`.
- Created `conftest.py` with a **function-scoped** `driver` fixture
  (`@pytest.fixture(scope='function')`) that initialises Chrome, `yield`s
  the driver to the test, and calls `driver.quit()` in teardown — every
  test receives the driver via parameter injection rather than creating its
  own instance.
- `test_simple_form_submission(driver)`: enters "Hello Selenium," submits,
  waits for the display element, and asserts the message matches exactly.
- `test_checkbox_demo(driver)`: clicks the first checkbox, asserts
  `is_selected()`, clicks again, asserts it's deselected.
- Verified with `pytest test_playground.py -v` that both tests pass with
  clean setup/teardown per test.

![Hands-On 6 Task 1 — explicit wait timing comparison](screenshots/ho6_t1_waits_terminal.png)
*`task2_waits.py` output carried into this stage — Step 36: alert text confirms "successfully" (PASS). Step 37: `time.sleep(3)` (4.01s) vs explicit wait (1.28s). Step 38: element confirmed clickable before the click fires. Step 39: FluentWait correctly times out when no table row loads within 10s of 500ms polling.*

![Hands-On 6 Task 1 — first pytest run](screenshots/ho6_t2_pytest_initial_run.png)
*`pytest -v test_playground.py` — **2 passed** (`test_simple_form_submission`, `test_checkbox_interaction`), each run through the shared `driver` fixture from `conftest.py`.*

### Task 2 — Parameterisation, Reporting & Screenshot-on-Failure
- Parameterised the form submission test with 3 values via
  `@pytest.mark.parametrize('message', ['Hello', 'Selenium Automation',
  '12345'])` — each value runs and reports as a separate test case.
- Added a `pytest_runtest_makereport` hook in `conftest.py` that inspects
  `request.node.rep_call.failed` and calls
  `driver.save_screenshot(f'{test_name}_failure.png')` on failure.
- Generated a self-contained HTML report:
  `pytest test_playground.py --html=report.html --self-contained-html`.
- Added a **session-scoped** `base_url` fixture
  (`'https://www.lambdatest.com/selenium-playground/'`) and refactored all
  tests to use it instead of hardcoded URLs.
- Added `test_dropdown_selection(driver)` using
  `Select(driver.find_element(...))` to choose "Wednesday" and assert the
  selected option text.

![Hands-On 6 Task 2 — parameterised suite, 5 passed](screenshots/ho6_t2_pytest_parametrized_run.png)
*Full suite after parameterisation — **5 passed**: `test_simple_form_submission[Hello]`, `[Selenium Automation]`, `[12345]`, plus `test_checkbox_interaction` and `test_dropdown_selection`, each shown individually in the pytest output.*

![Hands-On 6 Task 2 — HTML report generated](screenshots/ho6_t2_html_report.png)
*`pytest test_playground.py --html=report.html --self-contained-html` — **5 passed in 27.73s**, `report.html` generated at the project root with pass/fail status and duration per test.*

**Key takeaway:** `scope='function'` gives full test isolation with a fresh
browser per test (slower); `scope='session'` reuses one browser across all
tests (faster, but risks cross-test interference). The `yield` in a fixture
splits setup (before) from teardown (after) — the pytest equivalent of
`setUp`/`tearDown`.

---

## Hands-On 7 — Page Object Model (POM)
**Level:** Advanced | **Type:** Coding Exercise | **Scripts:** `automation_scripts/HandsOn-7/`

**Topics covered:** POM design principles · creating page classes ·
locator management in page classes · separating test logic from UI logic ·
reusability & maintainability · refactoring flat scripts to POM.

### Task 1 — Build Page Classes
- Created `pages/base_page.py` with a `BasePage` class: accepts the driver
  in `__init__` and exposes `navigate_to(url)`, `get_title()`, and
  `wait_for_element(locator, timeout=10)`. Also added a `safe_click()`
  helper that waits for clickability, scrolls the element into view, and
  falls back to a JS click if a normal click is intercepted.
- Created `simple_form_page.py` (`SimpleFormPage(BasePage)`) with locators
  as **class-level tuples** (e.g. `MESSAGE_INPUT = (By.ID,
  'user-message')`) — never hardcoded inside methods.
- Added interaction methods `enter_message(text)`, `click_submit()`, and
  `get_displayed_message()` — none contain `assert` statements; page
  methods only act and return values.
- Created `checkbox_page.py` (`CheckboxPage`) with `check_option(index)`,
  `uncheck_option(index)`, `is_option_checked(index)`.
- Created `dropdown_page.py` (`DropdownPage`) with `select_day(day_name)`
  using the `Select` class internally.

**Golden rule applied throughout:** test files contain **assertions**
(what should happen); page files contain **interactions** (how to make it
happen). No `driver.find_element` calls appear in any test file.

### Task 2 — Refactor Tests to POM and Build the Full Suite
- Refactored `test_simple_form_submission` to drive everything through
  `SimpleFormPage`: `page.navigate_to(...)`, `page.enter_message(...)`,
  `page.click_submit()`, `assert page.get_displayed_message() == '...'`.
- Refactored `test_checkbox_demo` → `CheckboxPage` and
  `test_dropdown_selection` → `DropdownPage`.
- Added `InputFormPage` and `test_input_form_submit(driver)` for the Input
  Form Submit page (name, email, phone, address fields), with page methods
  `fill_form(...)`, `submit_form()`, and `get_success_message()`.
- Ran the complete suite: `pytest tests/ -v --html=report.html
  --self-contained-html`.
- Documented in the README/code comments what would break in a **flat,
  non-POM** script if the Submit button's ID changed from `submit` to
  `btn-submit`: every test file with a hardcoded `driver.find_element(By.ID,
  'submit')` call would fail, requiring find-and-replace across the entire
  suite. With POM, only the single locator tuple in the page class needs
  updating.

![Hands-On 7 — POM-based test suite passing](screenshots/ho7_t1_pom_pytest_run.png)
*`pytest -m pytest -v test_playground_pom.py` — **5 passed in 106.54s**, all tests driven entirely through Page Object methods (`page.enter_message()`, `page.click_submit()`, `page.get_displayed_message()`, etc.) with zero direct `driver.find_element` calls inside the test file.*

![Hands-On 7 — final suite with README and HTML report](screenshots/ho7_t2_readme_final_report.png)
*Final `tests/` suite run as `pytest tests/ -v --html=report.html --self-contained-html` — **5 passed in 102.52s**, `report.html` generated, and `Readme.md` documenting the POM maintainability rationale (locator-change resilience) alongside the passing test list (`test_checkbox_interaction`, `test_dropdown_selection`, `test_simple_form_submission[Hello]`, `[Selenium Automation]`, `[12345]`).*

**Key takeaway:** POM is the single highest-leverage pattern in Selenium
automation — it converts brittle, HTML-coupled scripts into suites that
read like business requirements (`page.enter_message('Hello')`) and
survive UI changes with a one-line locator update.

---

## Setup & Run Instructions

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run an individual script (Hands-On 4/5)
python automation_scripts/HandsOn-4/setup_test.py
python automation_scripts/HandsOn-4/task2.py
python automation_scripts/HandsOn-5/task1_locators.py
python automation_scripts/HandsOn-5/task2_waits.py

# 3. Run the pytest suite (Hands-On 6)
cd automation_scripts/HandsOn-6
pytest -v test_playground.py --html=report.html --self-contained-html

# 4. Run the POM-refactored suite (Hands-On 7)
cd automation_scripts/HandsOn-7
pytest tests/ -v --html=report.html --self-contained-html
```

**requirements.txt**
```
selenium
pytest
pytest-html
webdriver-manager
```

---

## Key Takeaways Across the Module

- **Severity ≠ Priority** — impact on the system vs urgency to fix; they
  don't always move together.
- **Shift-Left testing** means QA engages during requirements and design,
  not just after code is written — catching issues when they're cheapest
  to fix.
- **Automate deliberately** — repetitive, high-risk, regression-prone tests
  are good candidates; exploratory and rapidly-changing UI tests often
  aren't worth the maintenance cost.
- **Locator strategy matters** — prefer `ID` → `Name` → `CSS Selector` over
  `XPath`, and avoid absolute XPath entirely; it hardcodes the full DOM
  path and breaks on any structural change.
- **Explicit waits beat `time.sleep()`** — faster on fast machines, more
  reliable on slow ones, and tied to the actual condition (visibility,
  clickability) rather than a guessed duration.
- **pytest fixtures** cleanly separate setup/teardown from test logic;
  `scope='function'` isolates tests at the cost of a fresh browser each
  time, while `scope='session'` trades isolation for speed.
- **Page Object Model** turns a fragile script into a maintainable suite —
  when the UI changes, one locator in one page class gets updated instead
  of every test file that touches that element.
