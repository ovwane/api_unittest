# coding=utf-8
from appium import webdriver
from Share import Share
import time,unittest
class Football(unittest.TestCase):
    def setUp(self):
        self.driver=Share().driver
        time.sleep(8)
    # def tearDown(self):
    #     print u"结束清理"
    #     driver.quit()
    #     time.sleep(2)
    def test001(self):
        Share().test001()

if __name__ == "__main__":
    unittest.main()

