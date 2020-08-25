from behave import *
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.add_employees import AdminEmployees
from lib.pages.edit_data_employee import EditDataEmployees

use_step_matcher("re")


@given("Un usuario registrado")
def authorized_user(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(",")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@given("El usuario tiene permisos de administración\.")
def user_with_admin_permissions(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@when('Añade nuevo empleados “(?P<cod>.+)”, "(?P<p_nombre>.+)", "(?P<s_nombre>.+)", "(?P<apellidos>.+)", "(?P<usu>.+)", "(?P<pwd>.+)"')
def add_new_employee(context, cod, p_nombre, s_nombre, apellidos, usu, pwd):

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

    name, code = employee.get_employee()
    context.employee = employee
    context.name = name


@then("confirma datos del nuevo empleado")
def search_and_confirm_employee_data(context):

    found = context.employee.search_name_employee(context.name)

    assert found


@when("Busca el nuevo empleado")
def search_data_registered_employee(context):

    edit = EditDataEmployees(context.driver)
    edit.select_menu()
    edit.search_data_employee()
    context.edit = edit


@step("Edita los datos personales")
def step_impl(context):

    new_id = context.edit.data_employee()
    context.new_id = new_id


@step("Añade archivos adjuntos")
def adding_attachments(context):

    context.edit.add_image()


@then("Confirma que los datos quedaron registrado")
def confirm_data_register(context):

    pass