from selenium.webdriver import ActionChains

from Browser import Browser

source_id = "draggable"
x_box_offset = 141
y_box_offset = 41
msg_id = "dropText"
slide = '/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]'
x_slide_offset = 280
y_slide_offset = 16
value_id = "range"


class drag_drop(Browser):

    def setup(self, link):
        self.driver.get(link)

    def drag(self):
        source = self.driver.find_element_by_id(source_id)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(source, x_box_offset, y_box_offset).perform()

    def slide(self):
        slider = self.driver.find_element_by_xpath(slide)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(slider, x_slide_offset, y_slide_offset).perform()

    def msg_box(self):
        m = self.driver.find_element_by_id(msg_id).text
        return m

    def msg_slide(self):
        v = self.driver.find_element_by_id(value_id).text
        return v
