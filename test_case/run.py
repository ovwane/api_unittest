# _*_ coding:utf-8 _*_

__author__ = 'chenhuan'

import unittest
import sys
import requests
import ConfigParser
import os
import json
import types
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
        parent_id = self.conf.get('app','parent_id')
        response = requests.get(self.base_url+"/api/category")
        self.assertEqual(response.status_code, 200)

        data= json.loads(response.content)

        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])

        for item in data['data']:

            if 'category_id' not in item:
                self.assertEqual('category_id',-1,'category_id require')

            if 'name' not in item:
                self.assertEqual('name', -1, 'name require')

            if 'image' not in item:
                self.assertEqual('image', -1, 'image require')

            if 'children' not in item:
                self.assertEqual('children', -1, 'children require')



            if type(item['category_id'])!=type(1):
                self.assertEqual('category_id', -1,'category_id require int')

            if type(item['children'])!=type([]):
                self.assertEqual('children', [],'children require array')

            break


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
