# Created by roxana at 23/09/20
Feature: Información Personal

  Background:
    Given Usuario con permisos registrado
    And Inicia sesion en la plataforma
    And Accede al módulo de información personal.


  Scenario Outline: Agregar Contactos de Emergencia
    Given Busca al empleado por "<id_employee>"
    And Accede a la opcion de contactos.
    When Añade sus contactos de emergencia.
    Then Confirma los datos de contacto.

    Examples:
    |id_employee|
    |ID1974421|
    |ID19260914|


  Scenario Outline: Agregar Cargas Familiares
    Given Localiza empleado por "<id_employee>".
    And Accede a los detalles del empleado.
    When Añade sus cargas familiares.
    Then confirma los datos añadidos.

    Examples:
    |id_employee|
    |ID1974421|
    |ID19260914|

