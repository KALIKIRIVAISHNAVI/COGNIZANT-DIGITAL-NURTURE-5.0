"""
pages/base_page.py
The parent class every page object inherits from. Holds common browser
actions so subclasses don't have to repeat them.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """Open the given URL and clear any popups that might intercept clicks."""
        self.driver.get(url)
        self.dismiss_overlays()

    def dismiss_overlays(self):
        """
        Best-effort dismissal of cookie-consent banners, chat widgets, or
        promo modals that can silently intercept clicks meant for the real
        page content. Marketing sites (like this one) often show these a
        few seconds after load, so a click can land on the overlay instead
        of the button underneath, with no exception raised — the test just
        times out waiting for a result that will never come. Each selector
        is tried briefly; if none is found, we just move on.
        """
        candidates = [
            (By.ID, "onetrust-accept-btn-handler"),
            (By.CSS_SELECTOR, "button[aria-label='Close']"),
            (By.CSS_SELECTOR, ".modal-close"),
            (By.CSS_SELECTOR, "[class*='cookie'] button"),
            (By.CSS_SELECTOR, "[class*='popup'] [class*='close']"),
        ]
        for locator in candidates:
            try:
                el = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable(locator)
                )
                el.click()
            except TimeoutException:
                continue
            except Exception:
                continue

    def get_title(self):
        """Return the current page's <title> text."""
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        """
        Wait until the element identified by `locator` (a (By, value) tuple)
        is visible, then return it. Centralizing this here means every page
        class gets consistent explicit-wait behavior for free.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=10):
        """
        Wait until the element identified by `locator` is present, visible,
        AND enabled/not-obscured, then return it. Use this before clicking
        anything — visibility alone doesn't guarantee a click will land,
        e.g. if something is still animating in or briefly covered by an
        overlay/banner right after page load.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def safe_click(self, locator, timeout=10):
        """
        Click an element robustly: wait until clickable, scroll it into
        view, then try a normal click. If something is still overlapping it
        (ElementClickInterceptedException), fall back to a JavaScript click,
        which bypasses whatever is visually on top and clicks the element
        directly in the DOM.
        """
        element = self.wait_for_clickable(locator, timeout=timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)