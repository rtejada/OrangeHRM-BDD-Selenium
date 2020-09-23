from behave import *
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_personal_data import EditDataEmployees
from lib.pages.add_personal_data import DataPersonalEmployee
import os
use_step_matcher("re")


@given("Usuario con permisos registrado")
def step_impl(context):
    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia sesion en la plataforma")
def step_impl(context):
    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede al módulo de información personal\.")
def step_impl(context):

    context.add = EditDataEmployees(context.driver)
    context.add.select_menu()


@given('Busca al empleado por "(?P<id_employee>.+)"')
def step_impl(context, id_employee):

    context.id_employee = id_employee
    context.add.search_data_employee(context.id_employee)


@step('Accede a la opcion de contactos\.')
def step_impl(context):

    context.add_data = DataPersonalEmployee(context.driver)
    context.add_data.personal_data(context.id_employee)


@when("Añade sus contacto de emergencia\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("confirma datos del contacto\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given('Localiza empleado por "(?P<id_employee>.+)"\.')
def step_impl(context, id_employee):
    """
    :type context: behave.runner.Context
    :type id_employee: str
    """
    pass


@step("Accede a los detalles del empleado\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Añade sus cargas familiares\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("confirma los datos añadidos\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass

