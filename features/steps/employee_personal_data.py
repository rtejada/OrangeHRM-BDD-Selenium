from behave import *
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_personal_data import EditDataEmployees
from lib.pages.add_personal_data import DataPersonalEmployee
from lib.data.orangeHRM_open_chrome_driver import *
use_step_matcher("re")


@given("Usuario con permisos registrado")
def registered_user(context):

    context.driver = get_driver()


@step("Inicia sesion en la plataforma")
def login_platform(context):
    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede al módulo de información personal\.")
def access_information_module(context):

    context.add = EditDataEmployees(context.driver)
    context.add.select_menu()


@given('Busca al empleado por "(?P<id_employee>.+)"')
def search_employee(context, id_employee):

    context.id_employee = id_employee
    context.add.search_data_employee(context.id_employee)


@step('Accede a la opcion de contactos\.')
def access_contacts_option(context):

    context.add_data = DataPersonalEmployee(context.driver)
    context.add_data.access_emergency_contact(context.id_employee)


@when("Añade sus contactos de emergencia\.")
def add_emergency_contacts(context):

    context.contact_name = context.add_data.emergency_contacts()


@then("Confirma los datos de contacto\.")
def confirm_contacts_details(context):

    found = context.add_data.confirm_added_data(context.contact_name)
    assert found


@given('Localiza empleado por "(?P<id_employee>.+)"\.')
def locate_employee(context, id_employee):

    context.id = id_employee
    context.add.search_data_employee(context.id)


@step("Accede a los detalles del empleado\.")
def access_details_employee(context):

    context.add_data = DataPersonalEmployee(context.driver)
    context.add_data.access_family_burdens(context.id)


@when("Añade sus cargas familiares\.")
def add_family_burdens(context):

    context.name = context.add_data.family_burdens()


@then("confirma los datos añadidos\.")
def confirm_data_add(context):

    found = context.add_data.confirm_data_family(context.name)
    assert found
