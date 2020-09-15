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


 And Añade Datos de Contacto.
   And Añade Datos de Contactos de Emergencia.
   And Añade sus Cargas Familiares.
   And Registra datos de Inmigración.
   

self.wait_selector_visible(self.PROFILE_PIC)
        self.click_button(self.PROFILE_PIC)
        self.wait_selector_visible(self.PHOTO_FILE)
        self.wait_button_clickable(self.PHOTO_FILE)
        self.driver.find_element(*self.PHOTO_FILE).send_keys(self.PATH + work_data["img"])
        self.wait_button_clickable(self.LOAD)
        self.send_enter_key(self.LOAD)
        self.wait_selector_visible(self.LOAD)
        self.wait_button_clickable(self.LOAD)

PROFILE_PIC = (By.ID, 'profile-pic')
PHOTO_FILE = (By.ID, 'photofile')
LOAD = (By.ID, 'btnSave')
PATH = os.getcwd() + "/features/lib/data/images/"
'''
