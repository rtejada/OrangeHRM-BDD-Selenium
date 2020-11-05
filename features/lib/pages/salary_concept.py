from selenium.webdriver.common.by import By
from lib.pages.add_salary import AddSalary
from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.confirm_registration import ConfirmRegisters
from lib.data.query_employee import DataBase
import os
import json


class SalaryConcept(OrangeBasePage):

    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_viewEmployeeList'
    RESULT_DATA = (By.ID, 'tableWrapper')
    BUTTON_LIST_EMPLOYEES = (By.ID, EMPLOYEE)
    ID_EMPLOYEE = (By.ID, 'empsearch_id')
    SEARCH_EMPLOYEE = (By.ID, 'searchBtn')
    SALARY = (By.LINK_TEXT, 'Salario/ Sueldo')
    ADD_SALARY = (By.ID, 'addSalary')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/data_users.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.CODE_EMPLOYEE = self.DATA_EMPLOYEE['id_employee']

    def select_menu(self):

        self.click_button(self.MODULE_INFO_PERSONAL)

        self.wait_selector_visible(self.BUTTON_LIST_EMPLOYEES)

        self.click_by_javascript(self.EMPLOYEE)

    def search_employee(self, id_employee):

        self.fill_text_field(self.ID_EMPLOYEE, id_employee)
        self.click_button(self.SEARCH_EMPLOYEE)
        self.wait_button_clickable(self.RESULT_DATA)
        self.click_link_text(id_employee)

    def open_salary_option(self):

        self.wait_selector_visible(self.SALARY)
        self.wait_button_clickable(self.SALARY)
        self.click_button(self.SALARY)
        self.wait_button_clickable(self.ADD_SALARY)
        self.click_button(self.ADD_SALARY)

    def amount(self, salary_scale):

        add = AddSalary(self.driver)
        add.enter_concepts(salary_scale)
        salary_component = add.get_salary_component()
        return salary_component

    def confirm_salary_component(self, salary_component):

        query = DataBase()
        query_result = query.get_salary_component(salary_component)
        if query_result is not None:
            try:
                if salary_component in query_result:
                    return True
            except Exception as e:
                print(f'Exception to get salary component: {e}')

        else:
            return f'The salary component not exists: {salary_component}'


