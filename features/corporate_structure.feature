# Created by roxana at 9/09/20
Feature: Información General sobre la Organización.

  Scenario: Añadir información.
    Given Usuario administrador conectado.
    And Accede a la opcion Información General.
    When Edita y añade la informacion general.
    Then Confirma información registrada.



