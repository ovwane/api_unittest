# coding=utf-8
import unittest
# 这里需要导入测试文件
import Sim
import HTMLTestRunner
import sys
reload(sys)
import Share
sys.setdefaultencoding('utf-8')
'''构造测试集'''
suite = unittest.TestSuite()
suite.addTest(Sim.jingdong('test_001'))
suite.addTest(Share.Share('testcase001'))



if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()

    fr = open('res.html','wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
    # report.run(suite)


    runner.run(suite)













#  #coding:utf-8
# import HTMLTestRunner
# class CreatHTMLReport(object):
#     def HTMLReportDriver(self,fileName,revtitle,revdesc,revSuit):
#         fileHtmlName='../jikeTestReport/'+fileName
#         #w是写入的意思，b是二进制代表图片，图片是已二进制的形式写入
#         with open(fileHtmlName,'wb') as htmlStream:
#             #stream：文件流向，verbosity：冗长是生成报告的条数，title：标题，description：描述信息
#             HTMLTestRunner.HTMLTestRunner(
#                 stream=htmlStream,
#                 verbosity=2,
#                 title=revtitle,
#                 description=revdesc
#             ).run(revSuit)