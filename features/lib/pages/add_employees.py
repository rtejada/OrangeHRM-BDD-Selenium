from lib.pages.base_page import OrangeBasePage
from lib.pages.search_employees import OrangeSiteSearchEmployee
from selenium.webdriver.common.by import By
import csv
import os
from random import randint


class AdminEmployees(OrangeBasePage):

    EMPLOYEES = ''
    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_addEmployee'
    ADD_EMPLOYEE = (By.ID, EMPLOYEE)
    VISIBLE_SCREEN = (By.XPATH, '//*[@id="content"]/div/div[1]/h1')
    FIRST_NAME = (By.ID, 'firstName')
    MIDDLE_NAME = (By.ID, 'middleName')
    LAST_NAME = (By.ID, 'lastName')
    EMPLOYEE_ID = (By.ID, 'employeeId')
    CHECK_LOGIN = (By.ID, 'chkLogin')
    ALIAS = (By.ID, 'user_name')
    PASS_ALIAS = (By.ID, 'user_password')
    RE_ALIAS = (By.ID, 're_password')
    SAVE_EMPLOYEE = (By.ID, 'btnSave')

    LIST_EMPLOYEES_ID = '//*[@id="menu_pim_viewEmployeeList"]'
    LIST_EMPLOYEES = (By.XPATH, '//*[@id="menu_pim_viewEmployeeList"]')
    VISIBLE_TABLE_SCREEN = (By.XPATH, '//*[@id="resultTable"]/thead/tr/th[1]//input')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[3]//a'

    def __init__(self, driver):
        super().__init__(driver)

        file = open(os.getcwd() + "/features/lib/data/orange_employees.csv")

        content = csv.reader(file, delimiter=',')
        self.EMPLOYEES = list(content)
        file.close()

        self.NAME = self.EMPLOYEES[1][1] + '-' + str(randint(1000, 2000))
        self.SURNAMES = self.EMPLOYEES[1][3] + '-' + str(randint(1000, 2000))
        self.USER_NAME = self.EMPLOYEES[1][4] + str(randint(2000, 3000))
        self.ID = self.EMPLOYEES[1][0] + '-' + str(randint(10000, 100000))
        self.NAME_EMPLOYEE = self.NAME + ' ' + self.EMPLOYEES[1][2]

    def select_menu(self):

        self.click_button(self.MODULE_INFO_PERSONAL)

        self.wait_selector_visible(self.ADD_EMPLOYEE)

        self.click_by_javascript(self.EMPLOYEE)

    def add_data(self):

        self.wait_button_clickable(self.FIRST_NAME)

        self.fill_text_field(self.FIRST_NAME, self.NAME)

        self.fill_text_field(self.MIDDLE_NAME, self.EMPLOYEES[1][2])

        self.fill_text_field(self.LAST_NAME, self.SURNAMES)

        self.fill_text_field(self.EMPLOYEE_ID, self.ID)

        self.click_button(self.CHECK_LOGIN)

        self.fill_text_field(self.ALIAS, self.USER_NAME)

        self.fill_text_field(self.PASS_ALIAS, self.EMPLOYEES[1][5])

        self.fill_text_field(self.RE_ALIAS, self.EMPLOYEES[1][5])

        self.send_enter_key(self.SAVE_EMPLOYEE)

    def get_employee(self):

        return self.NAME_EMPLOYEE

    def search_name_employee(self, name):

        search_contact = OrangeSiteSearchEmployee(self.driver)

        search_contact.menu_selector = self.LIST_EMPLOYEES
        #search_contact.menu_selector_id = self.LIST_EMPLOYEES_ID
        search_contact.result_table = self.VISIBLE_TABLE_SCREEN
        search_contact.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_contact.col_selector = self.COL_SELECTOR
        search_contact.name_selector = self.NAME_SELECTOR
        value = search_contact.search_element(name)

        return value





