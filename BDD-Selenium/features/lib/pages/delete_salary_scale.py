from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By


class DeleteSalaryScale(OrangeBasePage):

    TABLE_ASSIGNED_CURRENCIES = (By.ID, 'currencyCheckAll')
    BUTTON_DELETE = (By.ID, 'btnDeleteCurrency')
    TABLE = (By.XPATH, '//*[@id="tblCurrencies"]/thead/tr')

    def salary_scale(self):

        self.wait_selector_visible(self.TABLE_ASSIGNED_CURRENCIES)
        self.wait_button_clickable(self.TABLE_ASSIGNED_CURRENCIES)

        self.click_button(self.TABLE_ASSIGNED_CURRENCIES)

        self.wait_button_clickable(self.BUTTON_DELETE)
        self.click_button(self.BUTTON_DELETE)

        self.wait_selector_visible(self.TABLE_ASSIGNED_CURRENCIES)
        self.wait_button_clickable(self.TABLE_ASSIGNED_CURRENCIES)

        rows = len(self.driver.find_elements(*self.TABLE))

        if rows == 1:
            return True
