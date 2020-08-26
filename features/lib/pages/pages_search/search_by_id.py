from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By


class OrangeSiteSearchId(OrangeBasePage):

    SEARCH = (By.ID, 'searchBtn')
    personal_detail = ''
    menu_selector = ''
    employee = ''
    identification = ''
    table_row_selector = ''

    def employee_id(self):

        self.wait_selector_visible(self.personal_detail)

        self.wait_button_clickable(self.menu_selector)

        self.click_button(self.menu_selector)

        self.fill_text_field(self.employee, self.identification)

        self.send_enter_key(self.SEARCH)

        rows = len(self.driver.find_elements(*self.table_row_selector))

        return rows >= 1
