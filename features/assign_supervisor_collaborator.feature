Feature: Asignar Supervisor y Colaborador

  Background:
    Given Usuario con permisos asignados
    And Inicia sesion en la aplicación
    And Va al módulo de información personal.


  Scenario Outline: En los Detalles Añadir Reporta a
    Given Buscar empleado por "<id_employee>"
    And Acceder a los detalles del empleado.
    When Añade Reporta a Supervisor y Colaborador “<supervisor>”, "<colaborador>".
    Then Confirmar los datos del supervisor añadido.
    Then Confirmar datos del colaborador añadido.

    Examples:
    |id_employee|supervisor|colaborador|
    |ID19260914|Pedro-18201 BGAOFYJIP CSLDRJueF|Diego-18348 BlQZW6Xc0 CCLiZIQVW|
    |ID10390140|Pedro-18201 BGAOFYJIP CSLDRJueF|Diego-18348 BlQZW6Xc0 CCLiZIQVW|
    |ID1974421|Pedro-18201 BGAOFYJIP CSLDRJueF|Diego-18348 BlQZW6Xc0 CCLiZIQVW|
    |ID2420339|Pedro-18201 BGAOFYJIP CSLDRJueF|Diego-18348 BlQZW6Xc0 CCLiZIQVW|
