from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from random import randint
import json
import uuid
import os


class OrganizationData(OrangeBasePage):

    ORGANIZATION_DATA = ''
    NAME_FIRM = (By.ID, 'organization_name')
    TAX = (By.ID, 'organization_taxId')
    REG_NUMBER = (By.ID, 'organization_registraionNumber')
    PHONE = (By.ID, 'organization_phone')
    FAX = (By.ID, 'organization_fax')
    EMAIL = (By.ID, 'organization_email')
    ADDRESS_1 = (By.ID, 'organization_street1')
    ADDRESS_2 = (By.ID, 'organization_street2')
    CITY = (By.ID, 'organization_city')
    STATE_PROV = (By.ID, 'organization_province')
    CODE = (By.ID, 'organization_zipCode')
    COUNTRY = (By.ID, 'organization_country')
    NOTE = (By.ID, 'organization_note')
    BUTTON_SAVE = (By.ID, 'btnSaveGenInfo')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/info_corp_structure.json") as file:
            self.ORGANIZATION_DATA = json.load(file)

        guid_let = str(uuid.uuid4())
        keywords = guid_let.split("-")

        self.name_firm = self.ORGANIZATION_DATA["name_firm"] + '-' + self.random_letter(10)
        self.tax = self.ORGANIZATION_DATA["CUIT"] + keywords[0]
        self.reg_number = self.ORGANIZATION_DATA["registration_number"] + keywords[4]
        self.phone = self.ORGANIZATION_DATA["phone"] + str(randint(100, 1000000000))
        self.fax = self.ORGANIZATION_DATA["fax"] + str(randint(1000, 1000000000))
        self.email = keywords[0] + self.ORGANIZATION_DATA["email"] + keywords[4] + '.com'
        self.address_1 = self.ORGANIZATION_DATA["address_1"] + ' ' + str(randint(1, 100))
        self.address_2 = self.ORGANIZATION_DATA["address_2"] + ' ' + str(randint(1, 100))
        self.city = self.ORGANIZATION_DATA["city"]
        self.state_province = self.ORGANIZATION_DATA["state_province"]
        self.code = self.ORGANIZATION_DATA["code"] + str(randint(5000, 500000))
        self.country = self.ORGANIZATION_DATA["country"]
        self.note = self.ORGANIZATION_DATA["note"] + self.random_letter(100)

    def info(self):

        self.fill_text_field(self.NAME_FIRM, self.name_firm)

        self.fill_text_field(self.TAX, self.tax)

        self.fill_text_field(self.REG_NUMBER, self.reg_number)

        self.fill_text_field(self.PHONE, self.phone)

        self.fill_text_field(self.FAX, self.fax)

        self.fill_text_field(self.EMAIL, self.email)

        self.fill_text_field(self.ADDRESS_1, self.address_1)

        self.fill_text_field(self.ADDRESS_2, self.address_2)

        self.fill_text_field(self.CITY, self.code)

        self.fill_text_field(self.STATE_PROV, self.state_province)

        self.fill_text_field(self.CODE, self.code)

        self.fill_select_by_text(self.COUNTRY, self.country)

        self.fill_text_field(self.NOTE, self.note)

        self.send_enter_key(self.BUTTON_SAVE)

    def get_name(self):

        return self.name_firm
