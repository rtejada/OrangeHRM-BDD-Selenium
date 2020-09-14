from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
import os
import json
from random import randint


class PersonalData(OrangeBasePage):

    CONTACT_INFO = (By.LINK_TEXT, 'Datos de contacto')
    BUTTON_EDIT = (By.ID, 'btnSave')
    CONTACT_STREET1 = (By.ID, 'contact_street1')
    CONTACT_STREET2 = (By.ID, 'contact_street2')
    CONTACT_CITY = (By.ID, 'contact_city')
    CONTACT_PROVINCE = (By.ID, 'contact_province')
    CONTACT_CODE = (By.ID, 'contact_emp_zipcode')
    CONTACT_COUNTRY = (By.ID, 'contact_country')
    CONTACT_PHONE = (By.ID, 'contact_emp_hm_telephone')
    CONTACT_MOBILE = (By.ID, 'contact_emp_mobile')
    CONTACT_WORK_PHONE = (By.ID, 'contact_emp_work_telephone')
    CONTACT_WORK_EMAIL = (By.ID, 'contact_emp_work_email')
    CONTACT_OTHER_EMAIL = (By.ID, 'contact_emp_oth_email')
    BUTTON_SAVE = (By.ID, 'btnSave')


    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/personal_details.json") as file:
            self.PERSONAL_DATA = json.load(file)

        self.address_1 = self.PERSONAL_DATA['address_1'] + ' ' + self.random_letter(5)
        self.address_2 = self.PERSONAL_DATA['address_2'] + ' ' + self.random_letter(5)
        self.city = self.PERSONAL_DATA['city']
        self.state_province = self.PERSONAL_DATA['state_province'] + ' ' + self.random_letter(7)
        self.code = self.PERSONAL_DATA['code'] + str(randint(1000, 70000))
        self.country = self.PERSONAL_DATA['country']
        self.home_phone = self.PERSONAL_DATA['home_phone'] + str(randint(9000, 900000))
        self.mobile = self.PERSONAL_DATA['mobile'] + str(randint(90000, 9000000))
        self.phone = self.PERSONAL_DATA['phone'] + str(randint(90000, 9000000))
        self.email = self.random_letter(7) + self.PERSONAL_DATA['email']
        self.other_email = self.random_letter(7) + self.PERSONAL_DATA['other_email']

    def data_of_contact(self):

        self.wait_button_clickable(self.CONTACT_INFO)

        self.click_button(self.CONTACT_INFO)

        self.wait_button_clickable(self.BUTTON_EDIT)

        self.click_button(self.BUTTON_EDIT)

        self.fill_text_field(self.CONTACT_STREET1, self.address_1)

        self.fill_text_field(self.CONTACT_STREET2, self.address_2)

        self.fill_text_field(self.CONTACT_CITY, self.city)

        self.fill_text_field(self.CONTACT_PROVINCE, self.state_province)

        self.fill_text_field(self.CONTACT_CODE, self.code)

        self.fill_select_by_text(self.CONTACT_COUNTRY, self.country)

        self.fill_text_field(self.CONTACT_PHONE, self.home_phone)

        self.fill_text_field(self.CONTACT_MOBILE, self.mobile)

        self.fill_text_field(self.CONTACT_WORK_PHONE, self.phone)

        self.fill_text_field(self.CONTACT_WORK_EMAIL, self.email)

        self.fill_text_field(self.CONTACT_OTHER_EMAIL, self.other_email)

        self.send_enter_key(self.BUTTON_SAVE)




