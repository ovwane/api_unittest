# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest
from test_case import run_v1
from test_case import run_v2
from test_case import run_v3
from test_case import run_v4


#构造测试集
suite = unittest.TestSuite()
suite.addTest(run_v1.Run('relation_article'))
suite.addTest(run_v1.Run('article_status'))
suite.addTest(run_v1.Run('messageGet'))
suite.addTest(run_v1.Run('user_comment'))
suite.addTest(run_v1.Run('video_list'))



suite.addTest(run_v2.Run('user_info'))
suite.addTest(run_v2.Run('article_categories'))
suite.addTest(run_v2.Run('video_categories'))
suite.addTest(run_v2.Run('set_category_categories'))

suite.addTest(run_v3.Run('recommend'))
suite.addTest(run_v3.Run('article_list'))
suite.addTest(run_v3.Run('video_list'))
suite.addTest(run_v3.Run('article_details'))
suite.addTest(run_v3.Run('top'))


suite.addTest(run_v4.Run('article_list'))
suite.addTest(run_v4.Run('video_list'))


if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)