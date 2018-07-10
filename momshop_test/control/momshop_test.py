# -*- coding:utf-8 -*-


from selenium import webdriver
import time
from kefan_web.Get_setup import Get_setup
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class momshop_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        pass

    def setUp(self):
        # self.momshoptest.openH5()
        pass
    def tearDown(self):
        # self.momshoptest.closeH5()
        pass

    def test_ChekHome_1(self):
        # self.momshoptest.checkcontrol()
        pass


if __name__ =="__main__":
    unittest.main()