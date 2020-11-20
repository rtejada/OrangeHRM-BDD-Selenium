# Created by roxana at 3/11/20

Feature: Gestión de Empleados.
  Como usuario con permisos
  Quiero asegurarme, los pasos informados en la documentación, hacen
  lo que supone que debe hacer...

  Background: Establecer Conexión con el Background de Destino.
    Given Se establece URL base con sus parametros de autentificación.
    And Se establece el parametro necesario para crear nuevo empleado.
    When Realizar una petición POST.
    Then Confirmar Estado 200 (empleado creado con exito).

  Scenario: Recuperar y confirmar los datos del Empleado Creado.
    Given Establecer parametros para recuperar el usuario.
    When Se recupera los Datos del Empleado con una petición GET.
    Then Se confirman datos del empleado.

  Scenario: Actualizar Datos del Empleado.
    Given Se establece el parametro requerido para actualizar los datos.
    When Los datos del empleado se actualizan con una petición PUT.
    Then Se Confirma estado 200 (datos del empleado actualizado con exito).
    And Establecer parametros para recuperar los datos del usuario.
    And  Recuperar Datos actualizados con una petición GET
    And  Se confirman datos actualizados del empleado.

