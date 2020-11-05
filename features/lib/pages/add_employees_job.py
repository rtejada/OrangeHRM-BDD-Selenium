from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
import os
import json


class EmployeeWorkplaceData(OrangeBasePage):

    JOB_POSITION = (By.LINK_TEXT, 'Puesto de Trabajo')
    BUTTON_EDIT = (By.ID, 'btnSave')
    JOB_TITLE = (By.ID, 'job_job_title')
    JOB_STATUS = (By.ID, 'job_emp_status')
    JOB_CATEGORY = (By.ID, 'job_eeo_category')
    JOB_DATE = (By.ID, 'job_joined_date')
    CALENDAR = (By.ID, 'ui-datepicker-div')
    DATE_ENTRY = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[3]/a')
    JOB_LOCATION = (By.ID, 'job_location')
    JOB_CONTRACT_START_DATE = (By.ID, 'job_contract_start_date')
    BUTTON_SAVE = (By.ID, 'btnSave')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/personal_details.json") as file:
            self.DATA_EMPLOYEE = json.load(file)

        self.status = self.DATA_EMPLOYEE['status']

    def job_details(self, work_data):

        self.wait_button_clickable(self.JOB_POSITION)
        self.click_button(self.JOB_POSITION)
        self.click_button(self.BUTTON_EDIT)
        self.fill_select_by_text(self.JOB_TITLE, work_data["title"])
        self.fill_select_by_text(self.JOB_STATUS, self.status)
        self.fill_select_by_text(self.JOB_CATEGORY, work_data["category"])
        self.click_button(self.JOB_DATE)
        self.wait_selector_visible(self.CALENDAR)
        self.wait_button_clickable(self.DATE_ENTRY)
        self.click_button(self.DATE_ENTRY)
        self.wait_selector_visible(self.JOB_LOCATION)
        self.fill_select_by_text(self.JOB_LOCATION, work_data["location"])
        self.click_button(self.JOB_CONTRACT_START_DATE)
        self.wait_selector_visible(self.CALENDAR)
        self.wait_button_clickable(self.DATE_ENTRY)
        self.click_button(self.DATE_ENTRY)
        self.click_button(self.BUTTON_SAVE)

