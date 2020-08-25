from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.search_dates import OrangeSiteSearchEmployee
from selenium.webdriver.common.by import By
from random_word import RandomWords
from random import randint


class AdminEmployees(OrangeBasePage):

    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_addEmployee'
    ADD_EMPLOYEE = (By.ID, EMPLOYEE)
    FIRST_NAME = (By.ID, 'firstName')
    MIDDLE_NAME = (By.ID, 'middleName')
    LAST_NAME = (By.ID, 'lastName')
    EMPLOYEE_ID = (By.ID, 'employeeId')
    CHECK_LOGIN = (By.ID, 'chkLogin')
    ALIAS = (By.ID, 'user_name')
    PASS_ALIAS = (By.ID, 'user_password')
    RE_ALIAS = (By.ID, 're_password')
    SAVE_EMPLOYEE = (By.ID, 'btnSave')
    PERSONAL_DETAILS = (By.ID, 'pdMainContainer')
    LIST_EMPLOYEES = (By.XPATH, '//*[@id="menu_pim_viewEmployeeList"]')
    VISIBLE_TABLE_SCREEN = (By.XPATH, '//*[@id="resultTable"]/thead/tr/th[1]//input')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[3]//a'
    employee_code = ''
    first_name = ''
    middle_name = ''
    last_name = ''
    alias = ''
    pwd_alias = ''
    name_employee = ''

    def select_menu(self):

        self.click_button(self.MODULE_INFO_PERSONAL)

        self.wait_selector_visible(self.ADD_EMPLOYEE)

        self.click_by_javascript(self.EMPLOYEE)

    def add_data(self, cod, p_nombre, s_nombre, apellidos, usu, pwd):

        r = RandomWords()
        self.first_name = p_nombre + str(r.get_random_word())
        self.middle_name = s_nombre + str(r.get_random_word())
        self.last_name = apellidos + str(r.get_random_word())
        self.alias = usu + str(randint(20000, 300000))
        self.pwd_alias = pwd + str(randint(2000, 30000))
        self.employee_code = cod + str(randint(100000, 20000000))

        self.name_employee = self.first_name + ' ' + self.middle_name

        self.wait_button_clickable(self.FIRST_NAME)

        self.fill_text_field(self.FIRST_NAME, self.first_name)

        self.fill_text_field(self.MIDDLE_NAME, self.middle_name)

        self.fill_text_field(self.LAST_NAME, self.last_name)

        self.fill_text_field(self.EMPLOYEE_ID, self.employee_code)

        self.click_button(self.CHECK_LOGIN)

        self.fill_text_field(self.ALIAS, self.alias)

        self.fill_text_field(self.PASS_ALIAS, self.pwd_alias)

        self.fill_text_field(self.RE_ALIAS, self.pwd_alias)

        self.send_enter_key(self.SAVE_EMPLOYEE)

    def get_employee(self):

        return self.name_employee, self.employee_code

    def search_name_employee(self, name):

        search_contact = OrangeSiteSearchEmployee(self.driver)
        search_contact.personal_detail = self.PERSONAL_DETAILS
        search_contact.menu_selector = self.LIST_EMPLOYEES

        search_contact.result_table = self.VISIBLE_TABLE_SCREEN
        search_contact.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_contact.col_selector = self.COL_SELECTOR
        search_contact.name_selector = self.NAME_SELECTOR
        value = search_contact.search_element(name)

        return value





