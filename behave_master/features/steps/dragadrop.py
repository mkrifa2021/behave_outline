from behave import given,when,then

@given(u'The user is on the dragadrop home page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given The user is on the dragadrop home page')


@when(u'He drags the box to the target under "drop here" message')
def step_impl(context):
    raise NotImplementedError(u'STEP: When He drags the box to the target under "drop here" message')


@then(u'The user should see the message "dropped !"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then The user should see the message "dropped !"')
