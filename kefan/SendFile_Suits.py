#coding:utf-8
#封装测试套
import unittest
from Utills.CreateHTMLReport import CreateHTMLReport
class SendFile_Suits(unittest.TestCase):
    from zuobiaoCase.SendFile import SendFile

    #放在class下面，不然会执行完001，最后一条case又会重新执行一遍


#声明一个测试套
    SendFile_Suits=unittest.TestSuite()
    __fileName="发送文件.html" #生成一个.html的测试报告文件，文件名自定义
    __title="发送文件测试报告"
    __description=" case1：发送文件"
# #第一种方法，推荐多条case用：
    #添加用例到测试套，相当于类的实例化

    SendFile_Suits.addTest(SendFile('test_SendFile'))
    #loginSuit.addTest(LoginModule('testlogin002'))
#     #执行测试
    #unittest.TextTestRunner().run(loginSuit)
    #一定不要忘了（）
    CreateHTMLReport().HtMLReportDriver(__fileName,__title,__description,SendFile_Suits)
if __name__=="__main__":
    unittest.main()


