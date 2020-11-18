from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from lib.pages.pages_search.confirm_registration import ConfirmRegisters
from random import randint


class AssignedImmigrationRegistration(OrangeBasePage):

    RESULT_DATA = (By.ID, 'tableWrapper')
    MAIN_CONTAINER = (By.ID, 'pdMainContainer')
    REPORT_TO = (By.LINK_TEXT, 'Inmigración')
    IMMIGRATION_DATA_PANEL = (By.ID, 'immidrationList')
    ADD = (By.ID, 'btnAdd')
    IMMIGRATION_NUMBER = (By.ID, 'immigration_number')
    IMMIGRATION_PASSPORT_ISSUE_DATE = (By.ID, 'immigration_passport_issue_date')
    CALENDAR = (By.ID, 'ui-datepicker-div')
    DATE = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[3]')
    IMMIGRATION_PASSPORT_EXPIRE_DATE = (By.ID, 'immigration_passport_expire_date')
    SELECT_YEAR = (By.XPATH, '//*[@id="ui-datepicker-div"]//div/select[2]')
    YEAR = '2025'
    IMMIGRATION_STATUS = (By.ID, 'immigration_i9_status')
    IMMIGRATION_COUNTRY = (By.ID, 'immigration_country')
    COUNTRY = 'TZ'
    IMMIGRATION_PASSPORT_REVIEW_DATE = (By.ID, 'immigration_i9_review_date')
    IMMIGRATION_COMMENT = (By.ID, 'immigration_comments')
    SAVE = (By.ID, 'btnSave')
    IMMIGRATION_LIST = (By.ID, 'immidrationList')
    IMMIGRATION_CHECK_ALL = (By.ID, 'immigrationCheckAll')
    ROWS_FORM_IMMIGRATION = (By.XPATH, '//*[@id="frmImmigrationDelete"]/table/tbody/tr')
    FILE = '//*[@id="frmImmigrationDelete"]/table/tbody/'
    COL = '/td[3]'

    def immigration(self, id_employee):

        self.wait_button_clickable(self.RESULT_DATA)
        self.click_link_text(id_employee)
        self.wait_selector_visible(self.MAIN_CONTAINER)
        self.click_button(self.REPORT_TO)

    def add_immigration_registration(self):
        passport_number = randint(1, 99999999)

        self.wait_selector_visible(self.IMMIGRATION_DATA_PANEL)
        self.click_button(self.ADD)
        self.fill_text_field(self.IMMIGRATION_NUMBER, passport_number)
        self.click_button(self.IMMIGRATION_PASSPORT_ISSUE_DATE)
        self.wait_selector_visible(self.CALENDAR)
        self.click_button(self.DATE)
        self.click_button(self.IMMIGRATION_PASSPORT_EXPIRE_DATE)
        self.wait_selector_visible(self.CALENDAR)
        self.fill_select_field(self.SELECT_YEAR, self.YEAR)
        self.click_button(self.DATE)
        self.fill_text_field(self.IMMIGRATION_STATUS, self.random_letter(7))
        self.fill_select_field(self.IMMIGRATION_COUNTRY, self.COUNTRY)
        self.click_button(self.IMMIGRATION_PASSPORT_REVIEW_DATE)
        self.wait_selector_visible(self.CALENDAR)
        self.click_button(self.DATE)
        self.fill_text_field(self.IMMIGRATION_COMMENT, self.random_letter(70))
        self.send_enter_key(self.SAVE)

        return passport_number

    def search_register(self, passport_number):
        search = ConfirmRegisters(self.driver)
        search.section_work = self.IMMIGRATION_LIST
        search.data_form = self.IMMIGRATION_CHECK_ALL
        search.table_rows_selector = self.ROWS_FORM_IMMIGRATION
        search.file_selector = self.FILE
        search.col_selector = self.COL
        found = search.find_employee_records(str(passport_number))

        return found




