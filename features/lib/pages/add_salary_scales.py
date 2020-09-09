from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.pages_search.search_result_table import SearchElement
from lib.pages.delete_register import DeleteRegister
from selenium.webdriver.common.by import By


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

    ASSIGNED_CURRENCIES = (By.ID, 'currencyListHeading')
    VISIBLE_TABLE_SCREEN = (By.ID, 'currencyCheckAll')
    VALUE_MAX_SALARY = (By.XPATH, '//*[@id="tblCurrencies"]/tbody/tr/td[4]')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="tblCurrencies"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="tblCurrencies"]/tbody/'
    COL_SELECTOR = '/td[4]'

    VISIBLE_TABLE = (By.ID, 'ohrmList_chkSelectAll')
    BUTTON_DELETE = (By.ID, 'btnDelete')
    SCREEN_DELETE = (By.ID, 'deleteConfModal')
    BUTTON_OK = (By.ID, 'dialogDeleteBtn')
    TITLE_JOB = (By.XPATH, '//*[@id="resultTable"]/tbody/tr/td/a')
    ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SEL = '//*[@id="resultTable"]/tbody/'
    COL_SEL = '/td[2]/a'
    BUTTON_CHECK = '/td[1]'

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

        self.wait_selector_visible(self.ASSIGNED_CURRENCIES)

        self.wait_button_clickable(self.VISIBLE_TABLE_SCREEN)

        max_salary = self.driver.find_element(*self.VALUE_MAX_SALARY).text
        return max_salary

    def search_max_salary(self, search_item):

        search = SearchElement(self.driver)
        search.visible_selector = self.VISIBLE_TABLE_SCREEN
        search.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search.file_selector = self.NAME_SELECTOR
        search.col_selector = self.COL_SELECTOR
        value = search.get_value(search_item)
        return value

    def del_title_salary_scale(self, title):

        self.click_button(self.ADMIN)

        self.wait_selector_visible(self.JOBS_TITLE_LISTS)

        self.menu_select_option(self.JOBS_TITLE_LISTS, self.SALARY_SCALE_TITLE)

        self.wait_button_clickable(self.BUTTON_ADD)

        selector = DeleteRegister(self.driver)
        selector.visible_table = self.VISIBLE_TABLE
        selector.rows_selector = self.ROWS_SELECTOR
        selector.name_selector = self.NAME_SEL
        selector.col_selector = self.COL_SEL
        selector.button_check = self.BUTTON_CHECK
        selector.button_delete = self.BUTTON_DELETE
        selector.screen_data = self.SCREEN_DELETE
        selector.button_new_screen = self.BUTTON_OK
        value = selector.registration(title)
        return value






