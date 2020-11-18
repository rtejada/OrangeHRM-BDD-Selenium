from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.add_info_organization import OrganizationData
from selenium.webdriver.common.by import By


class OrgInformation(OrangeBasePage):

    ADMIN = (By.LINK_TEXT, 'Administrador')
    ORG_STRUCTURE = (By.ID, 'menu_admin_Organization')
    GENERAL_INFO = (By.ID, 'menu_admin_viewOrganizationGeneralInformation')
    COMPANY_STRUCTURE =(By.ID, 'menu_admin_viewCompanyStructure')
    VISIBLE_SCREEN = (By.ID, 'general-info')
    CONTENT_STRUCTURE = (By.ID, 'content')
    BUTTON_EDIT = (By.ID, 'btnSaveGenInfo')
    VALUE = (By.XPATH, '//*[@id="node_1"]')

    def select_menu(self):

        self.click_button(self.ADMIN)

        self.wait_selector_visible(self.ORG_STRUCTURE)

        self.menu_select_option(self.ORG_STRUCTURE, self.GENERAL_INFO)

        self.wait_selector_visible(self.VISIBLE_SCREEN)

        self.click_button(self.BUTTON_EDIT)

    def add_info(self):

        details = OrganizationData(self.driver)
        details.info()
        name_firm = details.get_name()
        return name_firm

    def confirm_data(self):

        self.wait_selector_visible(self.VISIBLE_SCREEN)

        self.wait_button_clickable(self.ADMIN)

        self.wait_selector_visible(self.ORG_STRUCTURE)

        self.menu_select_option(self.ORG_STRUCTURE, self.COMPANY_STRUCTURE)

        self.wait_selector_visible(self.CONTENT_STRUCTURE)

        name = self.driver.find_element(*self.VALUE).text

        return name.strip(' ')










