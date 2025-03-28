from helpers.base_page import BasePage
from selenium.webdriver.common.by import By


class SeacrhLocators:

    LOCATOR_BUTTON_ADD_CUSTOMER = (By.CSS_SELECTOR, "[ng-click='addCust()']")
    LOCATOR_FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[placeholder='First Name']")
    LOCATOR_FIELD_LAST_NAME = (By.CSS_SELECTOR, "[placeholder='Last Name']")
    LOCATOR_FIELD_POST_CODE = (By.CSS_SELECTOR, "[placeholder='Post Code']")
    LOCATOR_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default")
    LOCATOR_BUTTON_CUSTOMERS = (By.CSS_SELECTOR, "[ng-click='showCust()']")
    LOCATOR_SORT_FIRST_NAME = (By.XPATH, "//tr/td[1]/a")
    LOCATOR_TABLE = (By.XPATH, '//div/table/tbody/tr')

class SearchHelper(BasePage):

    # Метод для поиска элемента на странице и заполнения поля
    def enter_word(self, locator, word):
        search_field = self.click_element(locator)
        search_field.send_keys(word)
        return search_field


    def get_customers_del_btns(self, locator):
        customers_del_btns = {}

        rows = len(self.find_elements((locator[0], f'{locator[1]}')))
        columns = len(self.find_elements((locator[0], f'{locator[1]}[1]/td')))

        for r in range(1, rows + 1):
            first_name = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{1}]')).text
            delete_btn = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{columns}]/button'))
            customers_del_btns[first_name] = delete_btn

        return customers_del_btns




