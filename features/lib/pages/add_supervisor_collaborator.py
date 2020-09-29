from lib.pages.pages_search.base_page import OrangeBasePage
from selenium.webdriver.common.by import By
from lib.pages.pages_search.confirm_registration import ConfirmRegisters


class ReportTo(OrangeBasePage):

    RESULT_DATA = (By.ID, 'tableWrapper')
    MAIN_CONTAINER = (By.ID, 'pdMainContainer')
    REPORT_TO = (By.LINK_TEXT, 'Reporta a')
    CONTAINER_REPORT_TO = (By.ID, 'listReportToSubDetails')
    ADD_SUPERVISOR_DETAILS = (By.ID, 'btnAddSupervisorDetail')
    SUPERVISOR = (By.ID, 'reportto_supervisorName_empName')
    COLLABORATOR = (By.ID, 'reportto_subordinateName_empName')
    AC_RESULTS = (By.CLASS_NAME, 'ac_results')
    LIST_ROWS = (By.XPATH, "//div[@class='ac_results']/ul/li")
    S_NAME = 'P'
    C_NAME = 'D'
    REPORT_METHOD = (By.ID, 'reportto_reportingMethodType')
    VALUE_SUPERVISOR = 'Directo'
    ADD_COLLABORATOR_DETAILS = (By.ID, 'btnAddSubordinateDetail')
    FORM_SUBORDINATES = (By.ID, 'frmEmpDelSubordinates')
    VALUE_COLLABORATOR = 'Indirecto'
    SAVE = (By.ID, 'btnSaveReportTo')
    SUPERVISORS = (By.ID, 'frmEmpDelSupervisors')
    COLLABORATORS = (By.ID, 'frmEmpDelSubordinates')
    CHECK_ALl_SUP = (By.ID, 'checkAllSup')

    TABLE_ROWS_SUP = (By.XPATH, '//*[@id="sup_list"]/tbody/tr')
    FILE_SELECTOR_SUP = '//*[@id="sup_list"]/tbody/'
    COL_SELECTOR_SUP = '/td[2]'

    CHECK_ALl_COLLAB = (By.ID, 'checkAllSub')
    TABLE_ROWS_COLLAB = (By.XPATH, '//*[@id="sub_list"]/tbody/tr')
    FILE_SELECTOR_COLLAB = '//*[@id="sub_list"]/tbody/'
    COL_SELECTOR_COLLAB = '/td[2]'

    def report_to(self, id_employee):

        self.wait_button_clickable(self.RESULT_DATA)
        self.click_link_text(id_employee)
        self.wait_selector_visible(self.MAIN_CONTAINER)
        self.click_button(self.REPORT_TO)

    def add_supervisor(self, report):

        self.wait_selector_visible(self.CONTAINER_REPORT_TO)
        self.click_button(self.ADD_SUPERVISOR_DETAILS)

        element = self.driver.find_element(*self.SUPERVISOR)
        element.click()
        element.send_keys(self.S_NAME)

        self.wait_selector_visible(self.AC_RESULTS)
        rows = self.driver.find_elements(*self.LIST_ROWS)

        count = 0
        selected = -1

        for row in rows:
            if row.text == report['supervisor']:
                selected = count
                break

            count += 1

        if selected >= 0:
            try:
                rows[selected].click()
            except Exception as e:
                return f'ERROR: {e}'

        self.fill_select_by_text(self.REPORT_METHOD, self.VALUE_SUPERVISOR)
        self.send_enter_key(self.SAVE)

    def add_collaborator(self, report):

        self.wait_selector_visible(self.CONTAINER_REPORT_TO)
        self.wait_selector_visible(self.FORM_SUBORDINATES)
        self.wait_button_clickable(self.ADD_COLLABORATOR_DETAILS)
        self.click_button(self.ADD_COLLABORATOR_DETAILS)
        element = self.driver.find_element(*self.COLLABORATOR)
        element.click()
        element.send_keys(self.C_NAME)

        self.wait_selector_visible(self.AC_RESULTS)
        rows = self.driver.find_elements(*self.LIST_ROWS)

        count = 0
        selected = -1

        for row in rows:
            if row.text == report['collaborator']:
                selected = count
                break

            count += 1

        if selected >= 0:
            try:
                rows[selected].click()
            except Exception as e:
                return f'Error: {e}'

        self.fill_select_by_text(self.REPORT_METHOD, self.VALUE_SUPERVISOR)
        self.send_enter_key(self.SAVE)

    def confirm_added_supervisor_data(self, supervisor):

        supervisor = supervisor[0:11]
        data = ConfirmRegisters(self.driver)
        data.section_work = self.SUPERVISORS
        data.data_form = self.CHECK_ALl_SUP
        data.table_rows_selector = self.TABLE_ROWS_SUP
        data.file_selector = self.FILE_SELECTOR_SUP
        data.col_selector = self.COL_SELECTOR_SUP
        found = data.find_employee_records(supervisor)
        return found

    def confirm_added_collaborator_data(self, collaborator):

        collaborator = collaborator[0:11]
        data = ConfirmRegisters(self.driver)
        data.section_work = self.COLLABORATORS
        data.data_form = self.CHECK_ALl_COLLAB
        data.table_rows_selector = self.TABLE_ROWS_COLLAB
        data.file_selector = self.FILE_SELECTOR_COLLAB
        data.col_selector = self.COL_SELECTOR_COLLAB
        found = data.find_employee_records(collaborator)
        return found




