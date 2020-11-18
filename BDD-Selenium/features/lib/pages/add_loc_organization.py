from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from random import randint
import json
import os


class LocationData(OrangeBasePage):

    LOCATIONS = ''
    NAME = (By.ID, 'location_name')
    COUNTRY = (By.ID, 'location_country')
    PROVINCE = (By.ID, 'location_province')
    CITY = (By.ID, 'location_city')
    ADDRESS = (By.ID, 'location_address')
    CP = (By.ID, 'location_zipCode')
    PHONE = (By.ID, 'location_phone')
    FAX = (By.ID, 'location_fax')
    NOTE = (By.ID, 'location_notes')
    SAVE = (By.ID, 'btnSave')
    
    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/BDD-Selenium/features/lib/data/info_corp_structure.json") as file:
            self.LOCATIONS = json.load(file)      

        self.first_name = self.LOCATIONS["first_name"] + self.random_letter(10)
        self.country = self.LOCATIONS["country"]
        self.state_province = self.LOCATIONS["state_province"]
        self.address_1 = self.LOCATIONS["address_1"] + ' ' + str(randint(1, 100))
        self.code = self.LOCATIONS["code"] + str(randint(5000, 500000))
        self.phone = self.LOCATIONS["phone"] + str(randint(100, 1000000000))
        self.fax = self.LOCATIONS["fax"] + str(randint(1000, 1000000000))
        self.note = self.LOCATIONS["note"] + self.random_letter(100)

    def info(self, name, city):

        self.first_name = self.first_name + ' ' + name

        self.fill_text_field(self.NAME, self.first_name)

        self.fill_select_by_text(self.COUNTRY, self.country)

        self.fill_text_field(self.PROVINCE, self.state_province)

        self.fill_text_field(self.CITY, city)

        self.fill_text_field(self.ADDRESS, self.address_1)

        self.fill_text_field(self.CP, self.code)

        self.fill_text_field(self.PHONE, self.phone)

        self.fill_text_field(self.FAX, self.fax)

        self.fill_text_field(self.NOTE, self.note)

        self.send_enter_key(self.SAVE)

    def get_first_name(self):

        return self.first_name
