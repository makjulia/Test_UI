from helpers.generate_data import (generate_string_for_post_code,generate_string_for_first_name, generate_last_name,
                                   get_name_to_delete)
from pages.main_page import SearchHelper, SeacrhLocators
from re import  match
import allure



@allure.epic("Task_UI")
@allure.feature("Test Cases")
class TestsCases:
    @allure.story("Создание клиента Add Customer")
    @allure.step("Шаги")
    def test_customers(self, browser):
        main_page = SearchHelper(browser)
        main_page.open()

        with allure.step("Шаг - Клик по кнопке Add Customer"):
            main_page.click_element(SeacrhLocators.LOCATOR_BUTTON_ADD_CUSTOMER)

        post_code = generate_string_for_post_code()
        first_name = generate_string_for_first_name(post_code)
        last_name = generate_last_name()

        with allure.step("Шаг - Заполнение поля Post Code"):
            main_page.enter_word(SeacrhLocators.LOCATOR_FIELD_POST_CODE, f'{post_code}')
        with allure.step("Шаг - Заполнение поля First Name"):
            main_page.enter_word(SeacrhLocators.LOCATOR_FIELD_FIRST_NAME, f'{first_name}')
        with allure.step("Шаг - Заполнение поля Last Name"):
            main_page.enter_word(SeacrhLocators.LOCATOR_FIELD_LAST_NAME,f'{last_name}')
        with allure.step("Шаг - Клик по кнопке Add Customer"):
            main_page.click_element(SeacrhLocators.LOCATOR_BUTTON)

        alert = browser.switch_to.alert
        msg = alert.text
        assert bool(match(r'Customer added successfully', msg))
        alert.accept()

    @allure.epic("Task_UI")
    @allure.feature("Test Cases")
    @allure.story("Сортировка клиентов по имени First Name")
    @allure.step("Шаги")
    def test_sort_customers(self, browser):
        main_page = SearchHelper(browser)

        with allure.step("Шаг - Клик по кнопке Customers"):
            main_page.click_element(SeacrhLocators.LOCATOR_BUTTON_CUSTOMERS)
        with allure.step("Шаг - Клик по ссылке First Name"):
            main_page.click_element(SeacrhLocators.LOCATOR_SORT_FIRST_NAME)

    @allure.epic("Task_UI")
    @allure.feature("Test Cases")
    @allure.story("Удаление клиента")
    @allure.step("Шаги")
    def test_deletecustomers(self, browser):
        main_page = SearchHelper(browser)
        with allure.step("Шаг - Клик по кнопке Customers"):
            main_page.click_element(SeacrhLocators.LOCATOR_BUTTON_CUSTOMERS)
        customers_del_btns = main_page.get_customers_del_btns(SeacrhLocators.LOCATOR_TABLE)
        name_to_delete = get_name_to_delete(customers_del_btns.keys())
        with allure.step("Шаг - Клик по кнопке Delete"):
            customers_del_btns[name_to_delete].click()

        assert name_to_delete not in main_page.get_customers_del_btns(SeacrhLocators.LOCATOR_TABLE)
