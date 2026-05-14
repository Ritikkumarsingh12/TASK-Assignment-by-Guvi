Feature: OrangeHRM Login Functionality

  Scenario: Successful Login
    Given User launches OrangeHRM portal
    When User enters valid username and password
    And User clicks login button
    Then User should login successfully

  Scenario: Invalid Login
    Given User launches OrangeHRM portal
    When User enters invalid username and password
    And User clicks login button
    Then Error message should be displayed

  Scenario: Validate Logout
    Given User launches OrangeHRM portal
    When User enters valid username and password
    And User clicks login button
    Then User should logout successfully