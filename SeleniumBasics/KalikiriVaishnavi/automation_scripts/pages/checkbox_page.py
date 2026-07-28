"""
pages/checkbox_page.py
Page object for the Checkbox Demo page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    # Locator for ALL checkboxes on the page; individual checkboxes are
    # accessed by index from this list rather than hardcoding separate
    # locators for each one.
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def _get_checkbox(self, index):
        checkboxes = self.driver.find_elements(*self.CHECKBOXES)
        return checkboxes[index]

    def check_option(self, index):
        """Click the checkbox at `index` if it isn't already checked."""
        box = self._get_checkbox(index)
        if not box.is_selected():
            box.click()

    def uncheck_option(self, index):
        """Click the checkbox at `index` if it is currently checked."""
        box = self._get_checkbox(index)
        if box.is_selected():
            box.click()

    def is_option_checked(self, index):
        """Return True/False for whether the checkbox at `index` is selected."""
        return self._get_checkbox(index).is_selected()