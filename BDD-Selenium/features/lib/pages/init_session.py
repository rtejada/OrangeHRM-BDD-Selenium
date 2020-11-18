from selenium.webdriver.common.by import By
from lib.pages.pages_search.base_page import OrangeBasePage
import os


class StartSessionPage(OrangeBasePage):

    URL_ORANGE = ''
    USER = ''
    PWD = ''
    USERNAME = (By.ID, 'txtUsername')
    PASSWORD = (By.ID, 'txtPassword')
    LOGIN = (By.ID, 'btnLogin')

    def __init__(self, driver):

        super().__init__(driver)
        self.load_variables()

    def load_variables(self):
        self.URL_ORANGE = os.getenv("URL_OrangeHRM")
        self.USER = os.getenv("USERNAME")
        self.PWD = os.getenv("USERNAME_PWD")

    def load(self):
        self.driver.get(self.URL_ORANGE)

    def login_user(self):

        self.fill_text_field(self.USERNAME, self.USER)

        self.fill_text_field(self.PASSWORD, self.PWD)

        self.click_button(self.LOGIN)

