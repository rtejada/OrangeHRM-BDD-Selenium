from selenium.webdriver.common.by import By
from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.add_work_experience import CurriculumVitae
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
    NAME_SELECTOR = '//*[@id="frmDelWorkExperience"]/table/tbody/'
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

        self.wait_selector_visible(self.SECTION_WORK_EXPERIENCE)
        self.wait_button_clickable(self.WORK_CHECKBOX)
        rows_count = len(self.driver.find_elements(*self.TABLE_ROWS))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element(By.XPATH, (self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.COL_SELECTOR))

            self.LIST_COMPANY.append(value.text)

        return company in self.LIST_COMPANY


