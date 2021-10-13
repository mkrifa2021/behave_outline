from behave import given,when,then
from numpy.testing import assert_equal

url="https://qavbox.github.io/demo/dragndrop/"
expected_result="Dropped!"

@given(u'The user is on the dragadrop home page')
def step_impl(context):
    context.dd.setup(url)

@when(u'He drags the box to the target under "drop here" message')
def step_impl(context):
    context.dd.drag()

@then(u'The user should see the message "dropped !"')
def step_impl(context):
        msg=context.dd.msg_box()
        assert_equal(msg,expected_result)