# Created by roxana at 3/09/20
Feature: Administrar Turnos de Trabajo

  Background:
    Given Usuario admin registrado

  Scenario Outline: Agregar Turnos de Trabajo
    Given El Usuario tiene permisos para agregar los turnos de trabajo.
    And Accede a la opcion Turnos de Trabajo
    When Agrega Turnos de Trabajo “<nom_turno>”, "<desde>", "<hasta>", "<empleado_1>"
    And Agrega mas empleado “<nom_turno>”, “<empleado_2>”
    Then Confirma los turnos de trabajo Añadidos “<nom_turno>”
    And Eliminar Turno de Trabajo “<nom_turno>”


    Examples:
    |nom_turno|desde|hasta|empleado_1|empleado_2|
    |Diurno-Completo|09:00 |18:00|159|164|
    |Tarde-Completo|15:45 |23:45|168|165|


