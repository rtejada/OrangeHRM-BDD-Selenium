from behave import *
from lib.pages.api_connection import ApiConnection
from lib.pages.contact_details import ContactDetails
from lib.pages.query_employee import DataBase
import json
import requests

use_step_matcher("re")


@given("Se establece URL base con parametros de autentificación\.")
def authentication_parameters(context):

    token = ApiConnection()
    context.access_token = token.get_token()
    context.url_base = token.get_url_base()
    context.api_call_headers = {'Authorization': 'Bearer ' + context.access_token,
                                'Content-Type': 'application/json'
                                }


@given("Establecer parametros para para añadir los datos de contacto del empleado (?P<id_emp>.+)\.")
def step_impl(context, id_emp):

    id_emp = str(id_emp)
    params = ContactDetails()
    payload = {"addressStreet1": params.address_street1(), "addressStreet2": params.address_street2(),
               "city": params.city(),
               "state": params.state(), "zip": params.zip(), "county": params.country(),
               "homeTelephone": params.home_telephone(),
               "workTelephone": params.work_telephone(), "mobile": params.mobile(), "workEmail": params.work_email(),
               "otherEmail": params.other_email()}

    context.employee_data = payload
    context.payload = json.dumps(payload)

    query = DataBase()
    results = query.get_employee_number(id_emp)
    if results is not None:
        try:
            if results["emp_number"] == id_emp:
                context.url_base = context.url_base + "employee /" + id_emp + "/contact-detail"

        except Exception as e:
            print("Ocurrió un error con exception", e)


@when("Realizar nueva petición POST\.")
def step_impl(context):

    api_call_response = requests.post(context.url_base + str(id), headers=context.api_call_headers,
                                      data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@then("Confirmar Estado 200 \(Datos de contacto actualizados\)\.")
def step_impl(context):

    assert context.response_code == 200
    assert context.body_call_response["success"] == "Successfully Saved"


@step("Establecer parametros para recuperar los datos de contacto del usuario\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Recuperar datos de contactos actualizados con una petición GET")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Confirmar datos actualizados del empleado\.")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass