from behave import *
from lib.pages.init_session import StartSessionPage
from lib.pages.edit_personal_data import EditDataEmployees
from lib.pages.add_resume_data import AddingCurriculumData
from lib.data.orangeHRM_open_chrome_driver import *
use_step_matcher("re")


@given("Usuario con permisos de administración registrado\.")
def authorized_user(context):

    context.driver = get_driver()


@step("Inicia sesion y accede al Modulo de Información Personal\.")
def access_personal_information(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()

    edit = EditDataEmployees(context.driver)
    edit.select_menu()


@when('Busca el empleado por su "(?P<identificacion>.+)"')
def search_employee(context, identificacion):

    context.identification = identificacion

    data = AddingCurriculumData(context.driver)
    data.access_data_employee(context.identification)
    context.data = data


@step('Accede a su datos personales y añade su "(?P<fotografia>.+)"')
def access_personal_data(context, fotografia):

    context.photo = fotografia
    context.data.add_photo(context.photo)


@step("Añade su experiencia laboral, su formacion y sus habiliadades “(?P<puesto>.+)”, “(?P<empresa>.+)”")
def add_experience_training(context, puesto, empresa):
    context.work_experience = {"post": puesto, "company": empresa}
    context.data.add_curriculum(context.work_experience)


@then("Confirma los datos registrados “(?P<empresa>.+)”\.")
def confirm_recorded_data(context, empresa):

    context.empresa = empresa
    found = context.data.confirm_added_data(context.empresa)
    assert found
