# Created by roxana at 23/09/20
Feature: Asignar los Conceptos Salariales.

  Scenario Outline: Asigna salario segun Puesto de Empleo.
   Given Usuario administrador registrado.
   And Inicia sesion y accede a la opcion correspondiente.
   When Busca y selecciona empleado por “<id_employee>”
   And Accede a la opcion Salarios
   And Añade salario segun escala salarial "<escala>", "<monto>"
   Then Confirma componente salarial registrado

    Examples:
    |id_employee|escala|monto|
    |ID17323630|ADMINISTRADOR|32600|
    |ID10693967|AUXILIAR|31000|
    |ID10593465|GERENTE|48200|
    |ID19337062|SUPERVISOR|34800|


