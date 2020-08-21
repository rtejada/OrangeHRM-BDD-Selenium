from behave import *

use_step_matcher("re")


@given("Usuario con permisos de adminitración esta registrado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("Buscar empleados")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Editar su Datos Personales")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("Añadir archivos adjuntos")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("Confirmar que los datos se han registrado")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass