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
        postData = {}
        postData['lang'] = random.randint(1, 3)  # id 1：en 2:zh-cn 3:ar
        postData['channel_id'] = random.randint(1, 4)  # 请求渠道id 1：pc站，2：H5手机站，3：ios-app，4：android-app
        postData['email'] = self.user_random_str + '@simsim.onemena.com'
        postData['password'] = self.user_random_str
        postData['first_name'] = 'f' + self.user_random_str
        postData['last_name'] = 'l' + self.user_random_str
        response = requests.post(self.base_url + '/api/register', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])

    '''用户注册接口异常'''

    def register_case01(self):
        channel_id = self.str.split(',')  # str转数组
        print channel_id[random.randint(0, 3)]
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
        postData['email'] = self.user_random_str + '@simsim.onemena.com'
        postData['password'] = self.user_random_str
        response = requests.post(self.base_url + '/api/login', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)

        self.assertEqual(data['code'], 0)
        self.user_token = data['data']['token']

        return self.user_token

    '''退出登录'''

    def logout(self):
        headers = {'Authorization': 'Bearer ' + self.__get_user_token()}
        response = requests.get(self.base_url + '/api/logout', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')

    '''用户信息'''

    def user(self):
        response = requests.get(self.base_url + '/api/user?token=' + self.__get_user_token())
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)

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

    '''验证验证码是否有效'''

    def verification_code_post(self):
        code = "091002"
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
        postData['password'] = '123456'
        postData['confirm_password'] = '123456'
        response = requests.post(self.base_url + '/api/setup_password', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['data'], {})

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
            'children|array'
        })
        if 'children' in item and len(item['children']) > 0:
            for children in item['children']:
                self.valid_item(children)

    '''分类商品数据'''

    def product_category(self):
        response = requests.get(self.base_url + "/api/product/category")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])
        for item in data['data']:
            filter = Mfilter(self)
            filter.run(item, {
                'name|varchar|require',
                'price|float|require',
                'image_cover|varchar|require',
                'image_cover_middle|varchar|require	',
                'special|float',
                'discount|int',
                'is_wish|int|require',
                'is_stock|int|require',
                'wish_quantity|int|require'
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
        headers = {}
        headers['lang'] = ''
        headers['channel_id'] = ''
        headers['currency_code'] = '%&^$^sanb'
        # response = requests.get(self.base_url + "/api", headers=headers)
        # check(self, response)

        data = request(self, "get", self.base_url + "/api", headers=headers)

    def tearDown(self):
        pass


def request(self, method, url, **kwargs):
    response = requests.request(method, url, **kwargs)
    return check(self, response)


def check(self, response):
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.text)
    self.assertEqual(data['code'], 0)
    self.assertEqual(data['message'], 'success')
    return data


if __name__ == "__main__":
    unittest.main()
