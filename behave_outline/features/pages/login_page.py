from Browser import Browser

class login_page(Browser):

    def setup(self, link):
        self.driver.get(link)
        self.driver.find_element_by_link_text("Sample App").click()

    def user(self,user):
        if user!="None" :
            self.driver.find_element_by_name("UserName").send_keys(user)

    def mot(self,pwd):
        if pwd !="None" :
            self.driver.find_element_by_name("Password").send_keys(pwd)

    def log(self):
        self.driver.find_element_by_id("login").click()

    def msg_box(self):
        m= self.driver.find_element_by_id("loginstatus").text
        return m
