# Created by roxana at 9/09/20
Feature: Estructura Organizacional - Añadir Localizaciones.

  Background: Usuario conectado.
    Given Accede a la aplicación OrangeHRM.

  Scenario Outline: Añadir Localizaciones de la Organización.
    Given usuario admin registrado.
    And Accede a la opcion Localizaciones.
    When Añade Ubicaciones "<first_name>", "<city>"
    Then confirma Ubicaciones registradas
    And Elimina Ubicaciones

    Examples:
    |first_name|city|
    |S.A.|Madrid    |
    |S.L.|Barcelona |
    |S.Coop.|Galicia|
