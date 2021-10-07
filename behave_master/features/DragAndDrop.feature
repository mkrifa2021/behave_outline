Feature: drag and drop

	Scenario: dropped successful
	Given The user is on the dragadrop home page
	When  He drags the box to the target under "drop here" message
	Then  The user should see the message "dropped !"
