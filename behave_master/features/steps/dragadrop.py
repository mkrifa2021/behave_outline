from behave import given,when,then
from numpy.testing import assert_equal
from selenium import webdriver
from selenium.webdriver import ActionChains

@given(u'The user is on the dragadrop home page')
def step_impl(context):
    context.driver= webdriver.Chrome('c:\driver\chromedriver.exe')
    driver=context.driver
    driver.get("https://qavbox.github.io/demo/dragndrop/")

@when(u'He drags the box to the target under "drop here" message')
def step_impl(context):
    driver=context.driver
    source = driver.find_element_by_id("draggable")
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(source, 141, 41).perform()

@then(u'The user should see the message "dropped !"')
def step_impl(context):
        driver=context.driver
        msg=driver.find_element_by_id("dropText").text
        assert_equal(msg,"Dropped!")
        driver.quit()



