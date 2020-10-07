from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_personal_data import EditDataEmployees
from lib.pages.assigned_immigration_registration import AssignedImmigrationRegistration
import os
use_step_matcher("re")



@given("Usuario con permisos se registra\.")
def registerer_user(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia una sesion\.")
def star_session(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede al módulo Información Personal\.")
def step_impl(context):

    context.add = EditDataEmployees(context.driver)
    context.add.select_menu()


@given('Buscar empleado por "(?P<id_employee>.+)"\.')
def step_impl(context, id_employee):

    context.id_employee = id_employee
    context.add.search_data_employee(id_employee)


@step("Acceder a detalles del empleado\.")
def step_impl(context):

    context.data = AssignedImmigrationRegistration(context.driver)
    context.data.immigration(context.id_employee)


@when("Añadir inmigración\.")
def step_impl(context):

    context.passport_number = context.data.add_immigration_registration()


@then("confirmar datos de inmigración añadido\.")
def step_impl(context):

    found = context.data.search_register(context.passport_number)
    assert found
