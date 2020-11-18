# Created by roxana at 29/09/20
Feature: Asignar Inmigraciones del Empleado

  Background:
    Given Usuario con permisos se registra.
    And Inicia una sesion.
    And Accede al módulo Información Personal.

  Scenario Outline: Agregar Inmigración
    Given Buscar empleado por "<id_employee>".
    And Acceder a detalles del empleado.
    When Añadir inmigración.
    Then confirmar datos de inmigración añadido.

    Examples:
    |id_employee|
    |ID19337062|
    |ID10593465|
