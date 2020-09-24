from selenium.webdriver.common.by import By
from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.add_work_experience import CurriculumVitae
from lib.pages.pages_search.confirm_registration import ConfirmRegisters
import os


class AddingCurriculumData(OrangeBasePage):

    MODULE_INFO_PERSONAL = (By.LINK_TEXT, 'Módulo de Información Personal')
    EMPLOYEE = 'menu_pim_viewEmployeeList'
    BUTTON_LIST_EMPLOYEES = (By.ID, EMPLOYEE)
    ID_EMPLOYEE = (By.ID, 'empsearch_id')
    SEARCH_EMPLOYEE = (By.ID, 'searchBtn')
    RESULT_DATA = (By.ID, 'tableWrapper')
    PROFILE_PIC = (By.ID, 'profile-pic')
    CHANGE_PHOTO = (By.ID, 'empPic')
    PHOTO_FILE = (By.ID, 'photofile')
    LOAD = (By.ID, 'btnSave')
    CURRICULUM = (By.LINK_TEXT, 'Currículum')
    SECTION_WORK_EXPERIENCE = (By.ID, 'sectionWorkExperience')
    WORK_CHECKBOX = (By.ID, 'workCheckAll')
    TABLE_ROWS = (By.XPATH, '//*[@id="frmDelWorkExperience"]/table/tbody/tr')
    FILE_SELECTOR = '//*[@id="frmDelWorkExperience"]/table/tbody/'
    COL_SELECTOR = '/td[2]'
    LIST_COMPANY = []

    def access_data_employee(self, identification):

        self.fill_text_field(self.ID_EMPLOYEE, identification)

        self.click_button(self.SEARCH_EMPLOYEE)

        self.wait_button_clickable(self.RESULT_DATA)

        self.click_link_text(identification)

    def add_photo(self, img):

        path = os.getcwd() + "/features/lib/data/images/"
        self.wait_selector_visible(self.PROFILE_PIC)
        self.click_button(self.CHANGE_PHOTO)
        self.wait_selector_visible(self.PHOTO_FILE)
        self.wait_button_clickable(self.PHOTO_FILE)
        self.driver.find_element(*self.PHOTO_FILE).send_keys(path + img)
        self.wait_button_clickable(self.LOAD)
        self.send_enter_key(self.LOAD)

    def add_curriculum(self, experience):

        self.wait_selector_visible(self.CURRICULUM)
        self.wait_button_clickable(self.CURRICULUM)
        self.click_button(self.CURRICULUM)

        data = CurriculumVitae(self.driver)
        data.work_experience(experience)

    def confirm_added_data(self, company):

        data = ConfirmRegisters(self.driver)
        data.section_work = self.SECTION_WORK_EXPERIENCE
        data.data_form = self.WORK_CHECKBOX
        data.table_rows_selector = self.TABLE_ROWS
        data.file_selector = self.FILE_SELECTOR
        data.col_selector = self.COL_SELECTOR
        found = data.find_employee_records(company)
        return found


