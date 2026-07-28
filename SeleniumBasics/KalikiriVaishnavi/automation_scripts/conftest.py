"""
conftest.py — shared pytest fixtures for this folder.
pytest auto-loads this file; no import needed in test files.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url():
    """
    Step 48: session-scoped constant, computed once and reused by every
    test instead of each test hardcoding the URL string.
    """
    # NOTE: LambdaTest rebranded to "TestMu AI" and moved this playground to
    # testmuai.com. lambdatest.com now likely redirects through to this new
    # domain, and that extra redirect hop was causing our tests to time out
    # waiting for elements. Pointing directly at the current domain avoids
    # the redirect entirely.
    return "https://www.testmuai.com/selenium-playground/"


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Step 46: pytest hook that runs after EVERY phase of a test
    (setup / call / teardown) and attaches the outcome to the test item as
    rep_setup / rep_call / rep_teardown. The driver fixture below reads
    item.rep_call.failed to know whether the actual test body failed, so
    it can grab a screenshot before quitting the browser.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def driver(request):
    """
    scope='function' -> this fixture runs fresh for EVERY test function.
    That means each test gets its own brand-new browser instance, so tests
    are fully isolated and can't leak state (cookies, open dialogs, etc.)
    into each other. (scope='session' would reuse one browser across all
    tests — faster, but risks cross-test interference.)
    """
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # ---- SETUP (runs before the test) ----
    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    yield drv  # <-- test function receives `drv` here as the `driver` argument

    # ---- TEARDOWN (runs after the test, even if it fails/errors) ----
    # Step 46: check whether the test body ("call" phase) failed, and if so
    # save a screenshot named after the test before quitting the browser.
    if request.node.rep_call.failed:
        # request.node.name includes parametrize IDs, e.g.
        # "test_simple_form_submission[Hello]" -> safe to use as a filename
        safe_name = request.node.name.replace("[", "_").replace("]", "").replace("/", "_")
        drv.save_screenshot(f"{safe_name}_failure.png")

    drv.quit()