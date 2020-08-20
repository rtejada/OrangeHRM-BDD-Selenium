from behave import *
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.add_employees import AdminEmployees

use_step_matcher("re")


@given("Un usuario con permisos esta registrado")
def init_session(context):

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
def add_new_employee(context):

    employee = AdminEmployees(context.driver)
    employee.select_menu()
    employee.add_data()
    name = employee.get_employee()
    context.employee = employee
    context.name = name


@then("confirma datos registrados")
def confirm_registration(context):

    found = context.employee.search_name_employee(context.name)

    assert found



