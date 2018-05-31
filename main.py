# coding=utf-8
'''
Created on 2017-11-20

'''
import unittest
import HTMLTestRunner_jpg
import HTMLTestRunner

from test_case import run
from test_case import run_v1
from test_case import run_v6
#构造测试集
suite = unittest.TestSuite()
# suite.addTest(run.Run('register'))#用户注册接口
# suite.addTest(run.Run('logout'))#退出登录
# suite.addTest(run.Run('user'))#用户信息
# suite.addTest(run.Run('forget_password'))#忘记密码
# suite.addTest(run.Run('setup_password'))#重置密码
# suite.addTest(run.Run('category'))#分类数据接口
# suite.addTest(run.Run('wishlist_addOrDel'))#添加删除收藏
# suite.addTest(run.Run('api_wishlist'))#我的收藏
# suite.addTest(run.Run('select_address'))#查询地址
# suite.addTest(run.Run('delete_address'))#删除地址
# suite.addTest(run.Run('update_address'))#更新地址
# suite.addTest(run.Run('insert_address'))#新增地址
# suite.addTest(run.Run('area_info'))#国家城市联级查询
# suite.addTest(run.Run('order_cancel'))#订单取消
# suite.addTest(run.Run('order_repurchase'))#订单回购
suite.addTest(run_v6.Run('productOptions'))#商品详情页_V6
suite.addTest(run_v6.Run('cart_add'))#商品详情页_V6
# suite.addTest(run_v1.Run('productOptions'))#订单回购

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    fr = open('report/res.html','wb')
    report = HTMLTestRunner_jpg.HTMLTestRunner(title="电商接口测试报告",
                                            description="测试用例参考",
                                            stream=fr)
                                            # retry=1)
    # report.run(suite)
    runner.run(suite)
