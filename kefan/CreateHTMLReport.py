#生成HTML格式的测试报告
#coding:utf-8；【】、
import sys,os
sys.path.append(os.getcwd())
import HTMLTestRunner# 需在库中放一个HTML TestRunner.py文件后方可调用
class CreateHTMLReport(object):
    def HtMLReportDriver(self,fileName,revtitle,revdescription,revSuite):
        #fileHtmlName='../Report/'+fileName # 想生成测试报告得用一个文件，地址不能写死，为了方便读地址
        fileHtmlName ='/Users/shixin/zuobiao/Report/'+fileName
        #打开html文件,b代表图片以二进制的方式写入,as 后面可以自定义一个变量作为标识，该变量在内存空间中是为了运行效率更高
        with open(fileHtmlName,'wb') as a:
            # 括号是后加的，括号提示信息：stream是指文本流：告诉文件流向哪里，verboisity是指冗长取值为1/2,
            #1是指无论执行多少条case都只返回一条提示信息没有详细的测试信息，2是指会给出详细的测试信息
            #title是标题，不能写死，谁用谁调用
            #descri是描述信息
            HTMLTestRunner.HTMLTestRunner(
            stream=a,
            verbosity=2,
            title=revtitle,
            description=revdescription
            ).run(revSuite) # 跑单条就就填谁，跑多条就用测试套想测试哪些模块就封装谁成套