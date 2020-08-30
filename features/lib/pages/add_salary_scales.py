from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.search_according_job_options import SearchInJobOptions
from selenium.webdriver.common.by import By
import os


class AddSalaryScales(OrangeBasePage):

    ADMIN = (By.LINK_TEXT, 'Administrador')
    JOBS = 'menu_admin_Job'
    JOBS_TITLE_LISTS = (By.ID, 'menu_admin_Job')
    SALARY_SCALE_TITLE = (By.ID, 'menu_admin_viewPayGrades')
    BUTTON_ADD = (By.ID, 'btnAdd')
    VISIBLE_TITLE = (By.ID, 'payGradeHeading')
    NAME_SCALE = (By.ID, 'payGrade_name')
    BUTTON_SAVE = (By.ID, 'btnSave')
    ADD_DATA = (By.ID, 'btnAddCurrency')
    MONEY = (By.ID, 'payGradeCurrency_currencyName')
    MIN_SALARY = (By.ID, 'payGradeCurrency_minSalary')
    MAX_SALARY = (By.ID, 'payGradeCurrency_maxSalary')
    SAVE_CURRENCY = (By.ID, 'btnSaveCurrency')
    ASSIGNED_CURRENCIES = (By.ID, 'assigned currencies')
    VISIBLE_TABLE_SCREEN = (By.ID, 'currencyCheckAll')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="tblCurrencies"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="tblCurrencies"]/tbody/'
    COL_SELECTOR = '/td[4]//a'

    def select_menu(self):

        self.click_button(self.ADMIN)

        self.wait_selector_visible(self.JOBS_TITLE_LISTS)

        self.menu_select_option(self.JOBS_TITLE_LISTS, self.SALARY_SCALE_TITLE)

    def add_salary_sacale(self, salary_list):

        self.wait_button_clickable(self.BUTTON_ADD)

        self.click_button(self.BUTTON_ADD)

        self.wait_selector_visible(self.VISIBLE_TITLE)

        self.wait_button_clickable(self.NAME_SCALE)

        self.fill_text_field(self.NAME_SCALE, salary_list['title_scale'])

        self.send_enter_key(self.BUTTON_SAVE)

        self.wait_selector_visible(self.ADD_DATA)

        self.wait_button_clickable(self.ADD_DATA)

        self.click_button(self.ADD_DATA)

        self.wait_selector_visible(self.MONEY)

        self.wait_button_clickable(self.MONEY)

        self.fill_text_field(self.MONEY, salary_list['currency'])

        self.fill_text_field(self.MIN_SALARY, salary_list['minimum_salary'])

        self.fill_text_field(self.MAX_SALARY, salary_list['maximum_salary'])

        self.send_enter_key(self.SAVE_CURRENCY)

    def search_jobs(self, search_item):

        pass



