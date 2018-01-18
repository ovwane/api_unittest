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
        desired_caps['deviceName'] = 'ZX1G22DPVW'
        desired_caps['appActivity'] = 'com.onemena.app.activity.SplashActivity'
        desired_caps['appPackage'] = 'com.wekoora.football'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        time.sleep(2)

    '''【足球】关注'''
    def testcase001(self):
        pass
        # for i in range(3):
        #     self.driver.swipe(1350, 330, 123, 330, 1000)#移动关注导航栏
        # self.driver.tap([[1300, 340]])#点击兴趣频道
        # time.sleep(2)
        # self.driver.swipe(750, 723, 750, 1800, 1000)  #下拉刷新一次
        # time.sleep(2)
        # for i in range(10):
        #     self.driver.swipe(752, 2025, 752, 700, 1000)  # 上拉拉刷新一次


if __name__ == "__main__":
    unittest.main()
    #     self.driver.find_element_by_id("com.wekoora.football:id/img_login_fb").click()
    #     time.sleep(3)
    #     #点击金币任务查看
    #     self.driver.find_element_by_id("com.wekoora.football:id/rl_gold_task").click()
    #     #点击返回键
    #     self.driver.tap([[1300,200]])
    #     #点击首页
    #     self.driver.find_element_by_name("الرئيسية").click()
    #     #点击频道
    #     self.driver.find_element_by_name("مغربي").click()
    #     # 点击文章
    #     self.driver.tap([[1000,1000]])
    #     time.sleep(5)
    #     # 点击更多
    #     self.driver.find_element_by_id("com.wekoora.football:id/menu_iv").click()
    #     time.sleep(5)
    #     #点赞点踩
    #     for i in range(0, 2):
    #         #点击两次
    #         self.driver.find_element_by_id("com.wekoora.football:id/iv_like").click()
    #     #点击取消
    #     self.driver.find_element_by_id("إلغاء").click()
    #     # 点击输入框
    #     self.driver.tap([[700, 2000]])
    #     time.sleep(2)
    #
    #
    #
    #
    #
    #
    #
    # #【新闻】评论用例从点击进入详情页到评论列表
    # def testcase02(self):
    #     # 点击弹出框
    #     self.driver.tap([[600, 700]])
    #     time.sleep(2)
    #     # 点击弹出框
    #     self.driver.tap([[450, 800]])
    #     time.sleep(2)
    #     # 点击置顶图
    #     self.driver.tap([[500, 700]])
    #     time.sleep(5)
    #     #点击评论
    #     self.driver.tap([[620, 1200]])
    #     time.sleep(3)
    #     #点击输入框
    #     self.driver.find_element_by_id("com.arabsada.news:id/et_comment").send_keys("good")
    #     time.sleep(2)
    #     #点击提交
    #     self.driver.find_element_by_id("com.arabsada.news:id/comment_ok").click()
    #     time.sleep(5)
    #     #点击评论框
    #     self.driver.tap([[420,1200]])
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id=\"com.arabsada.news:id/et_comment\"]").send_keys("goog")
    #     time.sleep(5)
    #     #点击提交
    #     self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.arabsada.news:id/comment_ok\"]").click()
    #     time.sleep(4)
    #     #点击导航栏返回按钮
    #     self.driver.tap([[650, 100]])
    #     time.sleep(2)
    #     # 点击导航栏返回按钮
    #     self.driver.tap([[650, 100]])
    #     time.sleep(2)
    # #足球测试用例（进入赛事进行刷新操作）
    # def testcase003(self):
    #     #点击更新提示
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     time.sleep(2)
    #     #点击赛事赛程按钮
    #     self.driver.tap([[380,1100 ]])
    #     time.sleep(3)
    #     # 循环滑动刷新
    #     for i in range(0, 3):
    #         #向下刷新3次
    #         self.driver.swipe(392,342,392,900, 1000)
    #         time.sleep(5)
    #         #向右滑动切换射手榜
    #         self.driver.swipe(70,500,700,500, 1000)
    #         time.sleep(3)
    #         # 向下刷新3次
    #         self.driver.swipe(372, 400, 372, 1000, 1000)
    #         time.sleep(3)
    #         # 向右滑动切换赛程
    #         self.driver.swipe(90, 500, 700, 500, 1000)
    #         # 向下刷新3次
    #         self.driver.swipe(372, 400, 372, 1000, 1000)
    #         time.sleep(3)
    #         #向右切换到一级导航栏
    #         self.driver.swipe(37,443,694,443,1000)
    #         time.sleep(3)
    #     #点击首页按钮
    #     self.driver.tap([[700,1100 ]])
    #     time.sleep(2)
    #     #点击轮播图
    #     self.driver.find_element_by_id("com.wekoora.football:id/simple_img").click()
    #     time.sleep(2)
    #
    #










