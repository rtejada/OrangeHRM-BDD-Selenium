from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By


class DeleteRegister(OrangeBasePage):

    BUTTON_DELETE = (By.ID, 'btnDelete')
    SCREEN_DELETE = (By.ID, 'deleteConfModal')
    BUTTON_OK = (By.ID, 'dialogDeleteBtn')
    TITLE_JOB = (By.XPATH, '//*[@id="resultTable"]/tbody/tr/td/a')
    VISIBLE_TABLE_SCREEN = (By.ID, 'ohrmList_chkSelectAll')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[2]/a'
    BUTTON = '/td[1]'
    LIST_REGISTERS = []

    def registration(self, selector):

        self.wait_selector_visible(self.VISIBLE_TABLE_SCREEN)
        self.wait_button_clickable(self.VISIBLE_TABLE_SCREEN)

        rows_col = len(self.driver.find_elements(*self.TABLE_ROWS_SELECTOR))

        for a in range(1, rows_col + 1):
            button = self.driver.find_element_by_xpath(self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.BUTTON)
            value = self.driver.find_element_by_xpath(self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.COL_SELECTOR).text

            if value == selector:
                button.click()
                break

        self.wait_selector_visible(self.BUTTON_DELETE)

        self.wait_button_clickable(self.BUTTON_DELETE)

        self.click_button(self.BUTTON_DELETE)

        self.wait_selector_visible(self.SCREEN_DELETE)

        self.wait_button_clickable(self.BUTTON_OK)

        self.click_button(self.BUTTON_OK)

        self.wait_selector_visible(self.VISIBLE_TABLE_SCREEN)
        self.wait_button_clickable(self.VISIBLE_TABLE_SCREEN)

        rows_count = len(self.driver.find_elements(*self.TABLE_ROWS_SELECTOR))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.COL_SELECTOR)

            self.LIST_REGISTERS.append(value.text)

        return selector not in self.LIST_REGISTERS




