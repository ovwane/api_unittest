# coding=utf-8
from appium import webdriver

import time,unittest
class Footballxianxing(unittest.TestCase):
    def setUp(self):
        print u"初始化"
        global driver
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appActivity'] = 'com.taobao.tao.welcome.Welcome'
        desired_caps['appPackage'] = 'com.taobao.taobao'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)
    def tearDown(self):
        print u"结束清理"
        driver.quit()
        time.sleep(2)
    '''淘寶登錄走一個'''
    def login(self):
        driver.find_element_by_class_name("android.widget.LinearLayout")[4].click()
        time.sleep(2)

        # driver.find_element_by_id("com.wekoora.football:id/deatil_attention_btn").click()
        # time.sleep(2)
        # 取消订阅
        # driver.find_element_by_id("com.wekoora.football:id/deatil_attention_btn").click()
        # time.sleep(2)
        # # 点击返回
        # driver.find_element_by_id("com.wekoora.football:id/back_iv").click()
        # time.sleep(2)
        # # 下拉刷新
        # driver.swipe(612, 371, 612, 1000, 2000)
        # time.sleep(5)
        # for i in range(0,5):
        #     driver.swipe(80, 850, 660, 850, 2000)
        #     time.sleep(5)
        #     driver.swipe(612, 371, 612, 1000, 2000)
        #     time.sleep(5)


        # driver.tap([[600,700]])
        # time.sleep(2)
        # #点击赛事
        # driver.tap([[350,1200]])
        # time.sleep(5)
        # #向左滑动到射手榜
        # driver.swipe(80,850,660,850,2000)
        # time.sleep(5)
        # # 下拉刷新
        # driver.swipe(612, 371, 612, 1000, 2000)
        # time.sleep(5)
        # #循环滑动下拉
        # for i in range(0,5):
        #     driver.swipe(80, 850, 660, 850, 2000)
        #     time.sleep(5)
        #     # 下拉刷新
        #     driver.swipe(612, 371, 612, 1000, 2000)
        #     time.sleep(5)
        # # 向左滑动到赛程榜
        # driver.swipe(80, 850, 660, 850, 2000)
        # time.sleep(5)
        # #下拉刷新
        # driver.swipe(612,371,612,1000,2000)
        # time.sleep(5)
        # # 向左滑动
        # driver.swipe(80, 850, 660, 850, 2000)
        # time.sleep(5)
        # # 下拉刷新
        # driver.swipe(612, 371, 612, 1000, 2000)
        # time.sleep(5)
        # # 向左滑动
        # driver.swipe(80, 850, 660, 850, 2000)
        # time.sleep(5)
        # # 下拉刷新
        # driver.swipe(612, 371, 612, 1000, 2000)
        # time.sleep(5)
        # # 向左滑动
        # driver.swipe(80, 850, 660, 850, 2000)
        # time.sleep(5)
        # # 下拉刷新
        # driver.swipe(612, 371, 612, 1000, 2000)
        # time.sleep(5)
        # # 向左滑动
        # driver.swipe(80, 850, 660, 850, 2000)
        # time.sleep(5)
        # # 下拉刷新
        # driver.swipe(612, 371, 612, 1000, 2000)
        # time.sleep(5)
        # #点击推荐页按钮
        # driver.tap([[628,1200]])
        # time.sleep(5)
        # #点击一篇文章
        # driver.tap([[500,685]])
        # time.sleep(8)
        # # 向下滑动
        # driver.swipe(550,1140,550,87, 3000)
        # time.sleep(8)
        # # 点击点赞按钮
        # driver.tap([[480,1100]])
        # time.sleep(2)
if __name__ == "__main__":
    unittest.main()
