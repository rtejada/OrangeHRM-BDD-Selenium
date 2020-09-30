# Created by roxana at 29/09/20
Feature: Asignar Inmigraciones del Empleado

  Background:
    Given Usuario con permisos asignados
    And Inicia sesion en la aplicación
    And Va al módulo de información personal.

  Scenario Outline: Agregar Inmigración
    Given Buscar empleado por "<id_employee>".
    And Acceder a detalles del empleado.
    When Añadir inmigración.
    Then confirmar datos de inmigración añadido.

    Examples:
    |id_employee|
    |ID17323630|
    |ID10693967|
    |ID10593465|
    |ID19337062|