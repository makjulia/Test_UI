import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers.api.api_helper import ServiceApi


@pytest.fixture(scope="session")
def browser():
   print("\nstart browser for test..")
   options = Options()
   options.add_argument("--headless")
   browser = webdriver.Chrome(options=options)
   yield browser
   print("\nquit browser..")
   time.sleep(10)
   browser.quit()

@pytest.fixture(scope="session")
def service():
   print("\nstart api test..")
   service = ServiceApi()
   yield service
   print("\nfinish api test..")