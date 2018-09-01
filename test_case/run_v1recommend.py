#_*_ coding:utf-8 _*_
'''
 7 / 6 / 2 / 5 / 17 / 15 / 9 / 16 / 3 / 10 / 11 / 14 / 12 / 13 / 36 / 37 / 1 / 8 / 4
__author__ = 'kefan'
'''

import unittest
import time
import requests
import json

class Run(unittest.TestCase):
    def setUp(self):
        self.url17 = "http://chaoshi.detail.tmall.com/item.htm?id=527119772754&spm=875.7931836/B.2017039.6.50495dbf0IVrA8&scm=1007.12144.81309.73136_0&pvid=c5769529-5cd6-44ab-a4b9-341f0403008a&skuId=3136449436481"
        #兴趣频道地址
        self.url = "http://47.91.65.163:17710/focus/search.do?appType=fbAndroid&version=1.3.92&devid=642333e153271743""&focusType=member&focusId=99999999&isNew=1&isNeed=1"
        #新闻编辑频道上拉刷新
        self.url2 = "http://47.91.93.147:17316/arabic/filter.do?appid=2&devid=642333e153271743&catgId=15&isNew=0&isNeed=0"
        #新闻编辑频道下拉刷新
        self.url3 = "http://47.91.93.147:17316/arabic/filter.do?appid=2&devid=642333e153271743&catgId=999&isNew=1&isNeed=0 "
        #新闻编辑频道强制刷新
        self.url4 = "http://47.91.93.147:17316/arabic/filter.do?appid=2&devid=642333e153271743&catgId=999&isNew=1&isNeed=1 "
        #足球关注球队上拉刷新
        self.url6 = "http://47.91.93.147:17710/focus/search.do?appType=fbAndroid&version=1.4.10&devid=642333e153271743&focusType=team&focusId=1&isNew=0&isNeed=0"
        #足球关注球队文章列表
        self.url5 = "http://47.91.93.147:17710/focus/search.do?appType=fbAndroid&version=1.4.10&devid=a23dffd4d0cf301e&focusType=team&focusId=57&isNew=0&isNeed=0"
        self.headers = {
            'Access-Token':'642333e153271743'
        }

    '''兴趣频道'''
    def Interest_recommendation(self):
        respone = requests.get(self.url17)
        print respone.content
        self.assertEqual(respone.status_code,200)
        self.assertNotEqual(json.loads(respone.content)['docs'],[])
        data = json.loads(respone.content)
        if data['docs'] ==None:
            print "has New is 0"
            exit(0)
        content=data['docs']
        has = []
        not_has=[]
        for item in content:
            title = item['title']
            id = item['id']
            if title.find(u"الأهلي")>0:
                has.append(id)
            else:
                url= "http://api.wekoora.com/ar_AE/api/article_details/"+id
                respone = requests.get(url,None,headers=self.headers)
                content = json.loads(respone.content)
                acticle = content['content']['content']
                if acticle.find(u"الأهلي")>0:
                    has.append(id)#把包含关键词的文章ID放到数组中
                else:
                    not_has.append(id)#把不包含关键词的文章ID放到数组中
        if len(not_has)>0:#如果not_has数组中有
            self.assertEqual(json.dumps(not_has),-1)#打印出id,json.dumps转化成字符串

    def Channel_article(self):
        times = 15  # 设置请求次数
        ids = []
        for i in range(0,times):
            respone = requests.get(self.url16)
            jsonText = json.loads(respone.text)
            print jsonText
            if "docs" in jsonText and len(jsonText["docs"]) > 0:
                for doc in jsonText["docs"]:
                    ids.append(doc["id"])
            time.sleep(2)  # 这里是延迟设置
        # 遍历整理
        idDict = {}
        for id in ids:
            if id in idDict.keys():
                idDict[id] += 1
            else:
                idDict[id] = 1
        # 字典根据value排序
        newIdDict = sorted(idDict.items(), key=lambda x: x[1], reverse=True)
        if len(newIdDict) == len(ids):
            print("此次%d次请求无重复" % times)
        else:
            print("请求有重复id，如下是详情\n")
            print(newIdDict)

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()



