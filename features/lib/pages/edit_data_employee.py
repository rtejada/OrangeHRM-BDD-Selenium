from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.search_items import SearchItems
from lib.pages.data_employee import DataEmployee
from lib.pages.pages_search.add_file import AddFile
from selenium.webdriver.common.by import By
import os
import json


class EditDataEmployees(OrangeBasePage):

    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_viewEmployeeList'
    BUTTON_LIST_EMPLOYEES = (By.ID, EMPLOYEE)

    NAME_EMPLOYEE = (By.ID, 'empsearch_employee_name_empName')
    ID_EMP_SEARCH = (By.ID, 'empsearch_id')
    SEARCH_EMPLOYEE = (By.ID, 'searchBtn')

    VISIBLE_SCREEN = (By.XPATH, '//*[@id="attachmentList"]/div/h1')
    SCREEN_SELECT_FILE = (By.ID, 'addPaneAttachments')
    BUTTON_SELECT_FILE = (By.ID, 'ufile')
    BUTTON_ADD_LOAD = (By.ID, 'btnAddAttachment')

    PERSONAL_DETAILS = (By.ID, 'pdMainContainer')
    LIST_EMPLOYEES = (By.XPATH, '//*[@id="menu_pim_viewEmployeeList"]')
    IDENTIFICATION = (By.ID, 'empsearch_id')
    VISIBLE_TABLE_SCREEN = (By.XPATH, '//*[@id="resultTable"]/thead/tr/th[1]//input')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[3]//a'

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/data_users.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.CODE_EMPLOYEE = self.DATA_EMPLOYEE['id_employee']

    def select_menu(self):

        self.click_button(self.MODULE_INFO_PERSONAL)

        self.wait_selector_visible(self.BUTTON_LIST_EMPLOYEES)

        self.click_by_javascript(self.EMPLOYEE)

    def search_data_employee(self):

        self.fill_text_field(self.ID_EMP_SEARCH, self.CODE_EMPLOYEE)

        self.click_button(self.SEARCH_EMPLOYEE)

    def data_employee(self):

        edit = DataEmployee(self.driver)
        edit.add_data()
        new_id = edit.get_id()
        return new_id

    def add_image(self):

        self.wait_selector_visible(self.VISIBLE_SCREEN)

        self.click_button(self.BUTTON_ADD_LOAD)

        self.wait_selector_visible(self.SCREEN_SELECT_FILE)

        self.wait_button_clickable(self.SCREEN_SELECT_FILE)

        upload_file = AddFile(self.driver)
        upload_file.select_file = self.SCREEN_SELECT_FILE
        upload_file.add_img()

        self.wait_button_clickable(self.BUTTON_ADD_LOAD)

        self.send_enter_key(self.BUTTON_ADD_LOAD)

    def search_new_id_employee(self, name):

        search_id = SearchItems(self.driver)
        search_id.select_menu = self.PERSONAL_DETAILS
        search_id.access_option = self.LIST_EMPLOYEES
        search_id.item_employee = self.IDENTIFICATION

        press_filter = ''
        press_rapid_filter = ''
        visible_selector = ''
        contact_name = ''

        return value

















