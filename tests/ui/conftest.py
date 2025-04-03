import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def browser():
   print("\nstart browser for test..")
   options = Options()
   options.add_argument("--headless")
   browser = webdriver.Chrome(options=options)
   yield browser
   print("\nquit browser..")
   time.sleep(10)
   browser.quit()