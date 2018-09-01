#coding:utf-8
from selenium import webdriver
import time
import unittest
# from selenium.webdriver.support import expected_conditions as EC
class Run(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://newbeta-auth.izhikang.com/login")
        self.driver.maximize_window()
        time.sleep(3)
    def test_001(self):
        '''进入老业务系统完成登录操作'''
        self.driver.implicitly_wait(15)

        expValue = u"汪慧"
        self.driver.find_element_by_css_selector('#app > div > div.login-wrapper > form > div:nth-child(1) > div > div > input').send_keys("wanghui1155@100tal.com")#输入账号
        time.sleep(2)
        self.driver.find_element_by_css_selector('#app > div > div.login-wrapper > form > div:nth-child(2) > div > div > input').send_keys("izhikang7654321")#输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/button').click()#点击登录,此时出现提示输入验证码
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/form/button').click()#点击登录
        self.driver.implicitly_wait(8)
        self.driver.find_element_by_xpath("//p[contains(text(),'业务系统')]").click()#点击业务系统
        time.sleep(2)
        self.driver.refresh()
        time.sleep(3)
        actValue = self.driver.find_element_by_xpath('/html/body/div[1]/div/ul/div[2]/li[3]/span').text
        try:
            self.assertEqual(actValue,expValue)
        except Exception: \
            assert False, \
                "实际结果为:%s,预期结果为:%s" % (actValue, expValue)

        nowTime = time.strftime("%Y%m%d.%H.%M.%S")# 图片名称可以加个时间戳
        self.driver.get_screenshot_as_file('%s.jpg' % nowTime)


        # try:
        #     assert expValue == actValue
        #     print ('Assertion test pass.')
        # except Exception as e:
        #     print ('Assertion test fail.', format(e))
        #
        #             # 图片名称可以加个时间戳
        #     nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        #     self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
        #     raise

        # if self.driver.name == "chrome":
        #     js = "var q=document.body.scrollTop=1000"
        # else:
        #     js = "var q=document.documentElement.scrollTop=20000"

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()




















# #第一步从selenium导入webdriver模块
# from selenium import webdriver
# #导入time模块
# import time
# #第二步打开浏览器
# driver = webdriver.Firefox()
# #第三步打开浏览器如京东
# driver.get("https://www.jd.com/")
# #将浏览器窗口最大化
# driver.maximize_window()
# time.sleep(3)
    # expValue = u"京东超市"
# #获取当前的title
# actValue = driver.find_element_by_xpath(".//*[@id='navitems-group2']/li[2]/a").text
# print actValue
# try:
#     assert expValue == actValue
#     print ('Assertion test pass.')
# except Exception as e:
#     print ('Assertion test fail.', format(e))
# driver.quit()

#获取当前的url
# now_url=driver.current_url
# print(now_url)
#对url做判断
# if now_url=="http://poi.zuzuche.com/index-entrance-284ab515c664b25eb22fd29aaf3d553d.html?source=10000":
#     print("url ok")
# else:
#     print("url on")
# time.sleep(3)
# # driver.find_element_by_link_text("你好，请登录").click()
# time.sleep(3)
# driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]/div/div[2]/a").click()
# time.sleep(2)
# driver.find_element_by_xpath(".//*[@id='loginname']").send_keys("15190257357")
# driver.find_element_by_xpath(".//*[@id='nloginpwd']").send_keys("1314520trkf")
# driver.find_element_by_xpath(".//*[@id='loginsubmit']").click()
# actValue=driver.find_element_by_xpath("").text
# 获取弹框文本值
# actValue = driver.find_element_by_xpath(".//*[@id='nloginpwd']").text
# try:
#     driver.assertEqual(actValue,expValue)
# except Exception: \
#         assert False, \
#             "实际结果为:%s,预期结果为:%s" % (actValue, expValue)
# finally:
#         print ""

# time.sleep(2)
# driver.find_element_by_xpath(".//*[@id='content']/div[2]/div[1]/div/div[2]/a").click()
#
# driver.find_element_by_id("loginname").send_keys("15190257357")
# driver.find_element_by_name("nloginpwd").send_keys("1314520trkf")
# driver.find_element_by_class_name("btn-img btn-entry").click()

#用id定位
# driver.find_element_by_id("key").send_keys(u"家具")



        # js = "window.scrollTo(0,document.body.scrollHeight)"
        # dr.execute_script(js)
        # actValue = dr.find_element_by_xpath("html/body/div[1]/div/section[1]/h1").text
        # 断言
        # try:
        #     if actValue == expValue:
        #         print "ok"
        #     else:
        #         print "failed"
        # except Exception:\
        #     assert False,\
        #     "不一致"

# if __name__ == "__main__":
#     unittest.main()

#-*- coding:UTF-8 -*-

# import unittest,time
# from selenium import webdriver
# class Login(unittest.TestCase):
#     def setUp(self):
#         print u"初始化"
#         global dr
#         dr = webdriver.Firefox()
#         dr.maximize_window()
#         dr.get("https://www.jd.com/")
#         time.sleep(3)
#
#     def tearDown(self):
#         print u"结束清理"
#         time.sleep(2)
#         dr.quit()
#
#     def test001(self):
#         pass
        # dr.find_element_by_xpath(".//*[@id='newLeft']/div[3]/a/img").click()
        #
            #     all1 = dr.window_handles
            #     print u"获取所有句柄",all1
            #     for t1 in all1:
            #         if t1 != a:
            #             print u"第二次获取句柄",t1
            #             dr.switch_to_window(t1)
            #     time.sleep(2)
            #     dr.find_element_by_xpath(".//*[@id='classfied1']/ul/li/table/tbody/tr[1]/th/a").click()
            #
            #     all2 = dr.window_handles
            #     print u"获取所有句柄:",all2
            #     for t2 in all2:
            #         if t2 != t1 and t2 != a:
            #             print u"第三次获取句柄",t2
            #             dr.switch_to_window(t2)
            #     time.sleep(2)
            #     dr.find_element_by_xpath(".//*[@id='agree']/span/ins").click()
            #
            #     dr.find_element_by_id("sendSm").click()
            #     time.sleep(2)
            # 获取弹框文本值
