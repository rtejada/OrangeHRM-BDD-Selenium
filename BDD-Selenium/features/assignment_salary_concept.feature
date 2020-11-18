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
    |ID10469105|ADMINISTRADOR|32600|
    |ID18821339|GERENTE|48200|
    |ID2467284|SUPERVISOR|34800|
    |ID2467284|AUXILIAR|31000|


