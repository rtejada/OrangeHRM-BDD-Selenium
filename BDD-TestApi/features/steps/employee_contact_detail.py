from behave import *
from lib.pages.api_connection import ApiConnection
from lib.pages.contact_details import ContactDetails
from lib.pages.query_employee import DataBase
import json
import requests
use_step_matcher("re")


@given("URL Base con parametros de Autentificación\.")
def authentication_parameters(context):

    token = ApiConnection()
    context.access_token = token.get_token()
    context.url_base = token.get_url_base()
    context.api_call_headers = {'Authorization': 'Bearer ' + context.access_token,
                                'Content-Type': 'application/json'
                                }


@given("Establecer parametros para para añadir los datos de contacto del empleado (?P<id_emp>.+)\.")
def necessary_parameter(context, id_emp):
    context.employee_id = id_emp
    params = ContactDetails()
    payload = {"addressStreet1": params.address_street1(), "addressStreet2": params.address_street2(),
               "city": params.city(), "state": params.state(), "zip": params.zip(),
               "homeTelephone": params.home_telephone(), "workTelephone": params.work_telephone(),
               "mobile": params.mobile(), "workEmail": params.work_email(), "otherEmail": params.other_email()
               }

    context.employee_data = payload
    context.payload = json.dumps(payload)

    query = DataBase()
    context.results = query.get_employee_number(context.employee_id)
    if context.results is not None:
        try:
            if context.results["emp_number"] == int(context.employee_id):
                context.url_base = context.url_base + "employee/" + context.employee_id + "/contact-detail"

        except Exception as e:
            print("Ocurrió un error con exception", e)
    else:
        print("El empleado con ID:", context.employee_id, " No existe")


@when("Realizar nueva petición POST\.")
def make_request(context):

    api_call_response = requests.post(context.url_base, headers=context.api_call_headers,
                                      data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@then("Confirmar Estado 200 \(Datos de contacto añadidos\)\.")
def confirm_status(context):

    assert context.response_code == 200
    assert context.body_call_response["success"] == "Successfully Saved"


@step("Recuperar datos de contactos añadidos con una petición GET")
def recovering_employee_data(context):

    payload = {}
    api_call_response = requests.get(context.url_base, headers=context.api_call_headers,
                                     data=payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@step("Confirmar datos añadidos del empleado\.")
def confirm_employee_added_data(context):

    assert context.response_code == 200
    assert context.body_call_response["data"]["id"] == str(context.results["emp_number"])
    assert context.body_call_response["data"]["code"] == context.results["employee_id"]
    assert context.body_call_response["data"]["addressStreet1"] == context.employee_data["addressStreet1"]
    assert context.body_call_response["data"]["addressStreet2"] == context.employee_data["addressStreet2"]
    assert context.body_call_response["data"]["city"] == context.employee_data["city"]
    assert context.body_call_response["data"]["state"] == context.employee_data["state"]
    assert context.body_call_response["data"]["zip"] == context.employee_data["zip"]
    assert context.body_call_response["data"]["homeTelephone"] == context.employee_data["homeTelephone"]
    assert context.body_call_response["data"]["workTelephone"] == context.employee_data["workTelephone"]
    assert context.body_call_response["data"]["mobile"] == context.employee_data["mobile"]
    assert context.body_call_response["data"]["workEmail"] == context.employee_data["workEmail"]
    assert context.body_call_response["data"]["otherEmail"] == context.employee_data["otherEmail"]


@given("Establecer parametros para para actualizar los datos de contacto del empleado (?P<id_emp>.+)\.")
def set_parameters_update_data(context, id_emp):

    context.employee_id = id_emp
    params = ContactDetails()
    payload = {"addressStreet1": params.address_street1(), "addressStreet2": params.address_street2(),
               "city": params.city(), "state": params.state(), "zip": params.zip(), "country": params.country(),
               "homeTelephone": params.home_telephone(), "workTelephone": params.work_telephone(),
               "mobile": params.mobile(), "workEmail": params.work_email(), "otherEmail": params.other_email()
               }

    context.employee_data_updated = payload
    context.payload = json.dumps(payload)

    query = DataBase()
    context.results = query.get_employee_number(context.employee_id)
    if context.results is not None:
        try:
            if context.results["emp_number"] == int(context.employee_id):
                context.url_base = context.url_base + "employee/" + context.employee_id + "/contact-detail"

        except Exception as e:
            print("Ocurrió un error con exception", e)
    else:
        print("El empleado con ID:", context.employee_id, " No existe")


@when("Realizar nueva petición PUT\.")
def update_employee_data(context):

    api_call_response = requests.put(context.url_base, headers=context.api_call_headers,
                                     data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@then("Confirmar Estado 200 \(Datos de contacto actualizados\)\.")
def confirm_status(context):

    assert context.response_code == 200
    assert context.body_call_response["success"] == "Successfully Updated"


@step("Recuperar los datos de contactos actualizados con una petición GET")
def set_parameters_retrieve_data(context):

    payload = {}
    api_call_response = requests.get(context.url_base, headers=context.api_call_headers,
                                     data=payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@step("Confirmar datos actualizados del empleado\.")
def confirm_updated_data_recovery(context):

    assert context.response_code == 200
    assert context.body_call_response["data"]["id"] == str(context.results["emp_number"])
    assert context.body_call_response["data"]["code"] == context.results["employee_id"]
    assert context.body_call_response["data"]["addressStreet1"] == context.employee_data_updated["addressStreet1"]
    assert context.body_call_response["data"]["addressStreet2"] == context.employee_data_updated["addressStreet2"]
    assert context.body_call_response["data"]["city"] == context.employee_data_updated["city"]
    assert context.body_call_response["data"]["state"] == context.employee_data_updated["state"]
    assert context.body_call_response["data"]["zip"] == context.employee_data_updated["zip"]
    assert context.body_call_response["data"]["county"] == context.employee_data_updated["country"]
    assert context.body_call_response["data"]["homeTelephone"] == context.employee_data_updated["homeTelephone"]
    assert context.body_call_response["data"]["workTelephone"] == context.employee_data_updated["workTelephone"]
    assert context.body_call_response["data"]["mobile"] == context.employee_data_updated["mobile"]
    assert context.body_call_response["data"]["workEmail"] == context.employee_data_updated["workEmail"]
    assert context.body_call_response["data"]["otherEmail"] == context.employee_data_updated["otherEmail"]

