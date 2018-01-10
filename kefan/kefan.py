# coding=utf-8
from appium import webdriver
import time
import json
import requests
import ConfigParser
#定义启动设备需要参数
desired_caps = {}
#设备系统
desired_caps['platformName'] = 'Android'
#设备系统版本
desired_caps['platformVersion'] = '5.0.1'
#设备为模拟器
desired_caps['deviceName'] = 'Android Emulator'
#应用包名
desired_caps['appActivity'] = 'com.shanggame.tfsgz.official.MainActivity'
desired_caps['appPackage'] = 'com.shanggame.tfsgz.official'
#启动APP
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(4)

# driver.swipe(500,200,500,1000, 1000)
# for i in range(0, 3):
#     # 向下刷新3次
#     driver.swipe(500,200,500,1000, 1000)
#     time.sleep(3)
#

# #通过name方法定位
# driver.find_element_by_name("محمد صلاح يتحدى هارى كين فى قمة ليفربول وتوتنهام اليوم .. من ينتصر فى التحدى؟").click()
# time.sleep(2)


# def all_class(driver,element,number=0):
#     el = driver.find_elements_by_class_name(element).pop(number)
#     return el
#
# all_class(driver,"android.widget.RelativeLayout",3).click()
# # time.sleep(3)
#
# driver.background_app("com.wekoora.football")


