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
    |Diurno|09:00 |18:00|Pepe-6508 B8bMAHjpg CNBIgaaHn|Diego-14060 BKYQKXR9T CRO7NZkA6|
    |Tarde|15:45 |23:45|Pepe-6508 B8bMAHjpg CNBIgaaHn|Diego-14060 BKYQKXR9T CRO7NZkA6|
    |Parcial-Tarde|15:00 |20:00|Pepe-6508 B8bMAHjpg CNBIgaaHn|Diego-14060 BKYQKXR9T CRO7NZkA6|

