from behave import *
from dotenv import load_dotenv
import os
from selenium import webdriver
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_personal_data import EditDataEmployees
from selenium.webdriver.chrome.options import Options
from lib.pages.add_resume_data import AddingCurriculumData

use_step_matcher("re")


@given("Usuario con permisos de administración registrado\.")
def authorized_user(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia sesion y accede al Modulo de Información Personal\.")
def step_impl(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()

    edit = EditDataEmployees(context.driver)
    edit.select_menu()


@when('Busca el empleado por su "(?P<identificacion>.+)"')
def step_impl(context, identificacion):

    context.identification = identificacion

    data = AddingCurriculumData(context.driver)
    data.access_data_employee(context.identification)
    context.data = data


@step('Accede a su datos personales y añade su "(?P<fotografia>.+)"')
def step_impl(context, fotografia):

    context.photo = fotografia
    context.data.add_photo(context.photo)


@step("Añade su experiencia laboral, su formacion y sus habiliadades “(?P<puesto>.+)”, “(?P<empresa>.+)”")
def step_impl(context, puesto, empresa):
    context.work_experience = {"post": puesto, "company": empresa}
    context.data.add_curriculum(context.work_experience)


@then("Confirma los datos registrados “(?P<empresa>.+)”\.")
def step_impl(context, empresa):

    context.empresa = empresa
    found = context.data.confirm_added_data(context.empresa)
    assert found
