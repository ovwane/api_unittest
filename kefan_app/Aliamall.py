#-*- coding:UTF-8 -*-
import time
from appium import webdriver
import unittest
class Share(unittest.TestCase):
    #封装初始化
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appActivity'] = 'com.onemena.simsim.app.SplashActivity'
        desired_caps['appPackage'] = 'com.onemena.simsim'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    def test_login(self):
        self.driver.find_elements_by_id("com.onemena.simsim:id/image")[1].click()



if __name__ == "__main__":
    unittest.main()