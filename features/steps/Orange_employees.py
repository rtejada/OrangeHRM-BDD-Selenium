from behave import *
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.orange_start_session import StartSessionPage
from lib.pages.orange_add_emplyees import AdminEmployees

use_step_matcher("re")


@given("Un usuario con permisos esta registrado")
def step_impl(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(",")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@when("Añade empleados")
def step_impl(context):

    employee = AdminEmployees(context.driver)
    employee.select_menu()
    employee.add_data()
    context.name = employee.get_employee()


@then("confirma datos registrados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass