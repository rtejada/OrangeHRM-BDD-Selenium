from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from lib.pages.pages_search.confirm_registration import ConfirmRegisters
from lib.pages.adding_monitory_data import AddingMonitoryData


class ReportTo(OrangeBasePage):

    RESULT_DATA = (By.ID, 'tableWrapper')
    MAIN_CONTAINER = (By.ID, 'pdMainContainer')
    REPORT_TO = (By.LINK_TEXT, 'Reporta a')
    CONTAINER_REPORT_SUP_DETAILS = (By.ID, 'listReportToSupDetails')
    CONTAINER_REPORT_COL_DETAILS = (By.ID, 'listReportToSubDetails')
    ADD_SUP_DETAILS = (By.ID, 'btnAddSupervisorDetail')
    ADD_COL_DETAILS = (By.ID, 'btnAddSubordinateDetail')
    SUPERVISOR = (By.ID, 'reportto_supervisorName_empName')
    COLLABORATOR = (By.ID, 'reportto_subordinateName_empName')
    AC_RESULTS = (By.CLASS_NAME, 'ac_results')
    LIST_ROWS = (By.XPATH, "//div[@class='ac_results']/ul/li")
    S_NAME = 'P'
    C_NAME = 'M'
    REPORT_METHOD = (By.ID, 'reportto_reportingMethodType')
    METHOD_SUPERVISOR = 'Directo'
    METHOD_COLLABORATOR = 'Indirecto'
    ADD_COLLABORATOR_DETAILS = (By.ID, 'btnAddSubordinateDetail')
    SAVE = (By.ID, 'btnSaveReportTo')

    CHECK_ALl_SUP = (By.ID, 'checkAllSup')
    TABLE_ROWS_SUP = (By.XPATH, '//*[@id="sup_list"]/tbody/tr')
    FILE_SELECTOR_SUP = '//*[@id="sup_list"]/tbody/'
    COL_SELECTOR_SUP = '/td[2]'
    DELETE_SUPERVISOR = (By.ID, 'delSupBtn')
    DELETE_COLLABORATOR = (By.ID, 'delSubBtn')

    CHECK_ALl_COLLAB = (By.ID, 'checkAllSub')
    TABLE_ROWS_COLLAB = (By.XPATH, '//*[@id="sub_list"]/tbody/tr')
    FILE_SELECTOR_COLLAB = '//*[@id="sub_list"]/tbody/'
    COL_SELECTOR_COLLAB = '/td[2]'

    def report_to(self, id_employee):

        self.wait_button_clickable(self.RESULT_DATA)
        self.click_link_text(id_employee)
        self.wait_selector_visible(self.MAIN_CONTAINER)
        self.click_button(self.REPORT_TO)

    def add_supervisor(self, supervisor):

        s = AddingMonitoryData(self.driver)
        s.container_report_to = self.CONTAINER_REPORT_SUP_DETAILS
        s.add_report_to = self.ADD_SUP_DETAILS
        s.add_name = self.SUPERVISOR
        s.first_letter = self.S_NAME
        s.container_ac_results = self.AC_RESULTS
        s.list_rows = self.LIST_ROWS
        s.report_method = self.REPORT_METHOD
        s.value_method = self.METHOD_SUPERVISOR
        s.save = self.SAVE
        s.adding_supervision_collaborator(supervisor)

    def confirm_added_supervisor_data(self, supervisor):

        name = supervisor[0:11]
        first_name = supervisor[21:]
        supervisor = name + first_name
        data = ConfirmRegisters(self.driver)
        data.section_work = self.CONTAINER_REPORT_SUP_DETAILS
        data.data_form = self.CHECK_ALl_SUP
        data.table_rows_selector = self.TABLE_ROWS_SUP
        data.file_selector = self.FILE_SELECTOR_SUP
        data.col_selector = self.COL_SELECTOR_SUP
        found = data.find_employee_records(supervisor)
        return found

    def delete_supervisor(self):

        self.wait_selector_visible(self.CONTAINER_REPORT_SUP_DETAILS)
        self.click_button(self.CHECK_ALl_SUP)
        self.wait_button_clickable(self.DELETE_SUPERVISOR)
        self.click_button(self.DELETE_SUPERVISOR)

    def add_collaborator(self, collaborator):

        c = AddingMonitoryData(self.driver)
        c.container_report_to = self.CONTAINER_REPORT_COL_DETAILS
        c.add_report_to = self.ADD_COL_DETAILS
        c.add_name = self.COLLABORATOR
        c.first_letter = self.C_NAME
        c.container_ac_results = self.AC_RESULTS
        c.list_rows = self.LIST_ROWS
        c.report_method = self.REPORT_METHOD
        c.value_method = self.METHOD_COLLABORATOR
        c.save = self.SAVE
        c.adding_supervision_collaborator(collaborator)

    def confirm_added_collaborator_data(self, collaborator):

        name = collaborator[0:11]
        first_name = collaborator[21:]
        collaborator = name + first_name
        data = ConfirmRegisters(self.driver)
        data.section_work = self.CONTAINER_REPORT_COL_DETAILS
        data.data_form = self.CHECK_ALl_COLLAB
        data.table_rows_selector = self.TABLE_ROWS_COLLAB
        data.file_selector = self.FILE_SELECTOR_COLLAB
        data.col_selector = self.COL_SELECTOR_COLLAB
        found = data.find_employee_records(collaborator)
        return found

    def delete_collaborator(self):
        self.wait_selector_visible(self.CONTAINER_REPORT_SUP_DETAILS)
        self.click_button(self.CHECK_ALl_COLLAB)
        self.wait_button_clickable(self.DELETE_COLLABORATOR)
        self.click_button(self.DELETE_COLLABORATOR)




