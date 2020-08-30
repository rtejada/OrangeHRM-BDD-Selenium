# Created by roxana at 28/08/20
Feature: Administrar Escalas Salarias.

  Background:
  Given Usuario abre la aplicación OrangeHRM

  Scenario Outline: Añadir Escalas Salarias a los distintos Puestos de Trabajo.
    Given Usuario con permismos registrado.
    And Accede a la opcion Escalas Salariales.
    When Añade escalas salarias a los puestos de Trabajo “<title_scale>”, "<currency>", "<minimum_salary>" , "<maximum_salary>"
    Then confirma datos añadidos “<maximum_salary>”

    Examples:
    |title_scale|currency|minimum_salary|maximum_salary|
    |GERENTE|EUR - Euro|32000|50000|
    |SUPERVISOR|EUR - Euro|30000|40000|
    |ADMINISTRADOR|EUR - Euro|28000|36000|
