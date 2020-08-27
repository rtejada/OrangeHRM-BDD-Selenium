from behave import *
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.add_jobs import AddNewJobs
import os

use_step_matcher("re")


@given("Un usuario abre la aplicación OrangeHRM")
def step_impl(context):

    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")
    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(",")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)


@given("Usuario registrado\.")
def step_impl(context):
    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede a la opcion Puestos de Trabajo\.")
def step_impl(context):

    new_job = AddNewJobs(context.driver)
    new_job.select_menu()
    context.neew_job = new_job


@when('Añade varios puestos de Trabajo “(?P<title>.+)”, "(?P<job_description>.+)", "(?P<note>.+)"')
def step_impl(context, title, job_description, note):

    context.list_jobs = [title, job_description, note]
    context.new_job.aadd_jobs(context.list_jobs)




@then("Confirma titulos de los puestos añadidos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass