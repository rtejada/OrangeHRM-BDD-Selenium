from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
import os
import json
from random import randint


class AddSalary(OrangeBasePage):

    SALARY_SCALE = (By.ID, 'salary_sal_grd_code')
    SALARY_COMPONENT = (By.ID, 'salary_salary_component')
    SALARY_PAY_PERIOD = (By.ID, 'salary_payperiod_code')
    SALARY_CURRENCY = (By.ID, 'salary_currency_id')
    SALARY_BASIC = (By.ID, 'salary_basic_salary')
    SALARY_COMMENTS = (By.ID, 'salary_comments')
    SALARY_SET_DIRECT_DEBIT = (By.ID, 'salary_set_direct_debit')
    DIRECT_DEPOSIT_ACCOUNT = (By.ID, 'directdeposit_account')
    ACCOUNT_TYPE = (By.ID, 'directdeposit_account_type')
    ROUTING_NUMBER = (By.ID, 'directdeposit_routing_num')
    DIRECT_DEPOSIT_AMOUNT = (By.ID, 'directdeposit_amount')
    SAVE = (By.ID, 'btnSalarySave')

    def __init__(self, driver):
        super().__init__(driver)

        with open(os.getcwd() + "/features/lib/data/personal_details.json") as file:
            self.PERSONAL_DATA = json.load(file)

        self.salary_component = self.random_letter(10)
        self.period = self.PERSONAL_DATA["period"]
        self.money = self.PERSONAL_DATA["money"]
        self.account_type = self.PERSONAL_DATA["account_type"]
        self.comment = self.random_letter(50)
        self.account_number = str(randint(1, 9999999999))

    def enter_concepts(self, salary_scale):

        self.fill_select_by_text(self.SALARY_SCALE, salary_scale["escala_salarial"])
        self.fill_text_field(self.SALARY_COMPONENT, self.salary_component)
        self.fill_select_by_text(self.SALARY_PAY_PERIOD, self.period)
        self.fill_select_by_text(self.SALARY_CURRENCY, self.money)
        self.fill_text_field(self.SALARY_BASIC, salary_scale["monto"])
        self.fill_text_field(self.SALARY_COMMENTS, self.comment)
        self.click_button(self.SALARY_SET_DIRECT_DEBIT)
        self.fill_text_field(self.DIRECT_DEPOSIT_ACCOUNT, self.account_number)
        self.fill_select_by_text(self.ACCOUNT_TYPE, self.account_type)
        self.fill_text_field(self.ROUTING_NUMBER, self.account_number)
        self.fill_text_field(self.DIRECT_DEPOSIT_AMOUNT, salary_scale["monto"])
        self.send_enter_key(self.SAVE)

    def get_salary_component(self):

        return self.salary_component











