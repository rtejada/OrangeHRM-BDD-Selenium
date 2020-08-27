from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.search_in_list import OrangeSiteSearchList
from selenium.webdriver.common.by import By
from random_word import RandomWords
from random import randint
import uuid


class AddNewJobs(OrangeBasePage):

    ADMIN = (By.LINK_TEXT, 'Administrador')
    JOBS = 'menu_admin_Job'
    JOBS_TITLE_LISTS = (By.ID, 'menu_admin_Job')
    JOB_TITLES = (By.ID, 'menu_admin_viewJobTitleList')
    BUTTON_ADD = (By.ID, 'btnAdd')
    JOB_TITLE = (By.ID, 'jobTitle_jobTitle')
    JOB_DESCRIPTION = (By.ID, 'jobTitle_jobDescription')
    SELECT_FILE = (By.ID, 'jobTitle_jobSpec')
    NOTE = (By.ID, 'jobTitle_note')
    BUTTON_SAVE = (By.ID, 'btnSave')

    def select_menu(self):

        self.click_button(self.ADMIN)

        self.wait_selector_visible(self.JOBS_TITLE_LISTS)

        self.menu_select_option(self.JOBS_TITLE_LISTS, self.JOB_TITLES)

    def add_jobs(self, list_jobs):

        self.wait_button_clickable(self.BUTTON_ADD)

        for i in range(len(list_jobs)):

            self.click_button(self.BUTTON_ADD)
            self.fill_text_field(self.JOB_TITLE, list_jobs[0])
            self.fill_text_field(self.JOB_DESCRIPTION, list_jobs[1])

            self.fill_text_field(self.NOTE, list_jobs[2])

