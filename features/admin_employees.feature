# Created by roxana at 24/08/20
Feature: Módulo de Información Personal.

  Background:
    Given Un usuario registrado

  Scenario Outline: Agregar nuevos empleados
    Given El usuario tiene permisos de administración.
    When Añade nuevo empleados “<cod>”, "<p_nombre>", "<s_nombre>", "<apellidos>", "<usu>", "<pwd>"
    Then confirma datos del nuevo empleado

    Examples:
    |cod|p_nombre|s_nombre|apellidos|usu|pwd|
    |ID|Pedro|B|C|Usu|$%Orange%|

