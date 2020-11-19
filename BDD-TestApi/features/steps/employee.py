from behave import *
from lib.pages.api_connection import ApiConnection
from lib.pages.employee_data import EmployeeData
from lib.pages.query_employee import DataBase
import requests
import json
from random import randint
use_step_matcher("re")


@given("Se establece URL base con sus parametros de autentificación\.")
def authentication_parameters(context):

    token = ApiConnection()
    context.access_token = token.get_token()
    context.url_base = token.get_url_base()
    context.api_call_headers = {'Authorization': 'Bearer ' + context.access_token,
                                'Content-Type': 'application/json'
                                }


@step("Se establece el parametro necesario para crear nuevo empleado\.")
def necessary_parameter(context):

    params = EmployeeData()
    payload = {"firstName": params.first_name(), "middleName": params.middle_name(), "lastName": params.last_name(),
               "code": params.code()}

    context.employee_data = payload
    context.payload = json.dumps(payload)

    context.url_base = context.url_base + 'employee/'


@when("Realizar una petición POST\.")
def make_request(context):

    id = randint(1, 50)
    api_call_response = requests.post(context.url_base + str(id), headers=context.api_call_headers,
                                      data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code
    context.id_employee = context.body_call_response["id"]


@then("Confirmar Estado 200 \(empleado creado con exito\)\.")
def confirm_status(context):

    assert context.response_code == 200
    assert context.body_call_response["success"] == "Successfully Saved"
    assert context.body_call_response["id"] == context.id_employee


@given("Establecer parametros para recuperar el usuario\.")
def recover_user(context):
    context.payload = {}
    context.url_base = context.url_base + str(context.id_employee)


@when("Se recupera los Datos del Empleado con una petición GET\.")
def recovering_employee_data(context):

    api_call_response = requests.get(context.url_base, headers=context.api_call_headers,
                                     data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@then("Se confirman datos del empleado\.")
def confirm_employee_data(context):

    full_name = context.employee_data["firstName"]+' '+context.employee_data["middleName"]+' '+context.employee_data["lastName"]

    assert context.response_code == 200
    assert context.body_call_response["data"]["firstName"] == context.employee_data["firstName"]
    assert context.body_call_response["data"]["middleName"] == context.employee_data["middleName"]
    assert context.body_call_response["data"]["lastName"] == context.employee_data["lastName"]
    assert context.body_call_response["data"]["code"] == context.employee_data["code"]
    assert context.body_call_response["data"]["employeeId"] == context.id_employee
    assert context.body_call_response["data"]["fullName"] == full_name


@given("Se establece el parametro requerido para actualizar los datos\.")
def set_parameters_update_data(context):

    params = EmployeeData()
    payload = {"firstName": params.first_name(), "lastName": params.last_name(), "status": params.status(),
               "dob": params.dob(), "jobTitle": params.job_title(0), "maritalStatus": params.marital_status(0),
               "licenseNumber": params.drivers_license(), "licenseExpiryDate": params.license_expire(),
               "gender": params.gender(1), "nationality": params.nationality(), "sinNumber": params.sin_number()}

    context.payload = json.dumps(payload)
    context.url_base = context.url_base + str(context.id_employee)


@when("Los datos del empleado se actualizan con una petición PUT\.")
def update_employee_data(context):

    api_call_response = requests.put(context.url_base, headers=context.api_call_headers,
                                     data=context.payload)

    context.body_call_response = api_call_response.json()
    context.response_code = api_call_response.status_code


@then("Se Confirma estado 200 \(datos del empleado actualizado con exito\)\.")
def confirm_status(context):

    assert context.response_code == 200
    assert context.body_call_response["success"] == "Successfully Updated"


@step("Establecer parametros para recuperar los datos del usuario\.")
def set_parameters_retrieve_data(context):

    context.payload = {}
    #context.url_base = context.url_base + str(context.id_employee)


@step("Recuperar Datos actualizados con una petición GET")
def updated_data_recovery(context):

    api_call_response = requests.get(context.url_base, headers=context.api_call_headers,
                                     data=context.payload)

    context.body_call_update = api_call_response.json()
    context.response_code = api_call_response.status_code


@step("Se confirman datos actualizados del empleado\.")
def confirm_updated_data(context):

    query = DataBase()
    query_result = query.get_employee_number(context.id_employee)

    assert context.response_code == 200
    assert context.body_call_update["data"]["firstName"] == query_result["emp_firstname"]
    assert context.body_call_update["data"]["middleName"] == query_result["emp_middle_name"]
    assert context.body_call_update["data"]["lastName"] == query_result["emp_lastname"]
    assert query_result["emp_firstname"] in context.body_call_update["data"]["fullName"]
    assert context.body_call_update["data"]["code"] == query_result["employee_id"]
    assert context.body_call_update["data"]["employeeId"] == str(query_result["emp_number"])
    assert context.body_call_update["data"]["dob"] == str(query_result["emp_birthday"])
    assert context.body_call_update["data"]["driversLicenseNumber"] == query_result["emp_dri_lice_num"]
    assert context.body_call_update["data"]["maritalStatus"] == query_result["emp_marital_status"]


