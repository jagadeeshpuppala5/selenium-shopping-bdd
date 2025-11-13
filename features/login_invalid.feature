Feature: Verify login with Invalid Credentials


  Scenario: Login with invalid credentials
    Given user is on home page
    When user clicks on Signup/Login link
    And enters invalid email "chinnaa@test.com" and password "Test@123"
    Then "Your email or password is incorrect!" should be displayed