Feature: Verify Login with Valid Credentials


  Scenario: Login using valid credentials
    Given user is on home page
    When user clicks on Signup/Login link
    And enters valid email "chinna@test.com" and password "Test@123"
    Then "Logged in as chinna" should be visible