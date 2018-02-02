# coding=utf-8
'''
Created on 2017-11-20

'''
import unittest,HTMLTestRunner

from test_case import run



#构造测试集
suite = unittest.TestSuite()
suite.addTest(run.Run('register'))
suite.addTest(run.Run('login'))
suite.addTest(run.Run('logout'))
suite.addTest(run.Run('user'))
suite.addTest(run.Run('forget_password'))
suite.addTest(run.Run('setup_password'))
suite.addTest(run.Run('category'))
suite.addTest(run.Run('product'))
suite.addTest(run.Run('product_category'))
suite.addTest(run.Run('api'))
suite.addTest(run.Run('cart_add'))
suite.addTest(run.Run('cart_upcart'))
suite.addTest(run.Run('cart_delcart'))
suite.addTest(run.Run('cart_null'))
suite.addTest(run.Run('cart_add'))
suite.addTest(run.Run('cart_getCart'))
suite.addTest(run.Run('cart_getCartTotal'))
suite.addTest(run.Run('cart_upCartIos'))
suite.addTest(run.Run('wishlist_addOrDel'))
suite.addTest(run.Run('api_wishlist'))
suite.addTest(run.Run('select_address'))
suite.addTest(run.Run('delete_address'))
suite.addTest(run.Run('update_address'))
suite.addTest(run.Run('insert_address'))
suite.addTest(run.Run('area_info'))
suite.addTest(run.Run('coupon_verify'))
suite.addTest(run.Run('Cart_coupon_verify'))
suite.addTest(run.Run('api_checkout'))
suite.addTest(run.Run('api_immediatebuy'))
suite.addTest(run.Run('order_store'))
suite.addTest(run.Run('immediateBuy'))
suite.addTest(run.Run('order_list'))
suite.addTest(run.Run('order_list_status'))
suite.addTest(run.Run('order_detail01'))
suite.addTest(run.Run('order_detail02'))
suite.addTest(run.Run('order_cancel'))
suite.addTest(run.Run('order_repurchase'))
suite.addTest(run.Run('order_store'))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    fr = open('res.html','wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
    # report.run(suite)


    runner.run(suite)