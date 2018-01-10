# coding:utf-8

"""
python接口自动化1-发送get请求
"""

import requests
# # 请求博客首页
# # 这里的r也就是response，请求后的返回值，可以调用response里的status_code方法查看状态码
# r = requests.get('http://www.cnblogs.com/yoyoketang/')
# print r.status_code        #响应状态码
# print r.raise_for_status() #失败请求(非200响应)抛出异常
# print r.text               #返回文本信息
# print r.url                # 获取url
# print r.encoding           #编码
# print r.content            #返回获取内容gzip 和 deflate 压缩
# print r.headers            #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# print r.cookies            # 获取cookie
#
# #params     发一个带参数的get请求
# par = {"Keywords":"yoyoketang"}
# r = requests.get('http://zzk.cnblogs.com/s/blogpost',params=par)
#
# print r.status_code
# print r.text

#发送一个post请求
payload = {"yoyo":"helloworld",
            "pythonQQ群":"226296473"}
r = requests.post('http://httpbin.org/post',form=payload)
print (r.text)
print r.raise_for_status()