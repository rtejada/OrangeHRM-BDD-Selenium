from lib.pages.orange_base_page import OrangeBasePage
from selenium.webdriver.common.by import By
import csv
import os
from random import randint


class AdminEmployees(OrangeBasePage):

    EMPLOYEES = ''
    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    ADD_EMPLOYEE = (By.LINK_TEXT, 'Agregar Empleado')
    FIRST_NAME = (By.ID, 'firstName')
    MIDDLE_NAME = (By.ID, 'middleName')
    LAST_NAME = (By.ID, 'lastName')
    EMPLOYEE_ID = (By.ID, 'employeeId')
    CHECK_LOGIN = (By.ID, 'chkLogin')
    ALIAS = (By.ID, 'user_name')
    PASS_ALIAS = (By.ID, 'user_password')
    RE_ALIAS = (By.ID, 're_password')
    SAVE_EMPLOYEE = (By.ID, 'btnSave')

    def __init__(self, driver):
        super().__init__(driver)

        file = open(os.getcwd() + "/features/lib/data/orange_employees.csv")

        content = csv.reader(file, delimiter=',')
        self.EMPLOYEES = list(content)
        file.close()

        self.ID = self.EMPLOYEES[1][0] + '-' + str(randint(10000, 100000))
        self.NAME_EMPLOYEE = self.EMPLOYEES[1][1]

    def select_menu(self):

        self.menu_select_option(self.MODULE_INFO_PERSONAL, self.ADD_EMPLOYEE)

    def add_data(self):

        self.wait_selector_visible(self.FIRST_NAME)

        self.fill_text_field(self.FIRST_NAME, self.NAME_EMPLOYEE)

        self.fill_text_field(self.MIDDLE_NAME, self.EMPLOYEES[1][2])

        self.fill_text_field(self.LAST_NAME, self.EMPLOYEES[1][3])

        self.fill_text_field(self.EMPLOYEE_ID, self.ID)

        self.click_button(self.CHECK_LOGIN)

        self.fill_text_field(self.ALIAS, self.EMPLOYEES[1][4])

        self.fill_text_field(self.PASS_ALIAS, self.EMPLOYEES[1][5])

        self.fill_text_field(self.RE_ALIAS, self.EMPLOYEES[1][5])

        self.send_enter_key(self.SAVE_EMPLOYEE)

    def get_employee(self):

        return self.NAME_EMPLOYEE




