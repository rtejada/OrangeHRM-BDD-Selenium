from selenium import webdriver
from selenium.webdriver.common.by import By
from lib.pages.pages_search.base_page import OrangeBasePage
import os


class AddFile(OrangeBasePage):

    SCREEN_SELECT_FILE = (By.ID, 'addPaneAttachments')
    BUTTON_SELECT_FILE = (By.ID, 'ufile')
    COMMENTARY = (By.ID, 'txtAttDesc')
    SEARCH_BUTTON = (By.ID, 'search_form_submit')
    VISIBLE_SCREEN_LOAD = (By.ID, "frmEmpAttachment")
    BUTTON_ADD = (By.ID, 'btnAddAttachment')
    BUTTON_LOAD = (By.ID, 'btnSaveAttachment')
    VISIBLE_SCREEN = (By.XPATH, '//*[@id="attachmentList"]/div/h1')

    file_name = ''
    path = os.getcwd() + "/features/lib/data/images/"
    select_file = ''

    def add_files(self):

        file_add = self.driver.find_element(*self.select_file)
        self.driver.execute_script("arguments[0].style.display = 'block';", file_add)
        file_add.send_keys(self.path + self.file_name)

    def add_img(self, img):

        self.wait_selector_visible(self.VISIBLE_SCREEN)

        self.click_button(self.BUTTON_ADD)

        self.wait_selector_visible(self.SCREEN_SELECT_FILE)

        self.wait_button_clickable(self.BUTTON_SELECT_FILE)

        self.driver.find_element(*self.BUTTON_SELECT_FILE).send_keys(self.path + img)

        self.fill_text_field(self.COMMENTARY, self.random_letter(80))

        self.wait_selector_visible(self.VISIBLE_SCREEN_LOAD)

        self.wait_button_clickable(self.BUTTON_LOAD)

        self.send_enter_key(self.BUTTON_LOAD)

