# Created by roxana at 15/09/20
Feature: Añadir Curriculum Vitae

 Scenario Outline: Insertar experiencia laboral, formacion y habiliadades.
   Given Usuario con permisos de administración registrado.
   And Inicia sesion y accede al Modulo de Información Personal.
   When Busca el empleado por su "<identificacion>"
   And Accede a su datos personales y añade su "<fotografia>"
   And Añade su experiencia laboral, su formacion y sus habiliadades “<puesto>”, “<empresa>”
   Then Confirma los datos registrados.

    Examples:
    |identificacion|puesto|empresa|categoria|fotografia|
    |ID17323630|ADMINISTRADOR|IKEA|Officials and Managers|image1.jpg|
    |ID10693967|AUXILIAR|CANON|Professionals|image2.jpg|
    |ID10593465|GERENTE|YAHOO|Service Workers|neo.jpg|
    |ID19337062|SUPERVISOR|SONY|Technicians|image1.jpg|
