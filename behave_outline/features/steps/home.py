from behave import given

url="http://uitestingplayground.com"

@given(u'User is on the login home page.')
def step_impl(context):
    context.dd.setup(url)
