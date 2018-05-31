# _*_ coding:utf-8 _*_

import ConfigParser
import json
import os
import sys
import unittest
import requests
from mfilter import *
import random
import time
import urllib2
reload(sys)
sys.setdefaultencoding("utf-8")

user_token = None
def __get_user_token(self):
    if self.user_token == None:
        self.user_token = self.login()
    return self.user_token
class Run(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser.ConfigParser()
        conf.read(os.path.abspath('.')+'/env.conf')
        self.conf=conf
        self.base_url = conf.get('env','momshop')

    def login(self):
        u'''登录认证'''
        postData = {}
        postData['email'] = 'wukefan@20.com'
        postData['password'] = '123456'
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



    def productOptions(self):
        u'''商品详情_V6'''
        headers={}
        headers['lang']="1"
        headers['currencycode'] ='USD'
        headers['Api-Version'] ='application/vnd.momshop.v6+json'
        headers['device-code'] = '111111'
        url = '/api/product?id=898'
        response=requests.get(self.base_url+url,headers=headers,timeout=4)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['data']['product_id'],898)
        filter = Mfilter(self)
        filter.run(data['data'], {
            'cartQuantity|int|require',
            'attributes|array|require',
            'activity_tip|varchar|require',
            'isGift|int|require',
            'serverGuarantee|array|require',
            'product_id|int|require',
            'discount|int|require',
            'is_wish|bool|require',
            'images_max|array|require',
            'images|array|require',
            'quantity|int|require',
            'name|varchar|require',
            'nameTag|array|require',
            'properties|array|require'
    })
        for item in data['data']['properties']:
            filter = Mfilter(self)
            filter.run(item, {
                'propertyId|int|require',
                'propertyName|varchar|require',
                'values|array|require'
        })
        for item in data['data']['properties']:
            values = item['values']
            for value in values:
                filter.run(value, {
                        'valueId|int|require',
                        'valueName|varchar|require',
                        'selected|bool|require'
                })



    def cart_add(self):
        u'''添加购物车_V2'''
        headers={}
        headers['lang']="1"
        headers['currencycode'] ='USD'
        headers['Api-Version'] ='application/vnd.momshop.v2+json'
        headers['device-code'] = '111111'
        url = '/api/cart/add?product_id=898&product_option_id=1006'
        response=requests.get(self.base_url+url,headers=headers,timeout=4)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'],'success')
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|floot|require',
            'quantity|int|require',
            'currency_units|varchar|require'
    })


    def cart_add(self):
        u'''购物车总计_V3'''
        headers={}
        headers['lang']="1"
        headers['currencycode'] ='USD'
        headers['Api-Version'] ='application/vnd.aliamall.v3+json'
        headers['device-code'] = '111111'
        url = '/api/cart/getCartTotal'
        response=requests.get(self.base_url+url,headers=headers,timeout=4)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'],'success')
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|floot|require',
            'quantity|int|require',
            'currency_units|varchar|require'
    })
