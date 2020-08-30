from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By


class DeleteJob(OrangeBasePage):

    BUTTON_DELETE = (By.ID, 'btnDelete')

    VISIBLE_TABLE_SCREEN = (By.ID, 'ohrmList_chkSelectAll')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[2]/a'
    LIST_TITLE_JOBS = []

    def job(self, selector):

        self.wait_selector_visible(self.VISIBLE_TABLE_SCREEN)
        self.wait_button_clickable(self.VISIBLE_TABLE_SCREEN)

        rows_count = len(self.driver.find_elements(*self.TABLE_ROWS_SELECTOR))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.NAME_SELECTOR + 'tr[' + str(a) + ']' + self.COL_SELECTOR)

            self.LIST_TITLE_JOBS.append(value.text)

        self.LIST_TITLE_JOBS.remove(selector)

