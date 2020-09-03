from lib.pages.pages_search.base_page import OrangeBasePage


class OrangeSiteSearchList(OrangeBasePage):

    menu_selector = ''
    personal_detail = ''
    result_table = ''
    table_rows_selector = ''
    name_selector = ''
    col_selector = ''
    list_searchs = []

    def search_element(self, search_item):

        self.wait_selector_visible(self.personal_detail)

        self.wait_button_clickable(self.menu_selector)

        self.click_button(self.menu_selector)

        self.wait_selector_visible(self.result_table)

        self.wait_button_clickable(self.result_table)

        self.window_scroll_half()

        rows_count = len(self.driver.find_elements(*self.table_rows_selector))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.name_selector + 'tr[' + str(a) + ']' + self.col_selector)

            self.list_searchs.append(value.text)

        if search_item in self.list_searchs:
            return True
        else:
            return False


