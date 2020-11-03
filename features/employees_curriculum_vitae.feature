# Created by roxana at 15/09/20
Feature: Añadir Curriculum Vitae

 Scenario Outline: Insertar experiencia laboral, formacion y habiliadades.
   Given Usuario con permisos de administración registrado.
   And Inicia sesion y accede al Modulo de Información Personal.
   When Busca el empleado por su "<identificacion>"
   And Accede a su datos personales y añade su "<fotografia>"
   And Añade su experiencia laboral, su formacion y sus habiliadades “<puesto>”, “<empresa>”
   Then Confirma los datos registrados “<empresa>”.

    Examples:
    |identificacion|puesto|empresa|fotografia|
    |ID17323630|ADMINISTRADOR|IKEA|image1.jpg|
    |ID10693967|AUXILIAR|CANON|image2.jpg|
    |ID10593465|GERENTE|YAHOO|neo.jpg|
    |ID19337062|SUPERVISOR|SONY|image1.jpg|
