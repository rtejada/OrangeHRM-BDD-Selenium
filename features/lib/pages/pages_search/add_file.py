from selenium import webdriver
from selenium.webdriver.common.by import By
import os


class AddFile:

    SEARCH_BUTTON = (By.ID, 'search_form_submit')

    def __init__(self, driver: webdriver):
        # type driver: Chrome

        self.driver = driver
        self.select_file = ''
        self.file_name = 'image1.jpeg'
        self.path = os.getcwd() + "/features/lib/data/images"

        """:type: Chrome"""

    def add_files(self):
        file_add = self.driver.find_element(*self.select_file)
        self.driver.execute_script("arguments[0].style.display = 'block';", file_add)
        file_add.send_keys(self.path + self.file_name)

    def add_img(self):

        self.driver.find_element(*self.select_file).send_keys(self.path + self.file_name)

