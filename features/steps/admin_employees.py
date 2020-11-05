from behave import *
from lib.data.orangeHRM_open_chrome_driver import *
from lib.pages.init_session import StartSessionPage
from lib.pages.add_employees import AdminEmployees
use_step_matcher("re")


@given("Un usuario registrado")
def authorized_user(context):

    context.driver = get_driver()


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
    context.code = code


@then("confirma datos del nuevo empleado")
def search_and_confirm_employee_data(context):

    found = context.employee.search_name_employee(context.name)

    assert found
