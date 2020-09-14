from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.staff_details import PersonalData
from lib.pages.data_employee import DataEmployeeEdit
from lib.pages.pages_search.add_file import AddFile
from selenium.webdriver.common.by import By
import os
import json


class EditDataEmployees(OrangeBasePage):

    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_viewEmployeeList'
    BUTTON_LIST_EMPLOYEES = (By.ID, EMPLOYEE)

    ID_EMPLOYEE = (By.ID, 'empsearch_id')
    SEARCH_EMPLOYEE = (By.ID, 'searchBtn')

    PERSONAL_DETAILS = (By.ID, 'pdMainContainer')
    LIST_EMPLOYEES = (By.ID, 'menu_pim_viewEmployeeList')
    IDENTIFICATION = (By.ID, 'empsearch_id')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    name_employee = ''

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/data_users.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.CODE_EMPLOYEE = self.DATA_EMPLOYEE['id_employee']

    def select_menu(self):

        self.click_button(self.MODULE_INFO_PERSONAL)

        self.wait_selector_visible(self.BUTTON_LIST_EMPLOYEES)

        self.click_by_javascript(self.EMPLOYEE)

    def search_data_employee(self, id_employee):

        self.fill_text_field(self.ID_EMPLOYEE, id_employee)

        self.click_button(self.SEARCH_EMPLOYEE)

    def item_employee(self, id_employee):

        edit = DataEmployeeEdit(self.driver)
        edit.data_employee(id_employee)

    def add_image(self):

        upload_file = AddFile(self.driver)
        upload_file.add_img()

    def add_contact_details(self):

        add = PersonalData(self.driver)
        add.data_of_contact()

















