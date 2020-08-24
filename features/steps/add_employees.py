
from behave import *
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.add_employees import AdminEmployees

use_step_matcher("re")

@given("un usuario registrado")
def step_impl(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(",")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@given("El usuario tiene permisos de administración\.")
def step_impl(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@when('Añade nuevo empleados “(?P<cod>.+)”, "(?P<p_nombre>.+)", "(?P<s_nombre>.+)", "(?P<apellidos>.+)", "(?P<usu>.+)", "(?P<pwd>.+)"')
def step_impl(context, cod, p_nombre, s_nombre, apellidos, usu, pwd):
    context.request_cod = cod
    context.request_p_nombre = p_nombre
    context.request_s_nombre = s_nombre
    context.request_apellidos = apellidos
    context.request_usu = usu
    context.request_pwd = pwd

    employee = AdminEmployees(context.driver)
    employee.select_menu()
    employee.add_data(context.request_cod, context.request_p_nombre, context.request_s_nombre, context.request_apellidos,
                      context.request_usu, context.request_pwd)
    name = employee.get_employee()
    context.employee = employee
    context.name = name

@then("confirma datos del nuevo empleado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Busca el nuevo empleado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Edita los datos personales")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Añade archivos adjuntos")
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