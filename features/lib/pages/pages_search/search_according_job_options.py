from lib.pages.pages_search.base_page import OrangeBasePage


class SearchInJobOptions(OrangeBasePage):

    visible_selector = ''
    table_rows_selector = ''
    file_selector = ''
    col_selector = ''
    LIST_JOBS = []

    def added_job_option(self, search_item):

        self.wait_selector_visible(self.visible_selector)
        self.wait_button_clickable(self.visible_selector)

        rows_count = len(self.driver.find_elements(*self.table_rows_selector))

        for a in range(1, rows_count + 1):
            value = self.driver.find_element_by_xpath(self.file_selector + 'tr[' + str(a) + ']' + self.col_selector)

            self.LIST_JOBS.append(value.text)

        if search_item in self.LIST_JOBS:
            return True
        else:
            return False
