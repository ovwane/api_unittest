# coding=utf-8
import HTMLTestRunner
from appium import webdriver
from Share import Share
import time,unittest
class New(unittest.TestCase):
    def setUp(self):
        self.driver=Share().driver
    def tearDown(self):
        print u"结束清理"
        self.driver.quit()
        time.sleep(2)

    # 【新闻】关注用例从点击关注到查看关注列表
    # def test001(self):
    #     Share().testcase01()
    # def test002(self):
    #     pass

if __name__ == "__main__":
    unittest.main()

    # testunit = unittest.TestSuite()
    # testunit.addTest(unittest.makeSuite(Share.testcase01()))  # 将测试用例加入到测试容器中
    # timestr = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    # filename = '/F:/test/Test-ZQ/report/' +timestr+ '.html'  # 这个路径改成自己的目录路径
    # fp = file(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title',
    #                                        description='Report_description')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    # runner.run(testunit)  # 自动进行测试
    # fp.close()
