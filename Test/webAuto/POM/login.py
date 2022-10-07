from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from eventAnalysis_fanhuapolicy import EventAnalysis_fanhuaPolicy
from webAuto.POM.create_data import create_data

@create_data("D:/Files/pypro/Test/data/pom_data/LoginPage.json")
class LoginPage:
    # url = "https://172.16.16.96"

    class Button:
        # detail = (By.XPATH, '//button[@id="details-button"]')
        # login = (By.XPATH, '//*[@onclick="submitForm(this.form)"]')
        # # save = (By.XPATH, '//button[@class="ivu-btn ivu-btn-primary"]')
        # save = (By.XPATH, '//span[text()="保存"]')
        pass

    class Link:
        # proceed_link = (By.LINK_TEXT, "继续前往172.16.16.96（不安全）")
        pass

    class Input:
        # username = (By.XPATH, '//*[@id="username"]')
        # password = (By.XPATH, '//*[@id="password"]')
        # passwds = (By.CSS_SELECTOR,
        #            'div.ivu-modal-content>div.ivu-modal-body>form.ivu-form.ivu-form-label-right>div.ivu-form-item>div.ivu-form-item-content>div.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type-password>input.ivu-input.ivu-input-default')
        pass
    def __init__(self, driver):
        self.driver = driver

    def ToLoginPage(self):
        self.driver.find_element(*self.Button.detail).click()
        self.driver.find_element(*self.Link.proceed_link).click()

    def login(self, username, password):
        self.driver.find_element(*self.Input.username).send_keys(username)
        self.driver.find_element(*self.Input.password).send_keys(password)
        self.driver.find_element(*self.Button.login).click()

    def updatepasswd(self, oldpasswd, newpasswd, repasswd):
        time.sleep(10)  # 因为上面的点击让界面发生了变化，所以在点击之后等待页面渲染完成就好了

        pa = self.driver.find_elements(*self.Input.passwds)
        pa[0].send_keys(oldpasswd)
        pa[1].send_keys(newpasswd)
        pa[2].send_keys(repasswd)
        # self.driver.find_elements(*self.Button.save)[0].click()
        self.driver.find_element(*self.Button.save).click()
# if __name__ == ('__main__'):
    # driver = webdriver.Chrome()

    # driver.get(LoginPage.url)
    # driver.maximize_window()
    # LP = LoginPage(driver)
    # LP.ToLoginPage()
    # LP.login("operator", "Silvers$R7")
    # pp = EventAnalysis_fanhuaPolicy(driver)
    # pp.create_policy()
    # LP.login("admin", "admin")
    # LP.updatepasswd("admin", "Silvers$R7", "Silvers$R7")
