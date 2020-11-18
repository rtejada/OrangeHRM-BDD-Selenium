from lib.pages.pages_search.base_page import OrangeBasePage


class AddingMonitoryData(OrangeBasePage):

    container_report_to = ''
    add_report_to = ''
    add_name = ''
    first_letter = ''
    container_ac_results = ''
    list_rows = ''
    report_method = ''
    value_method = ''
    save = ''

    def adding_supervision_collaborator(self, supervisor):

        self.wait_selector_visible(self.container_report_to)
        self.click_button(self.add_report_to)

        element = self.driver.find_element(*self.add_name)
        element.click()
        element.send_keys(self.first_letter)
        self.wait_selector_visible(self.container_ac_results)
        rows = self.driver.find_elements(*self.list_rows)

        count = 0
        selected = -1

        for row in rows:
            if row.text == supervisor:
                selected = count
                break

            count += 1

        if selected >= 0:
            try:
                rows[selected].click()
            except Exception as e:
                return f'ERROR NO SE ENCONTRO EL ELEMENTO DE LA LISTA: {e}'

        self.fill_select_by_text(self.report_method, self.value_method)
        self.send_enter_key(self.save)
