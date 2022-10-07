import unittest
from selenium import webdriver
from webAuto.POM.eventAnalysis_fanhuapolicy import EventAnalysis_fanhuaPolicy
from webAuto.POM.login import LoginPage
from testcase.ddt import ddt
from webAuto.POM.Context import Context

@ddt.ddt
class Test(unittest.TestCase):

    # @ddt.file_data("D:/Files/pypro/Test/data/test_data/test_login.json")
    def test_login(self):
        driver = webdriver.Chrome()
        setattr(Context,"driver",driver)
        # driver = getattr(Context, "driver")
        driver.get(LoginPage.url)
        driver.maximize_window()
        LP = LoginPage(driver)
        LP.ToLoginPage()
        LP.login("operator", "Silvers$R7")

    def test_CreatePolicy(self):
        # driver = getattr(Context,"driver")

        driver = webdriver.Chrome()
        driver.get(LoginPage.url)
        driver.maximize_window()
        pp = EventAnalysis_fanhuaPolicy(driver)
        pp.create_policy()
    #     LP.login("admin", "admin")
    #     LP.updatepasswd("admin", "Silvers$R7", "Silvers$R7")
    # @classmethod
    # def setUpClass(cls):
    #     driver = webdriver.Chrome()
    #     setattr(Context, "driver", driver)
    #
    # @classmethod
    # def tearDown(self):
    #     getattr(Context,"driver").quit()
    #
    # @classmethod
    # def tearDownClass(cls):
    #     getattr(Context,"driver").quit()