from behave import *
from lib.pages.init_session import StartSessionPage
from lib.pages.general_information import OrgInformation
from lib.data.orangeHRM_open_chrome_driver import *
use_step_matcher("re")


@given("Usuario administrador conectado\.")
def admin_user_connected(context):

    context.driver = get_driver()

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede a la opcion Información General\.")
def access_general_information(context):

    data = OrgInformation(context.driver)
    data.select_menu()
    context.data = data


@when("Edita y añade la informacion general\.")
def edit_add_general_information(context):

    name_firm = context.data.add_info()

    context.name_firm = name_firm


@then("Confirma información registrada\.")
def confirm_reg_information(context):

    name = context.data.confirm_data()
    assert name == context.name_firm

