# Created by roxana at 14/09/20
Feature: Editar Datos Empleado
  # Enter feature description here

 Scenario Outline: Editar Datos Empleado
   Given Usuario con permisos registrado.
   And Incia sesion en OrangeHRM.
   When Busca empleado “<id_employee>”
   And Edita sus datos personales y añade archivo adjunto "<img>"
   And Añade Datos de Contacto y archivo adjunto "<img>"
   And Añade Puesto de Trabajo y archivo adjunto "<titulo_puesto>","<categoria>","<ubicacion>","<img>"
   Then Confirma que los datos quedaron registrado “<id_employee>”, “<titulo_puesto>”

    Examples:
    |id_employee|titulo_puesto|ubicacion|categoria|img|
    |ID17323630|ADMINISTRADOR|A4aDNuQgIV S.A.|Officials and Managers|image1.jpg|
    |ID10693967|AUXILIAR|XQQxZOtB3N S.Coop.|Professionals|image2.jpg|
    |ID10593465|GERENTE|PPQDGYX6MJ S.A.|Service Workers|neo.jpg|
    |ID19337062|SUPERVISOR|TUf5PHPo1k S.L.|Technicians|image1.jpg|







