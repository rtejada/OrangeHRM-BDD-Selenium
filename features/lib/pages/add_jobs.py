from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.search_result_table import SearchElement
from lib.pages.delete_register import DeleteRegister
from selenium.webdriver.common.by import By
import os


class AddNewJobs(OrangeBasePage):

    ADMIN = (By.LINK_TEXT, 'Administrador')
    JOBS = 'menu_admin_Job'
    JOBS_TITLE_LISTS = (By.ID, 'menu_admin_Job')
    JOB_TITLES = (By.ID, 'menu_admin_viewJobTitleList')
    BUTTON_ADD = (By.ID, 'btnAdd')
    FORM = (By.ID, 'frmSavejobTitleD')
    JOB_TITLE = (By.ID, 'jobTitle_jobTitle')
    JOB_DESCRIPTION = (By.ID, 'jobTitle_jobDescription')
    SELECT_FILE = (By.ID, 'jobTitle_jobSpec')
    NOTE = (By.ID, 'jobTitle_note')
    BUTTON_SAVE = (By.ID, 'btnSave')
    path = os.getcwd() + "/features/lib/data/images/"

    VISIBLE_TABLE_SCREEN = (By.XPATH, '//*[@id="resultTable"]/thead/tr/th[1]//input')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[2]//a'
    LIST_JOBS = []

    BUTTON_DELETE = (By.ID, 'btnDelete')
    SCREEN_DELETE = (By.ID, 'deleteConfModal')
    BUTTON_OK = (By.ID, 'dialogDeleteBtn')
    TITLE_JOB = (By.XPATH, '//*[@id="resultTable"]/tbody/tr/td/a')
    VISIBLE_TABLE = (By.ID, 'ohrmList_chkSelectAll')
    ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SEL = '//*[@id="resultTable"]/tbody/'
    COL_SEL = '/td[2]/a'
    BUTTON_CHECK = '/td[1]'

    def select_menu(self):

        self.click_button(self.ADMIN)

        self.wait_selector_visible(self.JOBS_TITLE_LISTS)

        self.menu_select_option(self.JOBS_TITLE_LISTS, self.JOB_TITLES)

    def add_jobs(self, dict_jobs):

        self.wait_button_clickable(self.BUTTON_ADD)

        self.click_button(self.BUTTON_ADD)

        self.wait_selector_visible(self.JOB_TITLE)

        self.wait_button_clickable(self.JOB_TITLE)

        self.fill_text_field(self.JOB_TITLE, dict_jobs['title'])
        self.fill_text_field(self.JOB_DESCRIPTION, dict_jobs['job_description'])
        self.driver.find_element(*self.SELECT_FILE).send_keys(self.path + dict_jobs['img'])
        self.fill_text_field(self.NOTE, dict_jobs['note'])

        self.send_enter_key(self.BUTTON_SAVE)

    def search_jobs(self, search_item):

        search = SearchElement(self.driver)
        search.visible_selector = self.VISIBLE_TABLE_SCREEN
        search.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search.file_selector = self.NAME_SELECTOR
        search.col_selector = self.COL_SELECTOR
        value = search.get_value(search_item)
        return value

    def delete_job(self, title_job):

        selector = DeleteRegister(self.driver)
        selector.visible_table = self.VISIBLE_TABLE
        selector.rows_selector = self.ROWS_SELECTOR
        selector.name_selector = self.NAME_SEL
        selector.col_selector = self.COL_SEL
        selector.button_check = self.BUTTON_CHECK
        selector.button_delete = self.BUTTON_DELETE
        selector.screen_data = self.SCREEN_DELETE
        selector.button_new_screen = self.BUTTON_OK
        selector.title = self.TITLE_JOB
        value = selector.registration(title_job)

        return value



