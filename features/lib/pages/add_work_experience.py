from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
import os
import json


class CurriculumVitae(OrangeBasePage):

    ADD_WORK_EXPERIENCE = (By.ID, 'addWorkExperience')
    FORM_WORK_EXPERIENCE = (By.ID, 'frmWorkExperience')
    COMPANY = (By.ID, 'experience_employer')
    JOB_TITLE = (By.ID, 'experience_jobtitle')
    EXP_FROM_DATE = (By.ID, 'experience_from_date')
    VISIBLE_CALENDAR = (By.ID, 'ui-datepicker-div')
    YEAR = (By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[2]')
    DATE = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/personal_details.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.year = self.DATA_EMPLOYEE['year']

    def work_experience(self, data):

        self.click_button(self.ADD_WORK_EXPERIENCE)

        self.wait_selector_visible(self.FORM_WORK_EXPERIENCE)

        self.fill_text_field(self.COMPANY, data['company'])

        self.fill_text_field(self.JOB_TITLE, data['post'])

        self.click_button(self.EXP_FROM_DATE)

        self.wait_selector_visible(self.VISIBLE_CALENDAR)

        self.wait_button_clickable(self.YEAR)

        self.fill_select_field(self.YEAR, self.DATE)


