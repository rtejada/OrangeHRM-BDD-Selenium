from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.staff_details import ContactData
from lib.pages.data_employee import DataEmployeeEdit
from lib.pages.add_employees_job import EmployeeWorkplaceData
from lib.pages.pages_search.confirm_registration import ConfirmRegisters
from lib.data.query_employee import DataBase
from selenium.webdriver.common.by import By
import os
import json


class EditDataEmployees(OrangeBasePage):

    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_viewEmployeeList'
    FORM_EMP_PERSONAL_DETAILS = (By.ID, 'frmEmpPersonalDetails')
    BUTTON_LIST_EMPLOYEES = (By.ID, EMPLOYEE)
    ID_EMPLOYEE = (By.ID, 'empsearch_id')
    SEARCH_EMPLOYEE = (By.ID, 'searchBtn')
    PERSONAL_DETAILS = (By.ID, 'ohrmList_chkSelectAll')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    FILE_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[5]'

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/data_users.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.CODE_EMPLOYEE = self.DATA_EMPLOYEE['id_employee']

    def select_menu(self):

        self.click_button(self.MODULE_INFO_PERSONAL)

        self.wait_selector_visible(self.BUTTON_LIST_EMPLOYEES)

        self.click_by_javascript(self.EMPLOYEE)

    def search_data_employee(self, employee_id):

        query = DataBase()
        result = query.get_employee_by_id(employee_id)

        if result is not None:
            try:
                self.fill_text_field(self.ID_EMPLOYEE, employee_id)

                self.click_button(self.SEARCH_EMPLOYEE)
            except Exception as e:
                print('Access Error', e)
        else:
            print('The employee is does not exist')

    def personal_data(self, id_employee):

        edit = DataEmployeeEdit(self.driver)
        edit.data_employee(id_employee)

    def add_contact_details(self):

        self.wait_selector_visible(self.FORM_EMP_PERSONAL_DETAILS)
        add = ContactData(self.driver)
        add.data_of_contact()

    def add_job(self, work_data):
        register = EmployeeWorkplaceData(self.driver)
        register.job_details(work_data)

    def search_register(self, data_search):

        data = ConfirmRegisters(self.driver)
        data.personal_information_module = self.MODULE_INFO_PERSONAL
        data.employee_list = self.BUTTON_LIST_EMPLOYEES
        data.search_id = self.ID_EMPLOYEE
        data.search = self.SEARCH_EMPLOYEE
        data.result_table = self.PERSONAL_DETAILS
        data.table_rows_selector = self.TABLE_ROWS_SELECTOR
        data.file_selector = self.FILE_SELECTOR
        data.col_selector = self.COL_SELECTOR
        found = data.register(data_search)
        return found


















