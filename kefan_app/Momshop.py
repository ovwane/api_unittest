#-*- coding:UTF-8 -*-
from kefan_web.Share import Share
import time
from appium import webdriver
import unittest
from kefan_web.Get_setup import Get_setup
class Momshop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=Get_setup.driver
    def setUp(self):
        pass
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0.1'
        # desired_caps['deviceName'] = 'Android Emulator'
        # desired_caps['appActivity'] = 'com.onemena.simsim.app.SplashActivity'
        # desired_caps['appPackage'] = 'com.onemena.momshop'
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # time.sleep(11)
        # self.driver.tap([[500, 600]])  # 点击新用户通栏
        # time.sleep(6)
        # self.driver.find_element_by_id("com.onemena.momshop:id/iv_get_it").click()  # 点击geeit
        # time.sleep(3)
        # self.driver.find_element_by_name("Log In").click()  # 点击log in
        # time.sleep(2)
        # self.driver.find_element_by_id("com.onemena.momshop:id/et_email").send_keys("1@1.com")  # 输入账号
        # time.sleep(2)
        # self.driver.find_element_by_id("com.onemena.momshop:id/et_password").send_keys("123456")  # 输入密码
        # time.sleep(2)
        # self.driver.find_element_by_id("com.onemena.momshop:id/tv_sign_up").click()  # 点击登录
        # time.sleep(8)

    def cart_pay(self):
        '''【Momshop】下单流程'''
        Share.test001()

    def tearDown(self):
        print u"结束清理"
        self.driver.quit()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()








