# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:编写Web测试用例
'''
import unittest,requests,HTMLTestRunner

from test_case import run



#构造测试集
suite = unittest.TestSuite()
suite.addTest(run.Run('category'))



if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    fr = open('res.html','wb')
    #report = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
    #report.run(suite)


    runner.run(suite)