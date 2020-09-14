from behave import *
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_data_employee import EditDataEmployees

use_step_matcher("re")


@given("Usuario con permisos registrado\.")
def authorized_user(context):
    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Incia sesion en OrangeHRM\.")
def begin_session(context):
    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@when("Busca empleado “(?P<id_employee>.+)”")
def search_data_registered_employee(context, id_employee):
    context.id = id_employee
    edit = EditDataEmployees(context.driver)
    edit.select_menu()
    edit.search_data_employee(context.id)

    context.edit = edit


@step("Edita sus datos personales")
def edit_personal_data(context):

    context.edit.item_employee(context.id)


@step("Añade archivos adjuntos")
def adding_attachments(context):

    context.edit.add_image()

@step("Añade Datos de Contacto\.")
def step_impl(context):

    context.edit.add_contact_details()

@step("Añade Datos de Contactos de Emergencia\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Añade sus Cargas Familiares\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Registra datos de Inmigración\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Añade Puestos de Trabajo\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Añade el Salario/Sueldo\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Reporta datos a")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Registra Curriculum")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Registra Menbresías")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Confirma que los datos quedaron registrado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

