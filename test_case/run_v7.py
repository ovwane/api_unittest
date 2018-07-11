# coding=utf-8

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


class Run(unittest.TestCase):
    user_token = None

    def __get_user_token(self):
        if self.user_token == None:
            self.user_token = self.login()
        return self.user_token

    def setUp(self):
        conf = ConfigParser.ConfigParser()
        conf.read(os.path.abspath('.')+'/env.conf')
        self.conf=conf
        self.base_url = conf.get('env','momshop')

    def login(self):
        u'''登录认证'''
        headers = {}
        headers['device-code'] = '642333e153271743'
        postData = {}
        postData['email'] = 'tester@2.com'
        postData['password'] = '123456'
        response = requests.post(self.base_url + '/api/login',headers=headers,data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)#字符串转成dict
        # j = json.dumps(data,ensure_ascii=False,indent=4)#json.dumps()用于将dict类型的数据转成str
        # print j
        self.assertEqual(data['code'], 0)
        self.user_token = data['data']['token']
        filter = Mfilter(self)
        filter.run(data['data'], {
            'token|varchar|require',
            'user|object|require'
        })

        return self.user_token



    def productOptions(self):
        u'''商品详情_V7'''
        headers={}
        headers['lang']="1"
        headers['currencycode'] ='USD'
        headers['Api-Version'] ='application/vnd.momshop.v7+json'
        headers['device-code'] = '642333e153271743'
        headers['Authorization'] = self.__get_user_token()
        url = '/api/product?id=4034'
        response=requests.get(self.base_url+url,headers=headers,timeout=4)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['data']['product_id'],4034)
        self.assertEqual(data['data']['properties'][0]['showType'], "image")
        value = json.dumps(data['data']['productOptions'], ensure_ascii=False, indent=4)  # json.dumps()用于将dict类型的数据转成str
        # print value
        filter = Mfilter(self)
        filter.run(data['data'], {
            'name|varchar|require',
            'image_cover|varchar|require',
            'image_cover_max|varchar|require',
            'images|array|require',
            'images_max|array|require',
            'price|float|require',
            'special|float|require',
            'is_wish|bool|require',
            'desciption|varchar|require',
            'attributes|array|require',
            'discount|int|require',
            'isOffSale|bool|require',
            'save_price|float|require',
            'rating|float|require',
            'serverGuarantee|array|require',
            'currency_units|varchar|require',
            'activity_tip|varchar|require',
            'cartQuantity|int|require',
            'isGift|int|require',
            'flag|int',
            'flashSale|array',
            'productOptions|array|require',
            'maxPrice|float|require',
            'freightPrice|float|require',
            'sales_quantity|int',
            'nameTag|array|require',
            'properties|array|require'
    })
        for item in data['data']['properties']:
            filter.run(item, {
                'propertyName|varchar|require',
                'showType|varchar|require',
                'values|array|require',
                'propertyId|int|require'
                })
            for item in data['data']['properties'][0]['values']:
                filter.run(item, {
                    'image|varchar|require',
                    'valueId|int|require',
                    'selected|bool|require',
                    'valueName|varchar|require'
                })
        for item in data['data']['productOptions']:
            filter.run(item, {
                'productOptionId|int|require',
                'name|varchar|require',
                'price|float|require',
                'discount|int|require',
                'imageMax|varchar|require',
                'props|object|require',
                'image|varchar|require'
            })


    def productOptionDetail(self):
        u'''规格详情_V7'''
        headers = {}
        headers['lang'] = "1"
        headers['currencycode'] = 'USD'
        headers['Api-Version'] = 'application/vnd.momshop.v7+json'
        headers['device-code'] = '111111'
        headers['Authorization'] = self.__get_user_token()
        url = '/api/product?id=4034'
        response = requests.get(self.base_url + url, headers=headers, timeout=4)
        data = json.loads(response.content)
    #     for item in data['data']['properties']:
    #         values = item['values']
    #         for value in values:
    #             filter.run(value, {
    #                     'valueId|int|require',
    #                     'valueName|varchar|require',
    #                     'selected|bool|require'
    #             })