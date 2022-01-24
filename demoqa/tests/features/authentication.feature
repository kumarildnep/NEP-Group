Feature: Authentication

Scenario: Verify user authentication
    Given user navigates to login page
    When user enters valid "User Name" and "Password"
    And user clicks on Login button
    Then user successfully login


Scenario: Verify authentication failure
    Given user navigates to login page
    When user enters "Invalid Username" and "Incorrect Password"
    And user clicks on Login button
    Then user login is unsuccessful