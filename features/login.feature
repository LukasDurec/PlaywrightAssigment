Feature: User Login and Logout

  Scenario: Successful Login
    Given the user is on the login page
    When the user enters a valid email
    And the user enters a valid password
    Then the user should be redirected to the inbox

  Scenario: Unsuccessful Login with Invalid Credentials
    Given the user is on the login page
    When the user enters an invalid email
    Then an invalid username error message should be displayed

  Scenario: Unsuccessful Login with Incorrect Password
    Given the user is on the login page
    When the user enters a valid email
    And the user enters an incorrect password
    Then an invalid password error message should be displayed

  Scenario: Logout
    Given the user is logged in
    When the user clicks on the profile icon
    And the user clicks on the "Sign out" button
    Then the user should be redirected to the logout page
