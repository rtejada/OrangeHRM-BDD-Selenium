from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
import os
import json


class CurriculumVitae(OrangeBasePage):

    ADD_WORK_EXPERIENCE = (By.ID, 'addWorkExperience')
    CHANGE_WORK_EXPERIENCE = (By.ID, 'changeWorkExperience')
    FORM_WORK_EXPERIENCE = (By.ID, 'frmWorkExperience')
    COMPANY = (By.ID, 'experience_employer')
    JOB_TITLE = (By.ID, 'experience_jobtitle')
    EXP_FROM_DATE = (By.ID, 'experience_from_date')
    VISIBLE_CALENDAR = (By.ID, 'ui-datepicker-div')
    YEAR = (By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/select[2]')
    DATE = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a')
    EXP_TO_DATE = (By.ID, 'experience_to_date')
    COMMENT = (By.ID, 'experience_comments')
    SAVE = (By.ID, 'btnWorkExpSave')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/BDD-Selenium/features/lib/data/personal_details.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.year_from = self.DATA_EMPLOYEE['year_from']
        self.year_to = self.DATA_EMPLOYEE['year_to']
        self.comment = self.DATA_EMPLOYEE['comment'] + self.random_letter(120)

    def work_experience(self, data):

        self.click_button(self.ADD_WORK_EXPERIENCE)
        self.wait_selector_visible(self.CHANGE_WORK_EXPERIENCE)
        self.wait_selector_visible(self.FORM_WORK_EXPERIENCE)
        self.wait_selector_visible(self.COMPANY)

        self.fill_text_field(self.COMPANY, data['company'])

        self.fill_text_field(self.JOB_TITLE, data['post'])

        self.click_button(self.EXP_FROM_DATE)

        self.wait_selector_visible(self.VISIBLE_CALENDAR)

        self.wait_button_clickable(self.YEAR)

        self.fill_select_field(self.YEAR, str(self.year_from))

        self.click_button(self.DATE)

        self.click_button(self.EXP_TO_DATE)

        self.wait_selector_visible(self.VISIBLE_CALENDAR)

        self.wait_button_clickable(self.YEAR)

        self.fill_select_field(self.YEAR, str(self.year_to))

        self.click_button(self.DATE)

        self.fill_text_field(self.COMMENT, self.comment)

        self.send_enter_key(self.SAVE)



