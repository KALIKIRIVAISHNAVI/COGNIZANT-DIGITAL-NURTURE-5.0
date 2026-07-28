import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    WebDriverException,
    NoSuchElementException,
    TimeoutException,
)
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


def safe_get(driver, url, retries=3, delay=3):
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
        f"This looks like a network/connectivity issue on this machine, "
        f"not a problem with the Selenium code."
    ) from last_error


def click_success_message_button(driver):
    """
    Finds a button containing 'success' (case-insensitive), scrolls to it, and clicks.
    """
    xpath = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'success')]"
    
    # 1. Wait for presence
    btn = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, xpath)),
        message="Could not find the success button. Please verify the page loaded correctly."
    )
    
    # 2. Scroll into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
    time.sleep(0.5) 
    
    # 3. Wait for clickable
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    
    # 4. Click
    try:
        btn.click()
    except Exception:
        driver.execute_script("arguments[0].click();", btn)


def step_36(driver):
    print("\n--- Step 36: WebDriverWait + visibility_of_element_located ---")
    # UPDATED URL
    safe_get(driver, "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

    click_success_message_button(driver)

    alert_el = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )

    alert_text = alert_el.text
    print(f"Alert text: {alert_text!r}")

    assert "success" in alert_text.lower(), (
        f"Expected alert text to indicate success, got: {alert_text!r}"
    )
    print("PASS: alert text confirms a successful action.")


def step_37(driver):
    print("\n--- Step 37: time.sleep(3) vs explicit wait (timed) ---")

    # UPDATED URL
    safe_get(driver, "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
    start_sleep = time.time()
    click_success_message_button(driver)
    time.sleep(3)  
    alert_el_sleep = driver.find_element(By.CSS_SELECTOR, ".alert-success")
    assert "success" in alert_el_sleep.text.lower()
    sleep_duration = time.time() - start_sleep
    print(f"time.sleep(3) version took: {sleep_duration:.2f}s")

    # UPDATED URL
    safe_get(driver, "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")
    start_wait = time.time()
    click_success_message_button(driver)
    alert_el_wait = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "success" in alert_el_wait.text.lower()
    wait_duration = time.time() - start_wait
    print(f"Explicit wait version took: {wait_duration:.2f}s")


def step_38(driver):
    print("\n--- Step 38: element_to_be_clickable ---")
    # UPDATED URL
    safe_get(driver, "https://www.lambdatest.com/selenium-playground/bootstrap-alert-messages-demo")

    click_success_message_button(driver)
    print("Clicked 'Success Message' button after confirming it was clickable.")

    alert_el = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    assert "success" in alert_el.text.lower()
    print("PASS: alert appeared after a clickable-gated click.")


def step_39(driver):
    print("\n--- Step 39: Fluent wait for a dynamically-loaded table row ---")

    safe_get(
        driver,
        "https://www.lambdatest.com/selenium-playground/table-pagination-datatable-search",
    )

    fluent_wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=0.5,
        ignored_exceptions=(NoSuchElementException,),
    )

    try:
        first_row = fluent_wait.until(
            lambda d: d.find_element(By.CSS_SELECTOR, "table tbody tr")
        )
        print(f"First dynamically-loaded row text: {first_row.text!r}")
        print("PASS: table row appeared within the fluent-wait polling window.")
    except TimeoutException:
        print(
            "TIMEOUT: no table row appeared within 10s of 500ms polling."
        )


def main():
    driver = get_driver()
    try:
        step_36(driver)
        step_37(driver)
        step_38(driver)
        step_39(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()