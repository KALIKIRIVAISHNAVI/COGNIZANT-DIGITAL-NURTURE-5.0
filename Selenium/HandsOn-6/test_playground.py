"""
test_playground.py
Run with:
    pip install selenium webdriver-manager pytest pytest-html
    python -m pytest -v test_playground.py
    python -m pytest test_playground.py --html=report.html --self-contained-html
"""

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


def safe_get(driver, url, retries=3, delay=3):
    """Navigate with retries so a flaky network blip doesn't fail the test."""
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            driver.get(url)
            return
        except WebDriverException as e:
            last_error = e
            time.sleep(delay)
    raise RuntimeError(f"Could not reach '{url}' after {retries} attempts.") from last_error


# Step 45: 3 separate parameter sets -> 3 separate test runs, each shown
# individually (pass/fail) in the HTML report.
@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    """
    Open Simple Form Demo, enter the parametrized message in the message
    input, click Submit, wait for the message display element, and assert
    its text equals the input message.
    """
    safe_get(driver, base_url + "simple-form-demo")

    message_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-message"))
    )
    message_input.clear()
    message_input.send_keys(message)

    submit_btn = driver.find_element(By.ID, "showInput")
    submit_btn.click()

    output = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert output.text.strip() == message, (
        f"Expected '{message}' but got '{output.text.strip()}'"
    )


def test_checkbox_interaction(driver, base_url):
    """
    Open Checkbox Demo, click the first checkbox, assert it is selected
    (is_selected()), click it again, assert it is deselected.
    """
    safe_get(driver, base_url + "checkbox-demo")

    # Grab the first checkbox input on the page rather than hardcoding an id,
    # since exact ids can change between site updates.
    first_checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox']"))
    )

    first_checkbox.click()
    assert first_checkbox.is_selected(), "Checkbox should be selected after first click"

    first_checkbox.click()
    assert not first_checkbox.is_selected(), "Checkbox should be deselected after second click"


def test_dropdown_selection(driver, base_url):
    """
    Step 49: open the Select Dropdown List demo, use Select(...) to choose
    'Wednesday', assert the selected option text is 'Wednesday'.

    Select is the correct way to interact with <select> HTML elements —
    clicking options directly is unreliable because native <select> dropdowns
    render as OS-level popups that Selenium can't click into like normal
    page elements.
    """
    safe_get(driver, base_url + "select-dropdown-demo")

    dropdown_el = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "select-demo"))
    )
    select = Select(dropdown_el)
    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option
    assert selected_option.text.strip() == "Wednesday", (
        f"Expected 'Wednesday' but got '{selected_option.text.strip()}'"
    )