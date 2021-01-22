from behave import *
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from lib.pages.user_login import UserLogin
from selenium import webdriver
import os

use_step_matcher("re")


@given("Usuario no registrado accede a la web\.")
def step_load_page(context):

    load_dotenv(os.getcwd() + "/BDD-Blinklearning/features/lib/data/.env.blinklearning")

    arguments = os.getenv('CHROME_ARGS')
    args = arguments.split(";")
    options = Options()
    for i in args:
        options.add_argument(i)

    context.driver = webdriver.Chrome(options=options)

    context.loadPage = UserLogin(context.driver)
    context.loadPage.load_url()


@when("Inserta credenciales no autorizadas(?P<email>.+), (?P<password>.+)\.")
def step_load_login(context, email, password):

    context.loadPage.load_login_page(email, password)


@then("Muestra aviso acceso incorrecto\.")
def step_incorrect_access(context):

    sample_note ='No se ha podido conectar con tu email/contraseña. Por favor, compruébalos e inténtalo de nuevo o pincha en "¿Olvidaste contraseña?". Recuerda que el registro es sensible a las mayúsculas. '
    notice = context.loadPage.register()

    assert notice == sample_note


