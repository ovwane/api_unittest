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
        desired_caps['appPackage'] = 'com.onemena.momshop'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(15)
        self.driver.tap([[500, 600]])  # 点击新用户通栏
        time.sleep(5)
        self.driver.find_element_by_id("com.onemena.momshop:id/iv_get_it").click()  # 点击geeit
        time.sleep(2)
        self.driver.find_element_by_name("Log In").click()  # 点击log in
        time.sleep(2)
        self.driver.find_element_by_id("com.onemena.momshop:id/et_email").send_keys("1@1.com")  # 输入账号
        time.sleep(2)
        self.driver.find_element_by_id("com.onemena.momshop:id/et_password").send_keys("123456")  # 输入密码
        time.sleep(2)
        self.driver.find_element_by_id("com.onemena.momshop:id/tv_sign_up").click()  # 点击登录
        time.sleep(3)

    def test001(self):
        '''添加购物车到下单'''
        self.driver.swipe(300,1000,600,160, 1500)  # 上滑免费礼物页面
        self.driver.find_elements_by_id("com.onemena.momshop:id/tv_name")[0].click()#点击推荐商品进入详情
        time.sleep(6)
        self.driver.find_element_by_name("Add To Cart").click()#点击添加购物车按钮
        time.sleep(2)
        self.driver.find_element_by_name("Pink/90cm").click()#选择规格
        time.sleep(1)
        self.driver.find_element_by_id("com.onemena.momshop:id/tv_add_to_cart").click()#点击加入购物车按钮
        time.sleep(2)
        self.driver.find_element_by_id("com.onemena.momshop:id/iv_cart").click()#点击购物车按钮
        time.sleep(3)
        self.driver.swipe(300, 800, 600, 200, 1500)  # 上滑
        self.driver.find_element_by_id("com.onemena.momshop:id/tv_checkout").click()#点击提交--确认订单页
        time.sleep(3)
        self.driver.find_element_by_name("Proceed to Payment").click()#点击支付--选择支付页
        time.sleep(3)
        self.driver.find_element_by_name("Verify").click()#点击货到付款
        time.sleep(3)
        self.driver.find_element_by_id("com.onemena.momshop:id/tv_my_orders").click()#点击myorders
        self.assertEqual("My Orders", self.driver.find_element_by_name("My Orders").text, msg=None)








