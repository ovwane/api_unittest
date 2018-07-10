#-*- coding:UTF-8 -*-
from appium import webdriver
from selenium import webdriver
import unittest
import time
from kefan_web.Common import singleton
@singleton
class Get_setup(unittest.TestCase):
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = "https://www.baidu.com/"
        self.driver.maximize_window()
        time.sleep(2)
    #
    # #打开网页
    # def openH5(self):
    #     self.chrome.openWeb(self.url.MomShopH5_URL)
    #     pass
    # #关闭网页
    # def closeH5(self):
    #     self.chrome.closeChrome()
    #     pass
    # #控件点击
    # def checkcontrol(self):
    #     self.chrome.FindXP("#app > div > div.tabBar > div > div > div.tab-item.router-link-exact-active.router-link-active > div > i").click()
    #
    #     pass
    # pass
