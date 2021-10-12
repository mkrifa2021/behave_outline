from behave import given,when,then
from numpy.testing import assert_equal

url="http://uitestingplayground.com"

@given(u'User is on the login home page.')
def step_impl(context):
    context.dd.setup(url)

@when(u'User enters "{username}" onto the UserName field.')
def step_impl(context,username):
    context.dd.user(username)

@when(u'User enters "{password}" onto the Password field.')
def step_impl(context,password):
    context.dd.mot(password)
@when(u'User clicks on the Login button.')
def step_impl(context):
    context.dd.log()
@then(u'User verifies if the "{expected}" is displayed')
def step_impl(context,expected):
    msg = context.dd.msg_box()
    assert_equal(msg, expected)


