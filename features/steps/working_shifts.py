from behave import *
from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lib.pages.init_session import StartSessionPage
from lib.pages.add_working_shifts import AddWorkingShift

use_step_matcher("re")


@given("Usuario admin registrado")
def authorized_user(context):
    load_dotenv(os.getcwd() + "/features/lib/data/.env.orangeHRM")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)
    context.driver = webdriver.Chrome(options=options)

@given("El Usuario tiene permisos para agregar los turnos de trabajo\.")
def user_with_admin_permissions(context):
    start_session = StartSessionPage(context.driver)
    start_session.load()
    start_session.login_user()

@step("Accede a la opcion Turnos de Trabajo")
def access_work_shift_option(context):

    work = AddWorkingShift(context.driver)
    work.select_menu()
    context.work = work


@when('Agrega Turnos de Trabajo “(?P<nom_turno>.+)”, "(?P<desde>.+)", "(?P<hasta>.+)", "(?P<empleado>.+)"')
def add_shift(context, nom_turno, desde, hasta, empleado):
    context.workings_hours = {'nom_turno': nom_turno, 'desde': desde, 'hasta': hasta}
    context.employee = empleado

    context.work.add_shift(context.workings_hours, context.employee)

@step("Agrega mas empleado “(?P<nom_turno>.+)”, “(?P<empleados>.+)”")
def add_more_employee(context, nom_turno, empleados):
    context.nom_turno = nom_turno
    context.empleado = empleados
    context.work.more_employees(context.nom_turno, context.empleado)


@then("Confirma los turnos de trabajo Añadidos “(?P<nom_turno>.+)”")
def confirm_registered_data(context, nom_turno):
    context.nom_turno = nom_turno
    fount = context.work.confirm_data(context.nom_turno)

    assert fount


@step("Eliminar Turno de Trabajo “(?P<nom_turno>.+)”")
def step_impl(context, nom_turno):

    context.nom_turno = nom_turno
    not_found = context.work.del_work_shift(context.nom_turno)

    assert not_found
