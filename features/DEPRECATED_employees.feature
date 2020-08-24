# Created by roxana at 19/08/20
Feature: Administración de Personal.

  Scenario: Agregar Empleados
    Given Un usuario con permisos esta registrado
    When Añade empleados
    Then confirma datos registrados


  Scenario: Editar Datos Empleado
    Given Usuario con permisos de adminitración esta registrado
    When Buscar empleados
    And Editar su Datos Personales
    And Añadir archivos adjuntos
    Then Confirmar que los datos se han registrado