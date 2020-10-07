# Created by roxana at 3/09/20
Feature: Administrar Turnos de Trabajo

  Background:
    Given Usuario admin registrado

  Scenario Outline: Agregar Turnos de Trabajo
    Given El Usuario tiene permisos para agregar los turnos de trabajo.
    And Accede a la opcion Turnos de Trabajo
    When Agrega Turnos de Trabajo “<nom_turno>”, "<desde>", "<hasta>", "<empleado>"
    And Agrega mas empleado “<nom_turno>”, “<empleados>”
    Then Confirma los turnos de trabajo Añadidos “<nom_turno>”
    And Eliminar Turno de Trabajo “<nom_turno>”


    Examples:
    |nom_turno|desde|hasta|empleado|empleados|
    |Diurno-Completo|09:00 |18:00|Pablo-13086 BFgk2BNwN C8WLD9rMH|Pepe-16201 BQTPNBa5n CFgNEp4UY|
    |Tarde-Completo|15:45 |23:45|Pedro-18201 BGAOFYJIP CSLDRJueF|Pepe-3549 BRBeNXU3c CYx9UaUAM|


