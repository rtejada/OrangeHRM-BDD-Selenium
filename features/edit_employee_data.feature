# Created by roxana at 14/09/20
Feature: Editar Datos Empleado
  # Enter feature description here

 Scenario Outline: Editar Datos Empleado
   Given Usuario con permisos registrado.
   And Incia sesion en OrangeHRM.
   When Busca empleado “<id_employee>”
   And Edita sus datos personales
   And Añade archivos adjuntos
   And Añade Datos de Contacto.
   And Añade Datos de Contactos de Emergencia.
   And Añade sus Cargas Familiares.
   And Registra datos de Inmigración.
   And Añade Puestos de Trabajo.
   And Añade el Salario/Sueldo.
   And Reporta datos a
   And Registra Curriculum
   And Registra Menbresías
   Then Confirma que los datos quedaron registrado

    Examples:
    |id_employee|
    |ID17323630|
    |ID10693967|
    |ID10593465|
    |ID19337062|
