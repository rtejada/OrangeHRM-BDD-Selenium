from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.salary_concept import SalaryConcept
import os

use_step_matcher("re")


@given("Usuario administrador registrado\.")
def step_impl(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@step("Inicia sesion y accede a la opcion correspondiente\.")
def step_impl(context):

    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()

    add = SalaryConcept(context.driver)
    add.select_menu()
    context.add = add

@when("Busca y selecciona empleado por “(?P<id_employee>.+)”")
def step_impl(context, id_employee):

    context.id_employee = id_employee
    context.add.search_employee(context.id_employee)


@step("Accede a la opcion Salarios")
def step_impl(context):

    context.add.open_salary_option()

@step('Añade salario segun escala salarial "(?P<escala>.+)", "(?P<monto>.+)"')
def step_impl(context, escala, monto):

    context.salary_scale = {"escala_salarial": escala, "monto": monto}
    context.salary_component = context.add.amount(context.salary_scale)


@then("Confirma componente salarial registrado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass