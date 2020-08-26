from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.search_by_id import OrangeSiteSearchId
from lib.pages.data_employee import DataEmployeeEdit
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

    PERSONAL_DETAILS = (By.ID, 'pdMainContainer')
    LIST_EMPLOYEES = (By.ID, 'menu_pim_viewEmployeeList')
    IDENTIFICATION = (By.ID, 'empsearch_id')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')

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

    def item_employee(self):

        edit = DataEmployeeEdit(self.driver)
        edit.data_employee()
        new_id = edit.get_id()
        return new_id

    def add_image(self):

        upload_file = AddFile(self.driver)
        upload_file.add_img()

    def search_new_id_employee(self, id_employee):

        search_id = OrangeSiteSearchId(self.driver)
        search_id.personal_detail = self.PERSONAL_DETAILS
        search_id.menu_selector = self.LIST_EMPLOYEES
        search_id.employee = self.IDENTIFICATION
        search_id.identification = id_employee
        search_id.table_row_selector = self.TABLE_ROWS_SELECTOR

        value = search_id.employee_id()
        return value

















