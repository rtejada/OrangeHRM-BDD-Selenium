Feature: Asignar Supervisor y Colaborador

  Background:
    Given Usuario con permisos asignados
    And Inicia sesion en la aplicación
    And Va al módulo de información personal.


  Scenario Outline: En los Detalles de Reporta a: Añadir Supervisor
    Given Buscar empleado por "<id_employee>"
    And Acceder a los detalles internos del empleado.
    When Añade Reporta a Supervisor “<supervisor>”.
    Then Confirmar los datos del supervisor añadido.
    And Eliminar datos del supervisor añadido.


    Examples:
    |id_employee|supervisor|
    |ID2420339|Pedro-18201 BGAOFYJIP CSLDRJueF|


  Scenario Outline: En los Detalles de Reporta a: Añadir Colaborador
    Given Buscar empleado por su "<id_employee>"
    And Acceder a sus datos internos
    When Añadir Reporta a Colaborador"<colaborador>"
    Then Confirmar datos del colaborador añadido.
    And Elimnar datos del colaborador añadido.

     Examples:
    |id_employee|colaborador|
    |ID2420339|Maria-4256 BGHQjSlmn CR7EDU2Q4|
