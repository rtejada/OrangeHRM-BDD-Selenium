from behave import *
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.locations_org import CompanyLocations

use_step_matcher("re")


@given("Accede a la aplicación OrangeHRM\.")
def step_impl(context):
    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@given("usuario admin registrado\.")
def step_impl(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede a la opcion Localizaciones\.")
def step_impl(context):

    company = CompanyLocations(context.driver)
    company.select_menu()
    context.company = company


@when('Añade Ubicaciones "(?P<first_name>.+)", "(?P<city>.+)"')
def step_impl(context, first_name, city):

    context.name = first_name
    context.city = city
    name = context.company.add_locations(context.name, context.city)
    context.name = name


@then("confirma Ubicaciones registradas")
def conf_registered_location(context):

    found = context.company.confirm(context.name)

    assert found


@step('Elimina Ubicaciones')
def step_impl(context):

    context.company.del_location()

