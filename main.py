# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest,requests,HTMLTestRunner
import time

from test_case import run_v1
from test_case import run_v2
from test_case import run_v3
from test_case import run_v4
from kefan_app import mom_login
from kefan_app import mom_register
#构造测试集
suite = unittest.TestSuite()
# suite.addTest(run_v1.Run('relation_article'))
# suite.addTest(run_v1.Run('article_status'))
# suite.addTest(run_v1.Run('messageGet'))
# suite.addTest(run_v1.Run('user_comments'))
# suite.addTest(run_v1.Run('video_list'))
#
# suite.addTest(run_v2.Run('user_info'))
# suite.addTest(run_v2.Run('set_category_categories'))
#
# suite.addTest(run_v3.Run('recommend'))
# suite.addTest(run_v3.Run('video_list'))
# suite.addTest(run_v3.Run('article_details'))
# suite.addTest(run_v4.Run('article_list'))
# suite.addTest(run_v4.Run('video_list'))
# suite.addTest(run_v4.Run('article_categories'))
# suite.addTest(run_v4.Run('video_categories'))
suite.addTest(mom_register.RegisterTest('test_register'))
# suite.addTest(mom_login.LoginTest('test_login'))


if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    timestr = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    fr = open('res.html','wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fr,title='Momshop_APP测试报告',description='测试报告详情')
    # report.run(suite)
    runner.run(suite)

    fr.close()