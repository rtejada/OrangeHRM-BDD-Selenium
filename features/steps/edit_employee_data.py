from behave import *
from dotenv import load_dotenv
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_personal_data import EditDataEmployees

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


@step('Edita sus datos personales')
def edit_personal_data(context):

    context.edit.personal_data(context.id)


@step('Añade Datos de Contacto')
def add_contact_details_and_file_attachment(context):

    context.edit.add_contact_details()


@step(
    'Añade Puesto de Trabajo y archivo adjunto "(?P<titulo_puesto>.+)","(?P<categoria>.+)","(?P<ubicacion>.+)","(?P<img>.+)"')
def add_job_and_attachment(context, titulo_puesto, categoria, ubicacion, img):
    context.file = img
    context.work_data = {"title": titulo_puesto, "category": categoria, "location": ubicacion}
    context.edit.add_job(context.work_data)


@then("Confirma que los datos quedaron registrado “(?P<id_employee>.+)”, “(?P<titulo_puesto>.+)”")
def confirm_register_data(context, id_employee, titulo_puesto):

    context.data_search = {"id": id_employee, "title": titulo_puesto}
    found = context.edit.search_register(context.data_search)

    assert found
