# _*_ coding:utf-8 _*_

__author__ = 'chenhuan'

import unittest
import sys
import requests
import ConfigParser
import os
import json
reload(sys)
sys.setdefaultencoding("utf-8")


class Run(unittest.TestCase):
    def setUp(self):
        conf = ConfigParser.ConfigParser()
        conf.read(os.path.abspath('.')+'/env.conf')
        self.conf = conf
        self.base_url = conf.get("env", "host")
        self.app_name = conf.get("env", "app_name")
        self.device_id = conf.get("app", "user_device_id")

        self.headers = {
            'Access-Token':self.device_id,
            'Accept': 'application/vnd.' + self.app_name + '.v2+json'

        }


    '''用户信息'''
    def user_info(self):
        response = requests.get(self.base_url+"/ar_AE/api/user_info" ,headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertNotEqual(json.loads(response.content)['content'], [])



    '''自定义频道'''
    def set_category_categories(self):

        data = {
            "add":[1,2,4],
            "not": [7, 8, 9]
        }

        response = requests.post(self.base_url + "/ar_AE/api/article_categories",json=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertNotEqual(json.loads(response.content)['content'], [])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
