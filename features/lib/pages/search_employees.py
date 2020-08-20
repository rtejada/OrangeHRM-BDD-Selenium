from lib.pages.base_page import OrangeBasePage
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class OrangeSiteSearchEmployee(OrangeBasePage):

    menu_selector = ''
    menu_selector_id = ''
    result_table = ''
    table_rows_selector = ''
    name_selector = ''
    col_selector = ''
    list_names = []

    def search_element(self, search_item):

        self.wait_button_clickable(self.menu_selector)

        time.sleep(2)

        self.click_button(self.menu_selector)

        self.wait_button_clickable(self.result_table)

        self.window_scroll_half()

        rows_count = len(self.driver.find_elements(*self.table_rows_selector))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.name_selector + 'tr[' + str(a) + ']' + self.col_selector)

            self.list_names.append(value.text)

        if search_item in self.list_names:
            return True
        else:
            return False


