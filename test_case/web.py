# _*_ coding:utf-8 _*_
import requests
import os
import HtmlTestRunner
url="https://fir.im/"
r=requests.get(url)
print(r.text)