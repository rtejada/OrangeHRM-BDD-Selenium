from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: webdriver):
        # type driver: Chrome

        self.driver = driver
        """:type: Chrome"""

    def fill_text_field(self, selector, text):
        element = self.driver.find_element(*selector)
        element.click()
        element.clear()
        element.send_keys(text)

    def click_button(self, selector):
        element = self.driver.find_element(*selector)
        element.click()

    def click_by_javascript(self, id):

        self.driver.execute_script('document.getElementById("' + id + '").click()')

    def wait_button_clickable(self, locator, time=5):
        wait = WebDriverWait(self.driver, time, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(locator))

    def wait_selector_visible(self, locator, time=5):
        wait = WebDriverWait(self.driver, time, poll_frequency=1)
        wait.until(EC.visibility_of_element_located(locator))










