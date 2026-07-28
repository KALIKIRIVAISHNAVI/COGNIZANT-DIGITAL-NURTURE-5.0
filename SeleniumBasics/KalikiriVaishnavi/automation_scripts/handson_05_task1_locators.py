"""
Task 1: Locator Strategies — From Simple to Robust
Run with:
    pip install selenium webdriver-manager
    python task1_locators.py
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    # Helps avoid some corporate firewalls/antivirus tools that flag
    # automation-controlled Chrome and block its network requests.
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


def safe_get(driver, url, retries=3, delay=3):
    """
    Navigate to a URL with retries. Raises a clear error if the machine
    genuinely has no route to the site (net::ERR_ADDRESS_UNREACHABLE etc).
    """
    last_error = None
    for attempt in range(1, retries + 1):
        try:
            driver.get(url)
            return
        except WebDriverException as e:
            last_error = e
            print(f"  Attempt {attempt}/{retries} failed to load {url}: {e.msg.splitlines()[0]}")
            time.sleep(delay)
    raise RuntimeError(
        f"Could not reach '{url}' after {retries} attempts. "
        f"This is a network/connectivity issue (DNS, proxy, firewall, or no internet) "
        f"on this machine, not a problem with the Selenium code. "
        f"Try opening the URL manually in a normal Chrome window to confirm."
    ) from last_error


def main():
    driver = get_driver()
    try:
        # ------------------------------------------------------------------
        # Steps 32-33: Simple Form Demo page
        # ------------------------------------------------------------------
        safe_get(driver, "https://www.lambdatest.com/selenium-playground/simple-form-demo")

        # FIXED: driver.get() returns as soon as the initial page load
        # starts — it does NOT guarantee the form fields have finished
        # rendering (ads/JS on this page can delay that). Racing ahead with
        # find_element() immediately after get() causes intermittent
        # "no such element" failures even for a rock-solid ID locator, just
        # because the element genuinely isn't in the DOM yet at that instant.
        # An explicit wait fixes this at the source instead of guessing at
        # markup changes that aren't actually happening.
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "user-message"))
        )

        # Step 32: locate the message input using all 6 strategies
        # Locate by ID first — this is our ground truth, since IDs are stable
        # and don't depend on guessing the current tag name.
        el_id = driver.find_element(By.ID, "user-message")
        actual_tag = el_id.tag_name  # discover the REAL tag instead of assuming "textarea"
        print(f"(Discovered actual tag for #user-message: <{actual_tag}>)")

        el_name = driver.find_element(By.NAME, "message")
        el_class = driver.find_element(By.CLASS_NAME, "form-control")
        el_tag = driver.find_element(By.TAG_NAME, actual_tag)

        # FIXED: use a wildcard tag (*) in XPath instead of hardcoding
        # "textarea" — the site's markup no longer uses a <textarea> for
        # this field, so an XPath assuming that tag fails even though the
        # id itself is correct and stable. "//*[@id='user-message']"
        # matches the element regardless of its actual tag name.
        el_xpath_relative = driver.find_element(By.XPATH, "//*[@id='user-message']")

        for name, el in [
            ("By.ID", el_id),
            ("By.NAME", el_name),
            ("By.CLASS_NAME", el_class),
            (f"By.TAG_NAME ('{actual_tag}')", el_tag),
            ("By.XPATH (relative)", el_xpath_relative),
        ]:
            print(f"{name}: found -> {el.is_displayed()}")

        # NOTE: If NAME, CLASS_NAME, or TAG_NAME print "found -> False",
        # that isn't a crash — find_element() returns the FIRST match in
        # DOM order, and it grabbed a different, hidden element that
        # happens to share that same name/class/tag elsewhere on the page.
        # This is precisely why non-unique locators are less reliable than
        # ID or an attribute-specific selector: they can silently resolve
        # to the wrong element instead of failing loudly.

        # Absolute XPath: deliberately fragile. Wrapped in try/except because
        # this is EXACTLY the failure mode Step 35 asks you to observe — any
        # change to the page's DOM structure (an extra wrapping <div>, a
        # reordered section, a changed tag, etc.) breaks the hardcoded path
        # entirely, even though the element itself hasn't moved semantically.
        absolute_xpath = "/html/body/div[2]/div/div[1]/div[2]/div/div[1]/form/div/div[1]/textarea"
        try:
            el_xpath_absolute = driver.find_element(By.XPATH, absolute_xpath)
            print(f"By.XPATH (absolute): found -> {el_xpath_absolute.is_displayed()}")
        except NoSuchElementException:
            print(
                "By.XPATH (absolute): FAILED to locate element.\n"
                "  -> This demonstrates why absolute XPath is the least preferred "
                "locator strategy: it hardcodes both the exact DOM path AND the exact "
                "tag name, so even a minor structural change on the page (an added "
                "wrapper div, a reordered section, or the field's tag changing) breaks "
                "it completely, while ID/Name/CSS/relative-XPath-by-attribute keep "
                "working because they target the element by its own stable attributes."
            )

        # Step 33: 3 CSS selectors for the same element
        css_by_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
        css_by_attr = driver.find_element(By.CSS_SELECTOR, "[name='message']")
        # FIXED (again): assuming a <form> ancestor was still guessing at
        # this page's markup, and it turns out the field has no <form>
        # ancestor at all here. Rather than keep guessing at parent
        # structure that keeps changing, this selector demonstrates a
        # different, self-contained CSS strategy instead: a compound
        # selector combining the ELEMENT'S OWN tag (dynamically discovered
        # above, not hardcoded) with its id. This is still a distinct
        # locator technique from a plain "#user-message" ID selector, but
        # it doesn't depend on any wrapper element that might disappear.
        css_by_parent_child = driver.find_element(By.CSS_SELECTOR, f"{actual_tag}#user-message")

        for name, el in [
            ("CSS by ID", css_by_id),
            ("CSS by attribute", css_by_attr),
            ("CSS by tag+id (compound)", css_by_parent_child),
        ]:
            print(f"{name}: found -> {el.is_displayed()}")

        # ------------------------------------------------------------------
        # Step 34: Checkbox Demo page
        # ------------------------------------------------------------------
        safe_get(driver, "https://www.lambdatest.com/selenium-playground/checkbox-demo")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='Option 1']"))
        )

        first_option_label = driver.find_element(By.XPATH, "//label[text()='Option 1']")
        print(f"\nExact text() match: {first_option_label.text}")

        all_option_labels = driver.find_elements(By.XPATH, "//label[contains(text(),'Option')]")
        print(f"contains() match count: {len(all_option_labels)}")
        for label in all_option_labels:
            print(f"  - {label.text}")

        # ------------------------------------------------------------------
        # Step 35: Ranking — most to least preferred, with justification
        # ------------------------------------------------------------------
        ranking_comment = """
        Ranking of locator strategies (most -> least preferred):
        1. ID              - unique by spec, fastest, most readable, resistant to markup changes
        2. Name             - nearly as reliable as ID for form fields
        3. CSS Selector     - fast, flexible, resilient to reordering, widely supported
        4. Class Name       - risky: classes are often shared for styling, so not always unique
        5. Relative XPath   - powerful for text/parent-axis lookups, but more verbose & slower than CSS
        6. Absolute XPath   - least preferred: hardcodes full DOM path, breaks on ANY structural change
        """
        print(ranking_comment)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()