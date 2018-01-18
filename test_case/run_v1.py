
#_*_ coding:utf-8 _*_
'''
__author__ = 'kefan_app'
'''

import unittest
import sys
import requests
import ConfigParser
import os
import json
import hashlib
import random

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
        }

    '''金币任务'''
    def send_task(self):

        headers = {
            'Access-Token':str(random.randrange(1,99999999)),
            'User-Token':self.conf.get('app','user_token')
        }
        event='look_video'
        secret =event+self.app_name
        secret = hashlib.md5(secret).hexdigest()
        secret = hashlib.md5(secret).hexdigest()
        data ={'event':event,'secret':secret}
        response = requests.post(self.base_url+"/ar_AE/api/send_task",None,json=data,headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertEqual(json.loads(response.content)['extra']['alert_message'], "")



    '''视频列表'''
    def video_list(self):
        category_id = self.conf.get('app','test_video_category_id')
        response = requests.get(self.base_url+"/ar_AE/api/video_list_v2/"+category_id+"/0" ,headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertNotEqual(json.loads(response.content)['content'], [])


    '''相关文章'''
    def relation_article(self):
        test_id = self.conf.get('app','test_id')
        response = requests.get(self.base_url+"/ar_AE/api/relation_article/"+test_id ,headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertNotEqual(json.loads(response.content)['content'], [])

    '''文章状态'''
    def article_status(self):
        test_id = self.conf.get('app','test_id')
        response = requests.get(self.base_url+"/ar_AE/api/article_status/"+test_id ,headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertNotEqual(json.loads(response.content)['content'], [])


    ''' 消息列表'''
    def messageGet(self):
        response = requests.get(self.base_url+"/ar_AE/api/message/get?channel=comment_reply&offset=0" ,headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)

    ''' 我的评论'''
    def user_comments(self):
        response = requests.get(self.base_url+"/ar_AE/api/user_comments/0" ,headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)

    '''添加广告wekoora'''
    def ad_start(self):
        response = requests.get(" http://help.test.mysada.com/api/ad_start/get/wekoora",headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertNotEqual(json.loads(response.content)['data'],[])

    '''添加广告anawin'''
    def ad_start(self):
        response = requests.get(" http://help.test.mysada.com/api/ad_start/get/anawin",headers = self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertNotEqual(json.loads(response.content)['data'],[])

    '''获取文字直播内容(有内容)'''
    def get_livetext(self):
        response = requests.get(self.base_url+"/ar_AE/api/get_live_game_texts?live_game_id=253",headers = self.headers)
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content)['code'],1)
        self.assertEqual(json.loads(response.content)['message'], "success")
        self.assertNotEqual(json.loads(response.content)['content']['liveGameTextDatas'],[])

    '''设置firbase_token接口'''
    def firbase_token(self):
        headers = {
            'Access-Token': '642333e153271743',
            # 'User-Token':self.conf.get('app','user_token'),
            'app_version': '1.3.92',
            'plate_form': 'Android',
            'fb_token': 'enhMD5hvJVI:APA91bGWIev6Wy5EEB9MfCLUCt - d4o_CcYr8ascIehmuUza31pECKNEXgt_MX3zI0HXsOXYeKytmd_g8kgs - QFpa39p2srbcB5UwnwzGKlYT9Tiw1i3NzqwzrsBzWMgbr0A9neiU3WeM'
        }
        response = requests.post(self.base_url+"/ar_AE/api/set_fb_token",headers = headers)
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content)['code'],1)
        self.assertNotEqual(json.loads(response.content)['content'],"")
        self.assertEqual(json.loads(response.content)['message'],"success")

    '''获取设置接口'''
    def setting_get(self):
        response = requests.get(self.base_url + "/ar_AE/api/get_live_game_texts?live_game_id=226", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['code'], 1)
        self.assertEqual(json.loads(response.content)['message'], "success")
        self.assertNotEqual(json.loads(response.content)['content']['liveGameTextDatas'], [])

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
