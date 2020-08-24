# Created by roxana at 24/08/20
Feature: Módulo de Información Personal.

  Background:
    Given un usuario registrado

  Scenario Outline: Agregar nuevos empleados
    Given El usuario tiene permisos de administración.
    When Añade nuevo empleados “<cod>”, "<p_nombre>", "<s_nombre>", "<apellidos>", "<usu>", "<pwd>"
    Then confirma datos del nuevo empleado

    Examples:
    |cod|p_nombre|s_nombre|apellidos|usu|pwd|
    |D|A|B|C|Usu|$%Orange%|


  Scenario: Listar y Editar Datos Empleado
    Given El usuario tiene permisos de administración.
    When Busca el nuevo empleado
    And Edita los datos personales
    And Añade archivos adjuntos
    Then Confirma que los datos quedaron registrado