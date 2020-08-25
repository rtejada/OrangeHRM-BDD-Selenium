from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By


class SearchItems(OrangeBasePage):

    SEARCH = (By.ID, 'search_form_submit')

    access_option = ''
    press_filter = ''
    press_rapid_filter = ''
    visible_selector = ''
    contact_name = ''

    def search_user(self, item):

        self.wait_button_clickable(self.access_option)

        self.click_button(self.access_option)

        self.wait_selector_visible(self.press_filter)

        self.click_button(self.press_filter)

        self.wait_selector_visible(self.visible_selector)

        self.click_button(self.press_rapid_filter)

        self.wait_selector_visible(self.contact_name)

        self.fill_text_field(self.contact_name, item)

        self.send_enter_key(self.SEARCH)

        rows = len(self.driver.find_elements(By.XPATH, '//*[@id="MassUpdate"]/div[3]/table/tbody/tr/td[4]'))

        return rows >= 1
