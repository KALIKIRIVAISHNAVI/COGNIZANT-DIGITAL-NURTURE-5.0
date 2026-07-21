from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

driver.get("https://www.lambdatest.com/selenium-playground/")
print(driver.title)
driver.quit()