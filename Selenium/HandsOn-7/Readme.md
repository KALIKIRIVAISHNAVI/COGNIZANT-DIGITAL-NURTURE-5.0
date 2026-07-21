# Hands-On 7 — Page Object Model

## Project structure

```
HandsOn-7/
├── conftest.py                  # shared fixtures: driver, base_url, screenshot-on-failure hook
├── pages/
│   ├── __init__.py
│   ├── base_page.py             # shared navigate/wait/click helpers
│   ├── simple_form_page.py
│   ├── checkbox_page.py
│   ├── dropdown_page.py
│   └── input_form_page.py
└── tests/
    └── test_playground_pom.py   # test logic + assertions only, zero driver.find_element calls
```

Run the full suite:

```powershell
python -m pytest tests/ -v --html=report.html --self-contained-html
```

Verify zero direct Selenium calls in test files:

```powershell
grep -rn "find_element" tests/
```
(should print nothing)

## Step 59 — Why POM matters when a locator changes

**Question:** What problem would occur in a flat (non-POM) script if the Submit
button's ID changed from `'submit'` to `'btn-submit'`? How does POM solve this?

**Answer:**

In a flat script, `driver.find_element(By.ID, 'submit').click()` is typically
written inline, directly inside every test function that needs to submit that
form. If the site changes the button's ID, **every single test function that
contains that exact string breaks at the same time**, and to fix it you have
to:

1. Search the entire test suite for every occurrence of `'submit'` used as a
   locator (not just as a variable name or an unrelated string — a plain
   text search isn't even reliable here).
2. Edit each occurrence individually, in every test file that happens to
   submit that form.
3. Hope you didn't miss one, because a missed occurrence doesn't fail until
   that specific test runs — possibly much later, and possibly reported as
   an unrelated-looking `NoSuchElementException` with no obvious connection
   to "the ID changed."

This is exactly the kind of breakage we hit repeatedly earlier in this
project (`user-message`, absolute XPath, the tag-name assumption) — a single
markup change rippling out and silently breaking tests in multiple places.

**With POM, the locator exists in exactly one place**: the class-level
constant `SUBMIT_BTN = (By.ID, 'submit')` inside the relevant page class
(e.g. `SimpleFormPage`). When the ID changes, there is exactly **one line to
edit** — the constant itself — and every test that calls `page.click_submit()`
picks up the fix automatically, with no changes needed in any test file.

This is also why a properly POM-compliant test reads like a business
requirement instead of HTML interaction code:

```python
# Test file — reads like a requirement:
page.enter_message('Hello')
page.click_submit()
assert page.get_displayed_message() == 'Hello'
```

```python
# vs. flat script — reads like HTML interaction code, and breaks everywhere
# the moment 'user-message' or 'submit' changes:
driver.find_element(By.ID, 'user-message').send_keys('Hello')
driver.find_element(By.ID, 'submit').click()
assert driver.find_element(By.ID, 'message').text == 'Hello'
```

POM doesn't prevent the site from changing — it just contains the blast
radius of that change to a single, obvious location.