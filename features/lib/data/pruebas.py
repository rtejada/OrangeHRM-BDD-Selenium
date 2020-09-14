import uuid
from string import ascii_uppercase, ascii_letters, digits, ascii_lowercase
from secrets import choice
guid_let = str(uuid.uuid4())
keywords = guid_let.split("-")

print(keywords)



characters = ascii_lowercase + digits
length = 5
chain = ''.join(choice(characters) for char in range(length))

print(chain)
texto = 'Nkwj2KkVcC   '
print(texto)
print(texto.strip(' '))

'''


@when('Busca el nuevo empleado “(?P<nombre>.+)”')
def search_data_registered_employee(context, nombre):
    context.name = nombre
    edit = EditDataEmployees(context.driver)
    edit.select_menu()
    edit.search_data_employee(context.name)

    context.edit = edit


@step("Edita los datos personales")
def edit_personal_data(context):

    new_id = context.edit.item_employee(context.name)
    context.new_id = new_id


@step("Añade archivos adjuntos")
def adding_attachments(context):

    context.edit.add_image()


@then("Confirma que los datos quedaron registrado")
def confirm_data_register(context):

    found = context.edit.search_new_id_employee(context.new_id)

    assert found
 ****   
    
    def search_new_id_employee(self, id_employee):

        search_id = OrangeSiteSearchId(self.driver)
        search_id.personal_detail = self.PERSONAL_DETAILS
        search_id.menu_selector = self.LIST_EMPLOYEES
        search_id.employee = self.IDENTIFICATION
        search_id.identification = id_employee
        search_id.table_row_selector = self.TABLE_ROWS_SELECTOR
        value = search_id.employee_id()
        return value
'''
