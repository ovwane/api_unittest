# _*_ coding:utf-8 _*_

__author__ = 'chenhuan'

import ConfigParser
import json
import os
import sys
import unittest
import requests
from mfilter import *

reload(sys)
sys.setdefaultencoding("utf-8")


class Run(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser.ConfigParser()
        conf.read(os.path.abspath('.')+'/env.conf')
        self.conf = conf
        self.base_url = conf.get("env", "host")



    '''分类数据接口'''
    def category(self):

        response = requests.get(self.base_url+"/api/category")
        self.assertEqual(response.status_code, 200)

        data= json.loads(response.content)

        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])

        for item in data['data']:
             self.valid_item(item)

    def valid_item(self,item):
        filter = Mfilter(self)
        filter.run(item,{
            'category_id|int|require',
            'image|varchar|require',
            'children|array'
        })
        if 'children' in item and len(item['children']) > 0:
            for children in item['children']:
                self.valid_item(children)

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


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
