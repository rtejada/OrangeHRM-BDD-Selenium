from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from random import randint
import os
import json
import uuid


class DataEmployee(OrangeBasePage):

    RESULT_DATA = (By.ID, 'tableWrapper')
    BUTTON_EDIT = (By.ID, 'btnSave')
    NEW_ID = (By.ID, 'personal_txtEmployeeId')
    OTHER_ID = (By.ID, 'personal_txtOtherID')
    ID_CARD_NUMBER = (By.ID, 'personal_txtLicenNo')
    CALENDAR = (By.ID, 'personal_txtLicExpDate')
    VISIBLE_CALENDAR = (By.ID, 'ui-datepicker-div')
    CARD_EXPIRATION_DATE = (By.ID, 'frmEmpPersonalDetails')

    BUTTON_MONTH = (By.XPATH, '//*[@id="ui-datepicker-div"]//div/select[@class="ui-datepicker-month"]')
    BUTTON_YEAR = (By.XPATH, '//*[@id="ui-datepicker-div"]//div/select[@class="ui-datepicker-year"]')
    DAY_EXPIRATION_CARD = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[3]/a')
    DAY_BIRTH = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a')
    GENDER = (By.ID, 'personal_optGender_2')
    MARITAL_STATUS = (By.ID, 'personal_cmbMarital')
    LIST_NATIONALITIES = (By.ID, 'personal_cmbNation')
    DATE_OF_BIRTH = (By.ID, 'personal_DOB')
    BUTTON_SAVE = (By.ID, 'btnSave')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/data_users.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.ID = self.DATA_EMPLOYEE['new_id_employee'] + str(randint(1, 900000))
        self.ADDITIONAL_ID = self.DATA_EMPLOYEE['other_id'] + str(randint(1, 90000000))
        self.CARD_NUMBER = self.DATA_EMPLOYEE['card_number'] + str(uuid.getnode())
        self.CODE_EMPLOYEE = self.DATA_EMPLOYEE['id_employee']
        self.MONTH_EXPIRATION_CARD = self.DATA_EMPLOYEE['month_expiration']
        self.YEAR_EXPIRATION_CARD = self.DATA_EMPLOYEE['year_expiration']
        self.CIVIL_STATUS = self.DATA_EMPLOYEE['marital_status']
        self.NATIONALITY = self.DATA_EMPLOYEE['nationality']
        self.MONTH_BIRTH = self.DATA_EMPLOYEE['month_birth']
        self.YEAR_BIRTH = self.DATA_EMPLOYEE['year_birth']

    def add_data(self):

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

        self.click_button(self.GENDER)

        self.fill_select_field(self.MARITAL_STATUS, self.CIVIL_STATUS)

        self.fill_select_by_text(self.LIST_NATIONALITIES, self.NATIONALITY)

        self.click_button(self.DATE_OF_BIRTH)

        self.wait_button_clickable(self.VISIBLE_CALENDAR)

        self.fill_select_by_text(self.BUTTON_MONTH, self.MONTH_BIRTH)

        self.fill_select_field(self.BUTTON_YEAR, self.YEAR_BIRTH)

        self.click_button(self.DAY_BIRTH)

        self.send_enter_key(self.BUTTON_SAVE)

    def get_id(self):

        return self.ID
