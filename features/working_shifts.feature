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
    |Completa-Diurno|09:00 |18:00|Acounselled Bsexualized Cpassionateness|Ainconvenienced Brestriping Cpicramate|
    |Completa-Tarde|15:45 |23:45|Atimewarps Bprepossession Crasing|Ajagger BBronx CPontypool|
    |Parcial|12:00 |16:00|Awhatevers Binfirmative Cspirea|Aconceipt Bbedrobe CSchutzstaffel|

