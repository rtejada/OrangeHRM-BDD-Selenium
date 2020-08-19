# Created by roxana at 19/08/20
Feature: Administración de Personal.

  Scenario: Agregar Empleados
    Given Un usuario con permisos esta registrado
    When Añade empleados
    Then confirma datos registrados