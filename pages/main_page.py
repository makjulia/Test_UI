from selenium.webdriver.common.by import By

from helpers.base_page import BasePage


class SearchLocators:

    LOCATOR_BUTTON_ADD_CUSTOMER = (By.CSS_SELECTOR, "[ng-click='addCust()']")
    LOCATOR_FIELD_FIRST_NAME = (By.CSS_SELECTOR, "[placeholder='First Name']")
    LOCATOR_FIELD_LAST_NAME = (By.CSS_SELECTOR, "[placeholder='Last Name']")
    LOCATOR_FIELD_POST_CODE = (By.CSS_SELECTOR, "[placeholder='Post Code']")
    LOCATOR_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default")
    LOCATOR_BUTTON_CUSTOMERS = (By.CSS_SELECTOR, "[ng-click='showCust()']")
    LOCATOR_SORT_FIRST_NAME = (By.XPATH, "//tr/td[1]/a")
    LOCATOR_TABLE = (By.XPATH, "//div/table/tbody/tr")

class SearchHelper(BasePage):

    """Метод для поиска элемента на странице и заполнения поля"""
    def enter_word(self, locator, word):
        search_field = self.click_element(locator)
        search_field.send_keys(word)
        return search_field

    """Метод для считывания имен First Name из таблицы"""
    def get_names(self, locator):
        names = []

        rows = len(self.find_elements((locator[0], f'{locator[1]}')))

        for r in range(1, rows + 1):
            first_name = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{1}]')).text
            names.append(first_name)

        return names

    """Метод для поиска кнопки Delete для удаления клиента"""
    def get_button_delete(self, locator, name):
        rows = len(self.find_elements((locator[0], f'{locator[1]}')))
        columns = len(self.find_elements((locator[0], f'{locator[1]}[1]/td')))

        for r in range(1, rows + 1):
            first_name = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{1}]')).text
            if first_name == name:
                button_delete = self.find_element((locator[0], f'{locator[1]}[{r}]/td[{columns}]/button'))
                return button_delete






