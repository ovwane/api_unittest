print('\n'.join([''.join([('AndyLove'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
# #coding:utf-8
# from selenium import webdriver
# import time
# import unittest
# class jingdong(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Firefox()
#         self.url = "http://www.test.arabsada.com/login/"
#         self.driver.maximize_window()
#         time.sleep(2)
#
#     def test_001(self):
#         '''新闻测试后台'''
#         expValue = 'a'
#         driver=self.driver#火狐驱动
#         driver.get(self.url)#打开链接
#         driver.find_element_by_xpath(".//*[@id='email']").send_keys("admin@admin.com")#输入用户名
#         driver.find_element_by_xpath(".//*[@id='password']").send_keys("1234")#输入密码
#         driver.find_element_by_xpath(".//*[@id='app']/div/div/div/div[2]/form/div[4]/div/input").click()#点击登录
#         time.sleep(3)
#         actValue = driver.title
#
#         try:
#             self.assertEqual(expValue,actValue)
#         except AssertionError as e:
#             print "fail"
#         if self.driver.name == "chrome":
#             js = "var q=document.body.scrollTop=1000"
#         else:
#             js = "var q=document.documentElement.scrollTop=20000"
#
#         time.sleep(10)
#
#
#     def tearDown(self):
#         self.driver.quit()
# if __name__ == "__main__":
#     unittest.main()
#
#



















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
