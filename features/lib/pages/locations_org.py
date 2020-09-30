from lib.pages.pages_search.base_page import OrangeBasePage
from lib.pages.add_loc_organization import LocationData
from selenium.webdriver.common.by import By


class CompanyLocations(OrangeBasePage):

    ADMIN = (By.LINK_TEXT, 'Administrador')
    ORG_STRUCTURE = (By.ID, 'menu_admin_Organization')
    LOCATIONS = (By.ID, 'menu_admin_viewLocations')
    VISIBLE_SCREEN = (By.ID, 'location-information')
    CONTENT_STRUCTURE = (By.ID, 'content')
    BUTTON_ADD = (By.ID, 'btnAdd')
    BUTTON_SEARCH = (By.ID, 'btnSearch')
    NAME = (By.ID, 'searchLocation_name')
    CHECK_SELECT_ALL = (By.ID, 'ohrmList_chkSelectAll')

    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="resultTable"]/tbody/tr')
    NAME_SELECTOR = '//*[@id="resultTable"]/tbody/'
    COL_SELECTOR = '/td[2]/a'
    BUTTON_CHECK = '/td[1]'
    BUTTON_DELETE = (By.ID, 'btnDelete')
    SCREEN_DELETE = (By.ID, 'deleteConfModal')
    BUTTON_OK = (By.ID, 'dialogDeleteBtn')

    def select_menu(self):

        self.click_button(self.ADMIN)

        self.wait_selector_visible(self.ORG_STRUCTURE)

        self.menu_select_option(self.ORG_STRUCTURE, self.LOCATIONS)

        self.wait_selector_visible(self.VISIBLE_SCREEN)

        self.click_button(self.BUTTON_ADD)

    def add_locations(self, first_name, city):

        data_org = LocationData(self.driver)
        data_org.info(first_name, city)
        name = data_org.get_first_name()
        return name

    def confirm(self, first_name):

        self.wait_selector_visible(self.CONTENT_STRUCTURE)

        self.fill_text_field(self.NAME, first_name)

        self.click_button(self.BUTTON_SEARCH)

        self.wait_button_clickable(self.CHECK_SELECT_ALL)

        rows = len(self.driver.find_elements(By.XPATH, '//*[@id="resultTable"]/tbody/tr'))

        return rows >= 1

    def del_location(self):

        self.wait_button_clickable(self.CHECK_SELECT_ALL)

        self.click_button(self.CHECK_SELECT_ALL)

        self.wait_selector_visible(self.BUTTON_DELETE)

        self.wait_button_clickable(self.BUTTON_DELETE)

        self.click_button(self.BUTTON_DELETE)

        self.wait_selector_visible(self.SCREEN_DELETE)

        self.wait_button_clickable(self.BUTTON_OK)

        self.click_button(self.BUTTON_OK)

