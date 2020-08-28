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
def Registered_user(context):
    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()


@step("Accede a la opcion Puestos de Trabajo\.")
def access_jobs_option(context):

    new_job = AddNewJobs(context.driver)
    new_job.select_menu()
    context.new_job = new_job


@when('Añade varios puestos de Trabajo “(?P<title>.+)”, "(?P<job_description>.+)", "(?P<note>.+)" , "(?P<img>.+)"')
def add_several_jobs(context, title, job_description, note, img):

    context.dict_jobs = {'title': title, 'job_description': job_description, 'note': note, 'img': img}
    context.new_job.add_jobs(context.dict_jobs)


@then("Confirma titulos de los puestos añadidos “(?P<title>.+)”")
def confirm_titles_added_posts(context, title):
    context.title = title
    found = context.new_job.search_jobs(context.title)
    assert found
