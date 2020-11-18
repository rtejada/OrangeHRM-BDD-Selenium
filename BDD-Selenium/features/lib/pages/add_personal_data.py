from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from lib.pages.pages_search.confirm_registration import ConfirmRegisters
from random import randint


class DataPersonalEmployee(OrangeBasePage):

    RESULT_DATA = (By.ID, 'tableWrapper')
    MAIN_CONTAINER = (By.ID, 'pdMainContainer')
    EMERGENCY_CONTACTS = (By.LINK_TEXT, 'Contactos de Emergencia')
    FAMILY_BURDENS = (By.LINK_TEXT, 'Cargas Familiares')
    LIST_EMERGENCY_CONTACTS = (By.ID, 'listEmegrencyContact')
    ADD_CONTACT = (By.ID, 'btnAddContact')
    EMERGENCY_CONTACT_NAME = (By.ID, 'emgcontacts_name')
    CONTACT_RELATION = (By.ID, 'emgcontacts_relationship')
    HOME_PHONE = (By.ID, 'emgcontacts_homePhone')
    MOBILE = (By.ID, 'emgcontacts_mobilePhone')
    WORK_PHONE = (By.ID, 'emgcontacts_workPhone')
    BUTTON_SAVE = (By.ID, 'btnSaveEContact')
    CONTAINER_DATA = (By.ID, 'listEmegrencyContact')
    CHECK_ALl_DATA = (By.ID, 'checkAll')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="emgcontact_list"]/tbody/tr')
    FILE_SELECTOR = '//*[@id="emgcontact_list"]/tbody/'
    COL_SELECTOR = '/td[2]'
    LISTING_FAMILY_BURDENS = (By.ID, 'listing')
    ADD_DEPENDENT = (By.ID, 'btnAddDependent')
    DEPENDENT_NAME = (By.ID, 'dependent_name')
    DEPENDENT_RELATION_TYPE = (By.ID, 'dependent_relationshipType')
    DEPENDENT = 'Otro'
    DEPENDENT_RELATION_SHIP = (By.ID, 'dependent_relationship')
    DEPENDENT_DATE_BIRTH = (By.ID, 'dependent_dateOfBirth')
    VISIBLE_CALENDAR = (By.ID, 'ui-datepicker-div')
    DAY = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[3]/a')
    BUTTON_SAVE_DEPENDENT = (By.ID, 'btnSaveDependent')
    TABLE_ROWS_FAMILY = (By.XPATH, '//*[@id="dependent_list"]/tbody/tr')
    FILE_SELECTOR_FAMILY = '//*[@id="dependent_list"]/tbody/'
    COL_SELECTOR_FAMILY = '/td[2]'

    def access_emergency_contact(self, id_employee):

        self.wait_button_clickable(self.RESULT_DATA)
        self.click_link_text(id_employee)
        self.wait_selector_visible(self.MAIN_CONTAINER)
        self.click_button(self.EMERGENCY_CONTACTS)

    def emergency_contacts(self):

        emergency_contact_name = self.random_letter(15)
        self.wait_selector_visible(self.LIST_EMERGENCY_CONTACTS)
        self.click_button(self.ADD_CONTACT)
        self.fill_text_field(self.EMERGENCY_CONTACT_NAME, emergency_contact_name)
        self.fill_text_field(self.CONTACT_RELATION, self.random_letter(15))
        self.fill_text_field(self.HOME_PHONE, str(randint(1, 9999999999)))
        self.fill_text_field(self.MOBILE, str(randint(1, 9999999999)))
        self.fill_text_field(self.WORK_PHONE, str(randint(1, 9999999999)))
        self.send_enter_key(self.BUTTON_SAVE)
        return emergency_contact_name

    def confirm_added_data(self, contact_name):

        data = ConfirmRegisters(self.driver)
        data.section_work = self.CONTAINER_DATA
        data.data_form = self.CHECK_ALl_DATA
        data.table_rows_selector = self.TABLE_ROWS_SELECTOR
        data.file_selector = self.FILE_SELECTOR
        data.col_selector = self.COL_SELECTOR
        found = data.find_employee_records(contact_name)
        return found

    def access_family_burdens(self, id_employee):

        self.wait_button_clickable(self.RESULT_DATA)
        self.click_link_text(id_employee)
        self.wait_selector_visible(self.MAIN_CONTAINER)
        self.click_button(self.FAMILY_BURDENS)

    def family_burdens(self):

        name = self.random_letter(12)
        self.wait_selector_visible(self.LISTING_FAMILY_BURDENS)
        self.wait_button_clickable(self.ADD_DEPENDENT)
        self.click_button(self.ADD_DEPENDENT)
        self.fill_text_field(self.DEPENDENT_NAME, name)
        self.fill_select_by_text(self.DEPENDENT_RELATION_TYPE, self.DEPENDENT)
        self.fill_text_field(self.DEPENDENT_RELATION_SHIP, self.random_letter(14))
        self.click_button(self.DEPENDENT_DATE_BIRTH)
        self.wait_selector_visible(self.VISIBLE_CALENDAR)
        self.click_button(self.DAY)
        self.send_enter_key(self.BUTTON_SAVE_DEPENDENT)
        return name

    def confirm_data_family(self, contact_name):

        data = ConfirmRegisters(self.driver)
        data.section_work = self.LISTING_FAMILY_BURDENS
        data.data_form = self.CHECK_ALl_DATA
        data.table_rows_selector = self.TABLE_ROWS_FAMILY
        data.file_selector = self.FILE_SELECTOR_FAMILY
        data.col_selector = self.COL_SELECTOR_FAMILY
        found = data.find_employee_records(contact_name)
        return found





