import os

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver
from pages.login_page import login_page

def before_scenario(context,scenario):
    dir = os.getcwd()
    option=webdriver.ChromeOptions()
    #option.add_argument("--start-maximized")
    option.add_argument("headless")
    config_file = "\config_files\chromedriver.exe"
    context.browser = webdriver.Chrome(executable_path=dir + config_file, chrome_options=option)
    #context.browser = webdriver.Chrome(executable_path=dir + config_file)
    context.dd=login_page(context.browser)

def after_scenario(context,scenario):
    context.browser.quit()
def after_step(context,step):
    if step.status == "failed":
        context.browser.save_screenshot('c://b/screenshot.png')
        attach(
            context.browser.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG)
