Feature: User update
  As user
  I want to update one of my properties
  So that I can obtain my new info

  @seed_user
  Scenario: Successful update
    Given a fresh username "doe@example.com"
    When I update via PUT /update/"test_id"
    