import pytest
from selenium import webdriver
import time



@pytest.fixture(scope="session", autouse=True)
def browser():
   print("\nstart browser for test..")
   browser = webdriver.Chrome()
   yield browser
   print("\nquit browser..")
   time.sleep(10)
   browser.quit()