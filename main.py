# coding=utf-8
'''
Created on 2017-11-20

'''
import unittest,HTMLTestRunner

from test_case import run

#构造测试集
suite = unittest.TestSuite()
suite.addTest(run.Run('register'))#用户注册接口
# suite.addTest(run.Run('logout'))#退出登录
# suite.addTest(run.Run('user'))#用户信息
# suite.addTest(run.Run('forget_password'))#忘记密码
# suite.addTest(run.Run('setup_password'))#重置密码
# suite.addTest(run.Run('category'))#分类数据接口
# suite.addTest(run.Run('product'))#商品
# suite.addTest(run.Run('product_category'))#分类商品数据
# suite.addTest(run.Run('api'))#首页
# suite.addTest(run.Run('cart_add'))#添加购物车
# suite.addTest(run.Run('cart_upcart'))#更新购物车
# suite.addTest(run.Run('Cart_coupon_verify'))#购物车验证优惠码接口
# suite.addTest(run.Run('cart_delcart'))#删除购物车
# suite.addTest(run.Run('cart_null'))#购物车为空时删除购物车
# suite.addTest(run.Run('cart_add'))#添加购物车
# suite.addTest(run.Run('cart_getCart'))#购物车详细页
# suite.addTest(run.Run('cart_getCartTotal'))#获取购物车总计信息
# suite.addTest(run.Run('cart_upCartIos'))#更新购物车IOS
# suite.addTest(run.Run('wishlist_addOrDel'))#添加删除收藏
# suite.addTest(run.Run('api_wishlist'))#我的收藏
# suite.addTest(run.Run('select_address'))#查询地址
# suite.addTest(run.Run('delete_address'))#删除地址
# suite.addTest(run.Run('update_address'))#更新地址
# suite.addTest(run.Run('insert_address'))#新增地址
# suite.addTest(run.Run('area_info'))#国家城市联级查询
# suite.addTest(run.Run('coupon_verify'))#立即购买--验证优惠码接口
# suite.addTest(run.Run('api_checkout'))#购物车确认订单
# suite.addTest(run.Run('api_immediatebuy'))#立即购买--确认订单
# suite.addTest(run.Run('immediateBuy'))#立即购买--提交订单
# suite.addTest(run.Run('order_list'))#(post)用户中心-订单列表查询多条
# suite.addTest(run.Run('order_list_status_1'))#(get)用户中心-订单列表查询单条状态1
# suite.addTest(run.Run('order_detail01'))#(get)用户中心-订单详情
# suite.addTest(run.Run('order_detail02'))#(post)用户中心-订单详情
# suite.addTest(run.Run('order_cancel'))#订单取消
# suite.addTest(run.Run('order_repurchase'))#订单回购
# suite.addTest(run.Run('order_store'))#提交订单


if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    fr = open('report/res.html','wb')
    report = HTMLTestRunner.HTMLTestRunner(stream=fr,title='测试报告',description='测试报告详情')
    # report.run(suite)
    runner.run(suite)
