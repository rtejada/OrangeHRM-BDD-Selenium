from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.add_more_employee import AddMoreEmployee
from lib.pages.delete_register import DeleteRegister
from selenium.webdriver.common.by import By


class AddWorkingShift(OrangeBasePage):

    ADMIN = (By.LINK_TEXT, 'Administrador')
    JOBS_TITLE_LISTS = (By.ID, 'menu_admin_Job')
    WORK_SHIFTS = (By.ID, 'menu_admin_workShift')
    BUTTON_ADD = (By.ID, 'btnAdd')
    VISIBLE_TITLE = (By.ID, 'workShiftHeading')
    SHIFT_NAME = (By.ID, 'workShift_name')
    FROM = (By.ID, 'workShift_workHours_from')
    TO = (By.ID, 'workShift_workHours_to')
    AVAILABLE_EMPLOYEES = (By.ID, 'workShift_availableEmp')
    ADD = (By.ID, 'btnAssignEmployee')
    BUTTON_SAVE = (By.ID, 'btnSave')

    VISIBLE_TABLE = (By.ID, 'ohrmList_chkSelectAll')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SEL = '//*[@id="resultTable"]/tbody/'
    COL_SEL = '/td[2]/a'
    BUTTON_CHECK = '/td[1]'
    BUTTON_DELETE = (By.ID, 'btnDelete')
    SCREEN_DELETE = (By.ID, 'deleteConfModal')
    BUTTON_OK = (By.ID, 'dialogDeleteBtn')

    def select_menu(self):

        self.click_button(self.ADMIN)

        self.wait_selector_visible(self.JOBS_TITLE_LISTS)

        self.wait_button_clickable(self.JOBS_TITLE_LISTS)

        self.menu_select_option(self.JOBS_TITLE_LISTS, self.WORK_SHIFTS)

    def add_shift(self, workings_hours, employee):

        self.wait_button_clickable(self.BUTTON_ADD)

        self.click_button(self.BUTTON_ADD)

        self.wait_selector_visible(self.VISIBLE_TITLE)

        self.fill_text_field(self.SHIFT_NAME, workings_hours['nom_turno'])

        self.fill_select_field(self.FROM, workings_hours['desde'])

        self.fill_select_field(self.TO, workings_hours['hasta'])

        self.fill_select_by_text(self.AVAILABLE_EMPLOYEES, employee)
        self.click_button(self.ADD)

        self.send_enter_key(self.BUTTON_SAVE)

    def more_employees(self, shift, employee):

        work = AddMoreEmployee(self.driver)
        work.more_shifts(shift, employee)

    def confirm_data(self, shift):

        confirm = AddMoreEmployee(self.driver)
        value = confirm.shifts(shift)
        return value

    def del_work_shift(self, work_shift):

        selector = DeleteRegister(self.driver)
        selector.visible_table = self.VISIBLE_TABLE
        selector.rows_selector = self.TABLE_ROWS_SELECTOR
        selector.name_selector = self.NAME_SEL
        selector.col_selector = self.COL_SEL
        selector.button_check = self.BUTTON_CHECK
        selector.button_delete = self.BUTTON_DELETE
        selector.screen_data = self.SCREEN_DELETE
        selector.button_new_screen = self.BUTTON_OK
        value = selector.registration(work_shift)

        return value



