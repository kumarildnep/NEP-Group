Feature: Book Store Search

Scenario: Book Search
    Given user navigate to DemoQA website
    When user navigates to book search page
    And user clicks on goto book store button
    And user types the "Search Key" in search input
    Then books related "Search Key" are displayed

Scenario: Verify search book details
    Given user navigate to DemoQA website
    When user navigates to book search page
    And user clicks on goto book store button
    And user types the "Search Key" in search input
    And user clicks on the link prompted
    Then details of the book are displayed