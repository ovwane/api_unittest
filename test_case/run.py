# _*_ coding:utf-8 _*_

__author__ = 'chenhuan'
import ConfigParser
import json
import os
import sys
import unittest
import requests
from mfilter import *
import random
import time

reload(sys)
sys.setdefaultencoding("utf-8")


class Run(unittest.TestCase):
    user_token = None

    def __get_user_token(self):

        if self.user_token == None:
            self.user_token = self.login()
        return self.user_token

    def setUp(self):
        conf = ConfigParser.ConfigParser()
        conf.read(os.path.abspath('.') + '/env.conf')
        self.conf = conf
        self.base_url = conf.get("env", "host")
        self.str = conf.get("app", "channel_id")
        self.user_random_str = time.strftime("%Y%m%d", time.localtime())

    '''用户注册接口'''

    def register(self):
        accout = self.str.split(',')
        postData = {}
        postData['lang'] = random.randint(1, 3)  # id 1：en 2:zh-cn 3:ar
        postData['channel_id'] = random.randint(1, 4)  # 请求渠道id 1：pc站，2：H5手机站，3：ios-app，4：android-app
        postData['email'] = self.user_random_str + "@s.e.com"
        postData['password'] = self.user_random_str
        postData['first_name'] = '1' + self.user_random_str
        postData['last_name'] = 'l' + self.user_random_str
        response = requests.post(self.base_url + '/api/register', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'],{
            'token|varchar|require',
            'user|object|require'

        })


    '''用户注册接口异常'''

    def register_case01(self):
        channel_id = self.str.split(',')  # str转数组
        postData = {}
        postData['lang'] = random.randint(1, 3)  # id 1：en 2:zh-cn 3:ar
        postData['channel_id'] = channel_id[random.randint(0, 4)]
        postData['email'] = self.user_random_str + '@simsim.onemena1.com'
        postData['password'] = self.user_random_str
        postData['first_name'] = 'f' + self.user_random_str
        postData['last_name'] = 'l' + self.user_random_str
        response = requests.post(self.base_url + '/api/register', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)


    '''登录认证'''
    def login(self):
        postData = {}
        postData['email'] = '15190257357@163.com'
        postData['password'] = '111111'
        response = requests.post(self.base_url + '/api/login', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.user_token = data['data']['token']
        filter = Mfilter(self)
        filter.run(data['data'], {
            'token|varchar|require',
            'user|object|require'
        })
        return self.user_token

    '''退出登录'''

    def logout(self):
        headers = {'Authorization': 'Bearer ' + self.__get_user_token()}
        response = requests.get(self.base_url + '/api/logout', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        filter = Mfilter(self)
        filter.run(data, {
            'data|object|require',
            'message|varchar|require'
        })



    '''用户信息'''
    def user(self):
        headers={}
        headers['Authorization']='Bearer'+ self.__get_user_token()
        response = requests.get(self.base_url + '/api/user/',headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        filter = Mfilter(self)
        filter.run(data, {
            'data|object|require',
            'message|varchar|require'
        })

    '''忘记密码'''
    def forget_password(self):
        postdata = {'email': '15190257357@163.com'}
        response = requests.post(self.base_url + '/api/forget_password', data=postdata)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'A new code has been sent to your email.')
        self.assertNotEqual(data['data']['email'], '')
        self.assertNotEqual(data['data']['customerId'], '')
        filter = Mfilter(self)
        filter.run(data, {
            'code|int|require',
            'data|object|require',
            'message|varchar|require'
        })
        filter.run(data['data'], {
            'customerId|int|require',
            'email|varchar|require'
        })

    '''验证验证码是否有效'''
    def verification_code_post(self):
        code = "493501"
        postData = {}
        postData['code'] = code
        postData['customer_id'] = 11
        response = requests.post(self.base_url + '/api/check_verification_code', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['data']['verificationCode'], '091002')
        self.assertEqual(data['data']['customerId'], '11')

    '''重置密码'''
    def setup_password(self):
        postData = {}
        postData['customer_id'] = '11'
        postData['password'] = '111111'
        postData['confirm_password'] = '111111'
        response = requests.post(self.base_url + '/api/setup_password', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['data'], {})
        filter = Mfilter(self)
        filter.run(data, {
            'code|int|require',
            'data|object|require',
            'message|varchar|require'
        })


    '''分类数据接口'''

    def category(self):
        response = requests.get(self.base_url + "/api/category")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])

        for item in data['data']:
            self.valid_item(item)
    def valid_item(self, item):
        filter = Mfilter(self)
        filter.run(item, {
            'category_id|int|require',
            'image|varchar|require',
            'name|varchar|require',
            'children|array'
        })
        if 'children' in item and len(item['children']) > 0:
            for children in item['children']:
                self.valid_item(children)

    '''分类商品数据'''
    def product_category(self):
        response = requests.get(self.base_url + "/api/product/category"+"?page=0&id=88")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])
        for item in data['data']:

            filter = Mfilter(self)
            filter.run(item, {
                'product_id|int|require',
                'name|varchar|require',
                'price|float|require',
                'image_cover|varchar|require',
                'image_cover_middle|varchar|require	',
                'special|float|require',
                'discount|int|require',
                'is_stock|Bool|require',
                'wish_quantity|int|require',
                'is_wish|bool|require',
                'currency_units|varchar|require'
            })

    '''商品'''
    def product(self):
        product_id = self.conf.get("app", "product_id")
        headers = {'Authorization': 'Bearer ' + self.__get_user_token()}
        response = requests.get(self.base_url + "/api/product", params={'id': product_id}, headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])

    '''首页数据接口'''
    def api(self):
        url='/api?lang=2&channel_id=2&currency_code=*'
        response = requests.get(self.base_url + url)
        self.assertEqual(response.status_code,200)
        data=json.loads(response.text)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'],'success')
        self.assertNotEqual(data['data'],{})
        filter = Mfilter(self)
        filter.run(data['data'],{
            'banner_info|object|require',
            'catagory_info|object|require'
        })

    '''商品详情'''
    def product(self):
        headers={}
        headers['Authorization']='Bearer'+self.__get_user_token()
        headers['device-code']='1fac37e853c6eb74'
        url='/api/product?id=145'
        response = requests.get(self.base_url+ url,headers=headers)
        self.assertEqual(response.status_code, 200)
        data=json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], "success")
        self.assertNotEqual(data['data'],[])
        filter = Mfilter(self)
        filter.run(data['data'],{
            'product_id|int|require',
            'special|float|require',
            'discount|int|require',
            'save_price|float ',
            'is_wish|Bool|require',
            'name|varchar|require',
            'image_cover|varchar|require',
            'image_cover_max|varchar|require',
            'images|array|require',
            'images_max|array|require',
            'price|float |require',
            'is_stock|Bool|require',
            'descrption|varchar',
            'attributes|array',
            'discount|int'



        })


    '''添加购物车'''
    def cart_add(self):
        headers={}
        headers['Authorization']='Bearer'+self.__get_user_token()
        url='/api/cart/add?product_id=145'
        response = requests.get(self.base_url+url, headers=headers)
        data= json.loads(response.text)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'],[])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'

        })



    '''更新购物车'''
    def cart_upcart(self):
        headers={}
        headers['Authorization']='Bearer'+self.__get_user_token()
        url= '/api/cart/upcart?product_id=145'
        response = requests.get(self.base_url+url,headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'],'success')
        self.assertNotEqual(data['data'],[])
        filter= Mfilter(self)
        filter.run(data['data'],{
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'

        })

    '''删除购物车'''
    def cart_delcart(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/delcart?product_id=145'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        self.assertEqual(data['data']['totalPrice'],0)
        self.assertEqual(data['data']['quantity'], 0)
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|int|require',
            'quantity|int|require',
            'currency_units|varchar|require'
        })


    '''購物車詳細接口'''
    def cart_getCart(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/getCart'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'cartList|array|require',
            'anomalyCartList|array|require',
            'recommendSalesList|array|require',
            'cartTotal|object|require'
        })


    '''獲取購物車總計信息'''
    def cart_getCartTotal(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/getCartTotal'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'
        })

    '''更新購物車IOS'''
    def cart_upCartIos(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/upCartIos?product_id=145'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'cartInfo|object|require',
            'cartTotal|object|require'
        })
        filter.run(data['data']['cartTotal'], {
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'
        })






    def tearDown(self):
        pass




if __name__ == "__main__":
    unittest.main()
