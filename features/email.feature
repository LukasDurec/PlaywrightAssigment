Feature: Send an email with an attachment

  Scenario: User sends an email with an attachment
    Given the user is logged into Gmail
    When the user composes a new email
    And the user attaches a file
    And the user sends the email to "me"
    Then the email should be sent successfully
