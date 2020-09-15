from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By


class ConfirmRegisters(OrangeBasePage):
    personal_information_module = ''
    employee_list = ''
    search_id = ''
    search = ''
    result_table = ''
    table_rows_selector = ''
    file_selector = ''
    col_selector = ''
    list_data = []

    def register(self, search):

        id = search['id']
        title = search['title']

        self.wait_selector_visible(self.personal_information_module)

        self.wait_button_clickable(self.personal_information_module)

        self.click_button(self.personal_information_module)

        self.wait_selector_visible(self.employee_list)

        self.wait_button_clickable(self.employee_list)

        self.click_button(self.employee_list)

        self.fill_text_field(self.search_id, id)

        self.click_button(self.search)

        self.wait_button_clickable(self.result_table)

        rows_count = len(self.driver.find_elements(*self.table_rows_selector))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element(By.XPATH, (self.file_selector + 'tr[' + str(a) + ']' + self.col_selector))
            self.list_data.append(value.text)

        return title in self.list_data

