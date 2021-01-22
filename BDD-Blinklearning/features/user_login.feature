# Created by roxana at 22/01/21
Feature: #Enter feature name here
  # Enter feature description here

  Scenario Outline: Login en la web.
    Given Usuario no registrado accede a la web.
    When Inserta credenciales no autorizadas<email>, <password>.
    Then Muestra aviso acceso incorrecto.

    Examples:
    |email|password|
    |rtejadasilva@gmail.com|12345|
