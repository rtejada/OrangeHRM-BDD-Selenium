# Created by roxana at 19/11/20

Feature: Gestión de Datos de Contacto.
  Como usuario con permisos
  Quiero asegurarme, los pasos informados en la documentación, hacen
  lo que se supone que debe hacer...

  Background:
    Given URL Base con parametros de Autentificación.

  Scenario Outline: Añadir Datos de Contacto de los Empleados.
    Given Establecer parametros para para añadir los datos de contacto del empleado <id_emp>.
    When Realizar nueva petición POST.
    Then Confirmar Estado 200 (Datos de contacto añadidos).
    And  Recuperar datos de contactos añadidos con una petición GET
    And  Confirmar datos añadidos del empleado.

    Examples:
    |id_emp|
    | 153  |
    | 156  |

  Scenario Outline: Actualizar Datos de Contacto de los Empleados.
    Given Establecer parametros para para actualizar los datos de contacto del empleado <id_emp>.
    When Realizar nueva petición PUT.
    Then Confirmar Estado 200 (Datos de contacto actualizados).
    And  Recuperar los datos de contactos actualizados con una petición GET
    And  Confirmar datos actualizados del empleado.

    Examples:
    |id_emp|
    | 153  |
    | 156  |




