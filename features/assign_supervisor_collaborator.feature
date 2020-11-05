Feature: Asignar Supervisor y Colaborador

  Background:
    Given Usuario con permisos asignados
    And Inicia sesion en la aplicación
    And Va al módulo de información personal.


  Scenario Outline: En los Detalles de Reporta a: Añadir Supervisor
    Given Buscar empleado por "<id_employee>"
    And Acceder a los detalles internos del empleado.
    When Añade Reporta a Supervisor “<supervisor_number>”.
    Then Confirmar los datos del supervisor añadido.
    And Eliminar datos del supervisor añadido.


    Examples:
    |id_employee|supervisor_number|
    |ID2420339|153|


  Scenario Outline: En los Detalles de Reporta a: Añadir Colaborador
    Given Buscar empleado por su "<id_employee>"
    And Acceder a sus datos internos
    When Añadir Reporta a Colaborador"<collaborator_number>"
    Then Confirmar datos del colaborador añadido.
    And Eliminar datos del colaborador añadido.

     Examples:
    |id_employee|collaborator_number|
    |ID2420339|156|
