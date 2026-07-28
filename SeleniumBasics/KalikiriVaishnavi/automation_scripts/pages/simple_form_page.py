"""
pages/simple_form_page.py
Page object for the Simple Form Demo page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    # Locators as class-level constants — never hardcoded inside a method.
    # If the site's markup ever changes, update it here ONCE and every
    # test that uses this page automatically picks up the fix.
    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BTN = (By.ID, "showInput")
    OUTPUT_MESSAGE = (By.ID, "message")

    def enter_message(self, text):
        """Type `text` into the message input field."""
        field = self.wait_for_element(self.MESSAGE_INPUT)
        field.clear()
        field.send_keys(text)

    def click_submit(self):
        """Click the 'Get Checked Value' / submit button, robustly."""
        self.safe_click(self.SUBMIT_BTN)

    def get_displayed_message(self, timeout=15):
        """
        Return the text shown in the output panel after submission.
        No assertion here — that belongs in the test file.
        """
        output = self.wait_for_element(self.OUTPUT_MESSAGE, timeout=timeout)
        return output.text.strip()