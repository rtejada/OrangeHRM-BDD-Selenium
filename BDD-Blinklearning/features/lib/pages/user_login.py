from selenium.webdriver.common.by import By
from lib.pages.base_page import BasePage
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class UserLogin(BasePage):

    URL_BLINKLEARNING = ''
    NAME = ''
    SURNAME = ''
    PASSWORD = ''
    INIT_SESSION = (By.LINK_TEXT, "Iniciar sesión")
    FIELD_EMAIL = (By.ID, 'email')
    FIELD_PASSWORD = (By.ID, 'contrasena')
    BUTTON_LOGIN = (By.ID, 'login')

    def __init__(self, driver):

        super().__init__(driver)
        self.load_variables()

    def load_variables(self):
        self.URL_BLINKLEARNING = os.getenv("URL_PAGE")

    def load_url(self):
        self.driver.get(self.URL_BLINKLEARNING)

    def load_login_page(self, email, password):

        self.wait_selector_visible(self.INIT_SESSION)
        self.click_button(self.INIT_SESSION)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        self.wait_selector_visible(self.FIELD_EMAIL)
        self.fill_text_field(self.FIELD_EMAIL, email)
        self.fill_text_field(self.FIELD_PASSWORD, password)

    def register(self):

        self.click_button(self.BUTTON_LOGIN)

        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text

        except TimeoutException:
            return "no alert"







