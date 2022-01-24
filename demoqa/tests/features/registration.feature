Feature: Registration

Scenario: Verify user successful registration
    Given user navigate to DemoQA website
    When user clicks on New User button
    And user provides "First Name","Last Name","New User Name" and "New Password"
    And user clicks on Register button
#    Then it successfully register the user