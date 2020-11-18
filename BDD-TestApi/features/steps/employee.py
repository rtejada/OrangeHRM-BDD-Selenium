from behave import *
from lib.pages.api_connection import ApiConnection
from lib.pages.params import GeneratorDataParameters
import requests
import json
from random import randint
use_step_matcher("re")


@given("Se establece URL base con sus parametros de autentificación\.")
def step_impl(context):

    token = ApiConnection()
    context.access_token = token.get_token()
    context.url_base = token.get_url_base()
    context.api_call_headers = {'Authorization': 'Bearer ' + context.access_token,
                                'Content-Type': 'application/json'
                                }


@step("Se establece el parametro necesario para crear nuevo empleado\.")
def step_impl(context):

    params = GeneratorDataParameters()
    payload = {"firstName": params.first_name(), "middleName": params.middle_name(), "lastName": params.last_name(),
               "code": params.code()}
    context.employee_data = payload
    context.payload = json.dumps(payload)

    context.url_base = context.url_base + 'employee/'


@when("Realizar una petición POST\.")
def step_impl(context):

    id = randint(1, 50)
    api_call_response = requests.post(context.url_base + str(id), headers=context.api_call_headers,
                                      data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code
    context.id_employee = context.body_call_response["id"]


@then("Confirmar Estado 200 \(empleado creado con exito\)\.")
def step_impl(context):

    confirm_success = context.body_call_response["success"]

    assert context.response_code == 200
    assert confirm_success == "Successfully Saved"


@given("Establecer parametros para recuperar el usuario\.")
def step_impl(context):
    context.payload = {}
    context.url_base = context.url_base + str(context.id_employee)


@when("Se recupera los Datos del Empleado con una petición GET\.")
def step_impl(context):

    api_call_response = requests.get(context.url_base, headers=context.api_call_headers,
                                     data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@then("Se confirman datos del empleado\.")
def step_impl(context):

    full_name = context.employee_data["firstName"]+' '+context.employee_data["middleName"]+' '+context.employee_data["lastName"]

    assert context.response_code == 200
    assert context.body_call_response["data"]["firstName"] == context.employee_data["firstName"]
    assert context.body_call_response["data"]["middleName"] == context.employee_data["middleName"]
    assert context.body_call_response["data"]["lastName"] == context.employee_data["lastName"]
    assert context.body_call_response["data"]["code"] == context.employee_data["code"]
    assert context.body_call_response["data"]["employeeId"] == context.id_employee
    assert context.body_call_response["data"]["fullName"] == full_name


@given("Se establece el parametro requerido para actualizar los datos\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Los datos del empleado se actualizan con una petición PUT\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Se Confirma estado 200 \(datos del empleado actualizado con exito\)\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


