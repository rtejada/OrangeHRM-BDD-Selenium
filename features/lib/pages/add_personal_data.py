from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from random import randint
import os
import json
import uuid


class DataPersonalEmployee(OrangeBasePage):

    RESULT_DATA = (By.ID, 'tableWrapper')
    BUTTON_EDIT = (By.ID, 'btnSave')
    BUTTON_SAVE = (By.ID, 'btnSave')
    SAVE = 'btnSave'

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/data_users.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

    def personal_data(self, id_employee):

        self.wait_button_clickable(self.RESULT_DATA)

        self.click_link_text(id_employee)

        self.click_button(self.BUTTON_EDIT)


