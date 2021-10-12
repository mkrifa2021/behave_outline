from behave import when,then
from numpy.testing import assert_equal

expected_result="100"

@when(u'He drags the slide to the end')
def step_impl(context):

    context.dd.slide()

@then(u'he sees the 100 value')
def step_impl(context):
    v = context.dd.msg_slide()
    assert_equal(v, expected_result)

