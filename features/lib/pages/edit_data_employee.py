from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from random_word import RandomWords
from random import randint
import os
import json
import uuid


class EditDataEmployees(OrangeBasePage):

    DATA_EMPLOYEE = ''

    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_viewEmployeeList'
    BUTTON_LIST_EMPLOYEES = (By.ID, EMPLOYEE)

    NAME_EMPLOYEE = (By.ID, 'empsearch_employee_name_empName')
    ID_EMP_SEARCH = (By.ID, 'empsearch_id')
    SEARCH_EMPLOYEE = (By.ID, 'searchBtn')
    RESULT_DATA = (By.ID, 'tableWrapper')
    BUTTON_EDIT = (By.ID, 'btnSave')

    OTHER_ID = (By.ID, 'personal_txtOtherID')
    ID_CARD_NUMBER = (By.ID, 'personal_txtLicenNo')
    CALENDAR = (By.ID, 'personal_txtLicExpDate')
    VISIBLE_CALENDAR = (By.ID, 'ui-datepicker-div')
    CARD_EXPIRATION_DATE = (By.ID, 'frmEmpPersonalDetails')

    BUTTON_MONTH = (By.CLASS_NAME, 'ui-datepicker-MONTH_EXPIRATION_CARD')
    BUTTON_YEAR = (By.CLASS_NAME, 'ui-datepicker-YEAR_EXPIRATION_CARD')
    DAY_EXPIRATION_CARD = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]/a')
    DAY_BIRTH = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a')
    GENDER = (By.ID, 'personal_optGender_2')
    MARITAL_STATUS = (By.ID, 'personal_cmbMarital')
    DATE_OF_BIRTH = (By.ID, 'personal_DOB')
    BUTTON_SAVE = (By.ID, 'btnSave')

    PERSONAL_DETAILS = (By.ID, 'pdMainContainer')
    LIST_EMPLOYEES = (By.XPATH, '//*[@id="menu_pim_viewEmployeeList"]')
    VISIBLE_TABLE_SCREEN = (By.XPATH, '//*[@id="resultTable"]/thead/tr/th[1]//input')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[3]//a'
    
    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/data_users.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.ADDITIONAL_ID = self.DATA_EMPLOYEE['other_id'] + str(randint(1, 90000000))
        self.CARD_NUMBER = self.DATA_EMPLOYEE['card_number'] + str(uuid.getnode())
        self.CODE_EMPLOYEE = self.DATA_EMPLOYEE['id_employee']
        self.MONTH_EXPIRATION_CARD = self.DATA_EMPLOYEE['month_expiration']
        self.YEAR_EXPIRATION_CARD = self.DATA_EMPLOYEE['year_expiration']

    def select_menu(self):

        self.click_button(self.MODULE_INFO_PERSONAL)

        self.wait_selector_visible(self.BUTTON_LIST_EMPLOYEES)

        self.click_by_javascript(self.EMPLOYEE)

    def search_data_employee(self):

        self.fill_text_field(self.ID_EMP_SEARCH, self.CODE_EMPLOYEE)

        self.click_button(self.SEARCH_EMPLOYEE)

    def data_employee(self):

        self.wait_button_clickable(self.RESULT_DATA)

        self.click_link_text(self.CODE_EMPLOYEE)

        self.click_button(self.BUTTON_EDIT)

        self.fill_text_field(self.OTHER_ID, self.ADDITIONAL_ID)

        self.fill_text_field(self.ID_CARD_NUMBER, self.CARD_NUMBER)

        self.click_button(self.CALENDAR)

        self.wait_button_clickable(self.VISIBLE_CALENDAR)

        self.fill_select_by_text(self.BUTTON_MONTH, self.MONTH_EXPIRATION_CARD)

        self.fill_select_field(self.BUTTON_YEAR, self.YEAR_EXPIRATION_CARD)

        self.click_button(self.DAY_EXPIRATION_CARD)






