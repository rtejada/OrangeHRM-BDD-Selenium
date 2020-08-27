# Created by roxana at 27/08/20
Feature: Administrar Puestos de Trabajo.

  Background:
  Given Un usuario abre la aplicación OrangeHRM

  Scenario Outline: Añadir Puestos de Trabajo.
    Given Usuario registrado.
    And Accede a la opcion Puestos de Trabajo.
    When Añade varios puestos de Trabajo “<title>”, "<job_description>", "<note>"
    Then Confirma titulos de los puestos añadidos

    Examples:
    |title|job_description|note|
    |GERENTE|Establece las prioridades laborales y gestiona los gastos de la empresa|Dpto FINANAZAS|
    |SUPERVISOR|Observa y dirige al personal para orientarlo y vigilarlo en el cumplimiento de sus funciones|Dpto PRODUCCION|
    |ADMINISTRADOR|Obtiene resultados a traves de otras personas.Es el responsable de llevar a cabo las actividades necesarias para alcanzar las metas organizacionales|Dpto VENTAS|
