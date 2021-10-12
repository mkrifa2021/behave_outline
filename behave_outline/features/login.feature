Feature: login for multiple sets of test data.
Scenario Outline: To verify if login is successful for multiple sets of test data.
Given User is on the login home page.
When User enters "<username>" onto the UserName field.
And User enters "<password>" onto the Password field.
And User clicks on the Login button.
Then User verifies if the "<expected>" is displayed

Examples:

|username|password|expected|
|Elyess|pwd|Welcome, Elyess!|
|None|None|Invalid username/password|
|Maamoun|pwd|Invalid username/password|
|None|pwd|Invalid username/password|
|Elyess|None|Invalid username/password|
|Elyess|pwd1|Invalid username/password|
|Maamoun|pwd2|Invalid username/password|