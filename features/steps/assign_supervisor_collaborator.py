from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_personal_data import EditDataEmployees
from lib.pages.add_supervisor_collaborator import ReportTo
import os

use_step_matcher("re")


@given("Usuario con permisos asignados")
def user_assigned_permissions(context):
    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia sesion en la aplicación")
def login_application(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Va al módulo de información personal\.")
def access_information_module(context):

    context.add = EditDataEmployees(context.driver)
    context.add.select_menu()



@given('Buscar empleado por "(?P<id_employee>.+)"')
def search_employee(context, id_employee):

    context.id_employee = id_employee
    context.add.search_data_employee(id_employee)

@step("Acceder a los detalles del empleado\.")
def access_employee_details(context):

    context.data = ReportTo(context.driver)
    context.data.report_to(context.id_employee)


@when('Añade Reporta a Supervisor y Colaborador “(?P<supervisor>.+)”, "(?P<colaborador>.+)"\.')
def add_report_to(context, supervisor, colaborador):
    context.report = {"supervisor": supervisor, "collaborator": colaborador}
    context.data.add_supervisor(context.report)
    context.data.add_collaborator(context.report)


@then("Confirmar los datos del supervisor añadido\.")
def confirm_data_supervisor_collaborator_added(context):

    found = context.data.confirm_added_supervisor_data(context.report["supervisor"])
    assert found


@then("Confirmar datos del colaborador añadido\.")
def step_impl(context):

    found = context.data.confirm_added_collaborator_data(context.report["collaborator"])
    assert found


