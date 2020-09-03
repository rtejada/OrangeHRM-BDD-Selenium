from lib.pages.pages_search.base_page import OrangeBasePage


class DeleteRegister(OrangeBasePage):

    LIST_REGISTERS = []
    visible_table = ''
    rows_selector = ''
    name_selector = ''
    col_selector = ''
    button_check = ''
    button_delete = ''
    screen_data = ''
    button_new_screen = ''

    def registration(self, selector):

        self.wait_selector_visible(self.visible_table)
        self.wait_button_clickable(self.visible_table)

        rows_col = len(self.driver.find_elements(*self.rows_selector))

        for a in range(1, rows_col + 1):
            button = self.driver.find_element_by_xpath(self.name_selector + 'tr[' + str(a) + ']' + self.button_check)
            value = self.driver.find_element_by_xpath(self.name_selector + 'tr[' + str(a) + ']' + self.col_selector).text

            if value == selector:
                button.click()
                break

        self.wait_selector_visible(self.button_delete)

        self.wait_button_clickable(self.button_delete)

        self.click_button(self.button_delete)

        self.wait_selector_visible(self.screen_data)

        self.wait_button_clickable(self.button_new_screen)

        self.click_button(self.button_new_screen)

        self.wait_selector_visible(self.visible_table)
        self.wait_button_clickable(self.visible_table)

        rows_count = len(self.driver.find_elements(*self.rows_selector))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.name_selector + 'tr[' + str(a) + ']' + self.col_selector)

            self.LIST_REGISTERS.append(value.text)

        return selector not in self.LIST_REGISTERS




