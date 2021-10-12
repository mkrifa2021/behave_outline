Feature: slide

	Scenario: slide progress
	Given The user is on the dragadrop home page
	When  He drags the slide to the end
	Then  he sees the 100 value
