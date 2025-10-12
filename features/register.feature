Feature: User registration
  As a new user
  I want to register
  So that I can obtain an access token

  Scenario: Successful registration
    Given a fresh username "italia@example.com" and password "Secret123!"
    When I register via POST /register
    Then the response status should be 201
    And the response should contain fields "id" and "access_token"
    And the response "username" should equal "italia@example.com"

    Scenario: Registration conflict
      Given a fresh username "italia@example.com" and password "Secret123!"
      When I register via POST /register
      And I register via POST /register
      Then the response status should be 409