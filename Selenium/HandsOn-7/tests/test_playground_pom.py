"""
test_playground_pom.py — Hands-On 7: same test coverage as test_playground.py,
refactored to use Page Object Model classes.

Golden rule of POM: test files contain assertions (what should happen),
page files contain interactions (how to make it happen). No driver.find_element
calls appear anywhere in this file.

Run with:
    python -m pytest -v test_playground_pom.py
"""

import pytest

from pages.simple_form_page import SimpleFormPage
from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage


@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    form_page = SimpleFormPage(driver)
    form_page.navigate_to(base_url + "simple-form-demo")

    form_page.enter_message(message)
    form_page.click_submit()

    displayed_message = form_page.get_displayed_message()
    assert displayed_message == message, (
        f"Expected '{message}' but got '{displayed_message}'"
    )


def test_checkbox_interaction(driver, base_url):
    checkbox_page = CheckboxPage(driver)
    checkbox_page.navigate_to(base_url + "checkbox-demo")

    checkbox_page.check_option(0)
    assert checkbox_page.is_option_checked(0), "Checkbox should be checked after check_option"

    checkbox_page.uncheck_option(0)
    assert not checkbox_page.is_option_checked(0), "Checkbox should be unchecked after uncheck_option"


def test_dropdown_selection(driver, base_url):
    dropdown_page = DropdownPage(driver)
    dropdown_page.navigate_to(base_url + "select-dropdown-demo")

    dropdown_page.select_day("Wednesday")

    selected = dropdown_page.get_selected_day()
    assert selected == "Wednesday", f"Expected 'Wednesday' but got '{selected}'"