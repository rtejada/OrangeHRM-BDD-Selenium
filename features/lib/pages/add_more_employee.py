from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By


class AddMoreEmployee(OrangeBasePage):

    LIST_NAME_SHIFT = []
    LIST_CONFIRM = []
    FORM_LIST = (By.ID, 'frmList_ohrmListComponent')
    VISIBLE_TABLE = (By.ID, 'ohrmList_chkSelectAll')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[2]/a'
    VISIBLE_TITLE = (By.ID, 'workShiftHeading')
    AVAILABLE_EMPLOYEES = (By.ID, 'workShift_availableEmp')
    ADD = (By.ID, 'btnAssignEmployee')
    BUTTON_SAVE = (By.ID, 'btnSave')

    def more_shifts(self, shift, employee):

        self.wait_selector_visible(self.FORM_LIST)

        self.wait_button_clickable(self.VISIBLE_TABLE)

        rows_count = len(self.driver.find_elements(*self.TABLE_ROWS_SELECTOR))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element(By.XPATH, (self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.COL_SELECTOR))

            self.LIST_NAME_SHIFT.append(value.text)

        if shift in self.LIST_NAME_SHIFT:

            self.click_link_text(shift)

        self.wait_selector_visible(self.VISIBLE_TITLE)

        self.fill_select_by_text(self.AVAILABLE_EMPLOYEES, employee)
        self.click_button(self.ADD)

        self.send_enter_key(self.BUTTON_SAVE)

    def shifts(self, shift):

        self.wait_selector_visible(self.FORM_LIST)

        self.wait_button_clickable(self.VISIBLE_TABLE)

        rows_count = len(self.driver.find_elements(*self.TABLE_ROWS_SELECTOR))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element(By.XPATH, (self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.COL_SELECTOR))

            self.LIST_CONFIRM.append(value.text)

        return shift in self.LIST_CONFIRM





