from behave import *
from lib.data.orangeHRM_open_chrome_driver import *
from lib.pages.init_session import StartSessionPage
from lib.pages.add_salary_scales import AddSalaryScales

use_step_matcher("re")


@given("Usuario abre la aplicación OrangeHRM")
def authorized_user(context):

    context.driver = get_driver()


@given("Usuario con permismos registrado\.")
def user_with_admin_permissions(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede a la opcion Escalas Salariales\.")
def access_salary_scale_option(context):

    new_scale = AddSalaryScales(context.driver)
    new_scale.select_menu()
    context.new_scale = new_scale

@when(
    'Añade escalas salarias a los puestos de Trabajo “(?P<title_scale>.+)”, "(?P<currency>.+)", "(?P<minimum_salary>.+)" , "(?P<maximum_salary>.+)"')
def step_impl(context, title_scale, currency, minimum_salary, maximum_salary):

    context.dict = {"title_scale": title_scale, "currency": currency, "minimum_salary": minimum_salary, "maximum_salary": maximum_salary}
    max_salary = context.new_scale.add_salary_sacale(context.dict)
    context.max_salary = max_salary


@then("confirma datos añadidos")
def step_impl(context):

    found = context.new_scale.search_max_salary(context.max_salary)
    assert found


@step('Elimina registro “(?P<title_scale>.+)”')
def step_impl(context, title_scale):

    context.title = title_scale
    not_found = context.new_scale.del_title_salary_scale(context.title)
    assert not_found
