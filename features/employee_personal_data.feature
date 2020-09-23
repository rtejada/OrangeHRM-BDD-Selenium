# Created by roxana at 23/09/20
Feature: Información Personal

  Background:
    Given Usuario con permisos registrado
    And Inicia sesion en la plataforma
    And Accede al módulo de información personal.


  Scenario Outline: Agregar Contactos de Emergencia
    Given Busca al empleado por "<id_employee>"
    And Accede a la opcion de contactos.
    When Añade sus contacto de emergencia.
    Then confirma datos del contacto.

    Examples:
    |id_employee|
    |ID17323630|
    |ID10693967|
    |ID19337062|

  Scenario Outline: Agregar Cargas Familiares
    Given Localiza empleado por "<id_employee>".
    And Accede a los detalles del empleado.
    When Añade sus cargas familiares.
    Then confirma los datos añadidos.

    Examples:
    |id_employee|
    |ID17323630|
    |ID10693967|
    |ID19337062|