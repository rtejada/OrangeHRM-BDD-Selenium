from lib.pages.pages_search.base_page import OrangeBasePage
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
    COL_SELECTOR = '/td[3]//a'
    LIST_JOBS = []

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

        self.wait_selector_visible(self.VISIBLE_TABLE_SCREEN)
        self.wait_button_clickable(self.VISIBLE_TABLE_SCREEN)

        rows_count = len(self.driver.find_elements(*self.TABLE_ROWS_SELECTOR))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.COL_SELECTOR)

            self.LIST_JOBS.append(value.text)

        if search_item in self.LIST_JOBS:
            return True
        else:
            return False

