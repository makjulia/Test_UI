from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(self.driver, timeout)
        self.base_url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def open(self):
        self.driver.maximize_window()
        return self.driver.get(self.base_url)


    def click_element(self, locator):
        click_element = self.find_element(locator)
        click_element.click()
        return click_element

