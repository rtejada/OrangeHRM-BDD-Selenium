from selenium import webdriver
from selenium.webdriver.common.by import By


class SuitecrmSiteSearch:

    SEARCH_BUTTON = (By.ID, 'search_form_submit')

    def __init__(self, driver: webdriver):
        # type driver: Chrome

        self.window_before = ''
        self.driver = driver
        self.selector_open_window = ''
        self.selector_search_field = ''
        self.search_query = ''
        self.filled = False

        """:type: Chrome"""

    def open_site_search(self):
        search = self.driver.find_element(*self.selector_open_window)
        self.window_before = self.driver.window_handles[0]
        search.click()

        window_after = self.driver.window_handles[1]

        self.driver.switch_to.window(window_after)

        if not self.filled:

            element = self.driver.find_element(*self.selector_search_field)
            element.click()
            element.clear()
            element.send_keys(self.search_query)

            button_search = self.driver.find_element(*self.SEARCH_BUTTON)
            button_search.click()

        click_name = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.search_query)
        click_name.click()

        self.driver.switch_to.window(self.window_before)

