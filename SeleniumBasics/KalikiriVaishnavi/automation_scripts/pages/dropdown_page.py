"""
pages/dropdown_page.py
Page object for the Select Dropdown List demo page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "select-demo")

    def select_day(self, day_name):
        """
        Select `day_name` from the dropdown using Selenium's Select class
        internally — the correct way to interact with native <select>
        elements, since clicking options directly is unreliable (native
        dropdowns render as OS-level popups Selenium can't click into).
        """
        dropdown_el = self.wait_for_element(self.DROPDOWN)
        select = Select(dropdown_el)
        select.select_by_visible_text(day_name)

    def get_selected_day(self):
        """Return the currently selected option's text. No assertion here."""
        dropdown_el = self.wait_for_element(self.DROPDOWN)
        select = Select(dropdown_el)
        return select.first_selected_option.text.strip()