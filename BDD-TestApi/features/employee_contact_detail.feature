# Created by roxana at 19/11/20

Feature: Gestión de Datos de Contacto.
  Como usuario con permisos
  Quiero asegurarme, los pasos informados en la documentación, hacen
  lo que se supone que debe hacer...

  Background: Establecer Conexión con el Background de Destino.
    Given Se establece URL base con parametros de autentificación.

  Scenario Outline: Recuperar y confirmar los datos del Empleado Creado.
    Given Establecer parametros para para añadir los datos de contacto del empleado <id_emp>.
    When Realizar nueva petición POST.
    Then Confirmar Estado 200 (Datos de contacto actualizados).
    And  Establecer parametros para recuperar los datos de contacto del usuario.
    And  Recuperar datos de contactos actualizados con una petición GET
    And  Confirmar datos actualizados del empleado.

    Examples:
    |id_emp|
    | 200  |
    | 210  |
    | 250  |
    | 212  |
    | 222  |
    | 230  |
    | 231  |
    | 237  |
    | 300  |


