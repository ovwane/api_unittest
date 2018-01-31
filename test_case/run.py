# _*_ coding:utf-8 _*_

__author__ = 'chenhuan'
import ConfigParser
import json
import os
import sys
import unittest
import requests
from mfilter import *
import random
import time


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
        conf.read(os.path.abspath('.') + '/env.conf')
        self.conf = conf
        self.base_url = conf.get("env", "host")
        self.str = conf.get("app", "channel_id")
        self.str =conf.get("app","email")
        self.user_random_str = time.strftime("%Y%m%d", time.localtime())

    '''用户注册接口'''

    def register(self):
        postData = {}
        postData['lang'] = random.randint(1, 3)  # id 1：en 2:zh-cn 3:ar
        postData['channel_id'] = random.randint(1, 4)  # 请求渠道id 1：pc站，2：H5手机站，3：ios-app，4：android-app
        postData['email'] = self.user_random_str +'kefan@sim.com'
        postData['password'] = self.user_random_str
        postData['first_name'] = '1' + self.user_random_str
        postData['last_name'] = 'l' + self.user_random_str
        response = requests.post(self.base_url + '/api/register', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'],{
            'token|varchar|require',
            'user|object|require'
        })


    '''用户注册接口异常'''
    def register_case01(self):
        channel_id = self.str.split(',')  # str转数组
        postData = {}
        postData['lang'] = random.randint(1, 3)  # id 1：en 2:zh-cn 3:ar
        postData['channel_id'] = channel_id[random.randint(0, 4)]
        postData['email'] = self.user_random_str + '@simsim.onemena1.com'
        postData['password'] = self.user_random_str
        postData['first_name'] = 'f' + self.user_random_str
        postData['last_name'] = 'l' + self.user_random_str
        response = requests.post(self.base_url + '/api/register', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)


    '''登录认证'''
    def login(self):
        postData = {}
        postData['email'] = '15190257357@163.com'
        postData['password'] = '000000'
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

    '''退出登录'''
    def logout(self):
        headers = {'Authorization': 'Bearer ' + self.__get_user_token()}
        response = requests.get(self.base_url + '/api/logout', headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        filter = Mfilter(self)
        filter.run(data, {
            'data|object|require',
            'message|varchar|require'
        })



    '''用户信息'''
    def user(self):
        headers={}
        headers['Authorization']='Bearer'+ self.__get_user_token()
        response = requests.get(self.base_url + '/api/user/',headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        filter = Mfilter(self)
        filter.run(data, {
            'data|object|require',
            'message|varchar|require'
        })

    '''忘记密码'''
    def forget_password(self):
        postdata = {'email': '15190257357@163.com'}
        response = requests.post(self.base_url + '/api/forget_password', data=postdata)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'A new code has been sent to your email.')
        self.assertNotEqual(data['data']['email'], '')
        self.assertNotEqual(data['data']['customerId'], '')
        filter = Mfilter(self)
        filter.run(data, {
            'code|int|require',
            'data|object|require',
            'message|varchar|require'
        })
        filter.run(data['data'], {
            'customerId|int|require',
            'email|varchar|require'
        })

    '''验证验证码是否有效'''
    def verification_code_post(self):
        code = "493501"
        postData = {}
        postData['code'] = code
        postData['customer_id'] = 11
        response = requests.post(self.base_url + '/api/check_verification_code', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['data']['verificationCode'], '091002')
        self.assertEqual(data['data']['customerId'], '11')

    '''重置密码'''
    def setup_password(self):
        postData = {}
        postData['customer_id'] = '11'
        postData['password'] = '000000'
        postData['confirm_password'] = '000000'
        response = requests.post(self.base_url + '/api/setup_password', data=postData)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['data'], {})
        filter = Mfilter(self)
        filter.run(data, {
            'code|int|require',
            'data|object|require',
            'message|varchar|require'
        })


    '''分类数据接口'''

    def category(self):
        response = requests.get(self.base_url + "/api/category")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])

        for item in data['data']:
            self.valid_item(item)
    def valid_item(self, item):
        filter = Mfilter(self)
        filter.run(item, {
            'category_id|int|require',
            'image|varchar|require',
            'name|varchar|require',
            'children|array'
        })
        if 'children' in item and len(item['children']) > 0:
            for children in item['children']:
                self.valid_item(children)

    '''分类商品数据'''
    def product_category(self):
        response = requests.get(self.base_url + "/api/product/category"+"?page=1&id=88")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])
        for item in data['data']:
            filter = Mfilter(self)
            filter.run(item, {
                'product_id|int|require',
                'name|varchar|require',
                'price|float|require',
                'image_cover|varchar|require',
                'image_cover_middle|varchar|require	',
                'special|float|require',
                'discount|int|require',
                'is_stock|Bool|require',
                'wish_quantity|int|require',
                'is_wish|bool|require',
                'currency_units|varchar|require'
            })

    '''商品'''
    def product(self):
        product_id = self.conf.get("app", "product_id")
        headers = {'Authorization': 'Bearer ' + self.__get_user_token()}
        response = requests.get(self.base_url + "/api/product", params={'id': product_id}, headers=headers)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data'], [])

    '''首页数据接口'''
    def api(self):
        url='/api?lang=2&channel_id=2&currency_code=*'
        response = requests.get(self.base_url + url)
        self.assertEqual(response.status_code,200)
        data=json.loads(response.text)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'],'success')
        self.assertNotEqual(data['data'],{})
        filter = Mfilter(self)
        filter.run(data['data'],{
            'banner_info|object|require',
            'catagory_info|object|require'
        })

    '''商品详情'''
    def product(self):
        headers={}
        headers['Authorization']='Bearer'+self.__get_user_token()
        headers['device-code']='1fac37e853c6eb74'
        url='/api/product?id=145'
        response = requests.get(self.base_url+ url,headers=headers)
        self.assertEqual(response.status_code, 200)
        data=json.loads(response.text)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], "success")
        self.assertNotEqual(data['data'],[])
        filter = Mfilter(self)
        filter.run(data['data'],{
            'product_id|int|require',
            'special|float|require',
            'discount|int|require',
            'save_price|float ',
            'is_wish|Bool|require',
            'name|varchar|require',
            'image_cover|varchar|require',
            'image_cover_max|varchar|require',
            'images|array|require',
            'images_max|array|require',
            'price|float |require',
            'is_stock|Bool|require',
            'descrption|varchar',
            'attributes|array',
            'discount|int'
        })


    '''添加购物车'''
    def cart_add(self):
        headers={}
        headers['Authorization']='Bearer'+self.__get_user_token()
        url='/api/cart/add?product_id=145'
        response = requests.get(self.base_url+url, headers=headers)
        data= json.loads(response.text)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'],[])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'

        })



    '''更新购物车'''
    def cart_upcart(self):
        headers={}
        headers['Authorization']='Bearer'+self.__get_user_token()
        url= '/api/cart/upcart?product_id=145'
        response = requests.get(self.base_url+url,headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'],'success')
        self.assertNotEqual(data['data'],[])
        filter= Mfilter(self)
        filter.run(data['data'],{
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'

        })

    '''删除购物车'''
    def cart_delcart(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/delcart?product_id=145&add_wishlist=1'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        self.assertEqual(data['data']['totalPrice'],0)
        self.assertEqual(data['data']['quantity'], 0)
        self.assertNotEqual(data['data']['currency_units'],[] )
        self.assertEqual(data['data']['successId'], "145")
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|int|require',
            'quantity|int|require',
            'currency_units|varchar|require',
            'successId|varchar|require',
            'failId|varchar|require'
        })



    '''购物车为空时删除购物车'''
    def cart_null(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/delcart?product_id=145&add_wishlist=1'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        self.assertEqual(data['data']['totalPrice'],0)
        self.assertEqual(data['data']['quantity'], 0)
        self.assertNotEqual(data['data']['currency_units'],[] )
        self.assertEqual(data['data']['successId'], "")
        self.assertEqual(data['data']['failId'], "145")
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|int|require',
            'quantity|int|require',
            'currency_units|varchar|require',
            'successId|varchar|require',
            'failId|varchar|require'
        })


    '''購物車詳細接口'''
    def cart_getCart(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/getCart'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'cartList|array|require',
            'anomalyCartList|array|require',
            'recommendSalesList|array|require',
            'cartTotal|object|require'
        })


    '''獲取購物車總計信息'''
    def cart_getCartTotal(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/getCartTotal'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'
        })

    '''更新購物車IOS'''
    def cart_upCartIos(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/cart/upCartIos?product_id=145'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'cartInfo|object|require',
            'cartTotal|object|require'
        })
        filter.run(data['data']['cartTotal'], {
            'totalPrice|float|require',
            'quantity|int|require',
            'currency_units|varchar|require'
        })

    '''添加删除收藏'''
    def wishlist_addOrDel(self):
        headers={}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        headers['channel_id']=random.randint(1, 4)
        headers['lang'] =random.randint(1, 3)
        headers['device-code'] = '1234567890'
        url='/api/wishlist/addOrDel?product_id=145'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        filter = Mfilter(self)
        filter.run(data, {
            'data|array|require'
        })


    '''我的收藏'''
    def api_wishlist(self):
        headers = {}
        headers['Authorization'] = 'Bearer'+self.__get_user_token()
        url = '/api/wishlist?page=1'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertNotEqual(data['data'], [])
        for item in data['data']:
            self.assertEqual(item['product_id'],145)
            filter = Mfilter(self)
            filter.run(item, {
                'product_id|int|require',
                'name|varchar|require',
                'price|float|require',
                'image|varchar|require',
                'viewed|int|require',
                'quantity|int|require',
                'status|int|require',
                'is_wish|bool|require',
                'wishlist_total|int|require',
                'currency_units|varchar|require'
            })

    '''地址查询'''
    def select_address(self):
        headers = {}
        headers['Authorization'] = 'Bearer'+self.__get_user_token()
        url='/api/select_address'
        response =requests.get(self.base_url+url,headers=headers)
        data=json.loads(response.content)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'], 'success')
        for item in data['data']['addressInfos']:
            filter=Mfilter(self)
            filter.run(item,{
                'id|int|require',
                'customerId|int|require',
                'firstName|varchar|require',
                'lastName|varchar|require',
                'streetInfo|varchar|require',
                'countryId|int|require',
                'zoneId|int|require',
                'cityId|int|require',
                'districtId|int|require',
                'mobile|varchar|require',
                'addTime|varchar|require',
                'isDefault|int|require',
                'areaCode|varchar|require',
                'countryName|varchar|require',
                'countryDeep|int|require',
                'zoneName|varchar|require',
                'zoneDeep|int|require',
                'cityName|varchar|require',
                'cityDeep|int|require',
                'districtName|varchar|require',
                'districtDeep|int|require'
            })
            content = json.loads(response.content)['data']['addressInfos']
            for item in content:
                id = item['id']
                return id


    '''删除地址'''
    def delete_address(self):
        id = self.select_address()
        headers={}
        headers['Authorization']='Bearer '+ self.__get_user_token()
        url = self.base_url+'/api/delete_address?address_id='+str(id)
        response = requests.get(url,headers=headers)
        data=json.loads(response.content)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'],'success')
        self.assertNotEqual(data['data'],[])
        self.assertEqual(data['data']['deleteNum'],1)
        filter=Mfilter(self)
        filter.run(data['data'],{
            'deleteNum|int|require',
            })


    '''新增地址'''
    def insert_address(self):
        headers = {}
        postdata={}
        postdata['first_name']='wukefan'
        postdata['last_name'] = 'om'
        postdata['country_id'] = 1878
        postdata['zone_id'] = 2536
        postdata['city_id'] = 233059
        postdata['street_info'] = '<script>alert(document.cookie)</script>'
        postdata['mobile'] = 123213232
        postdata['area_code'] = 971
        postdata['is_default'] = 0
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/insert_address'
        response = requests.post(self.base_url + url, headers=headers,data=postdata)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        for item in data['data']['addressInfo']:
            filter = Mfilter(self)
            filter.run(item, {
                'id|int|require',
                'customerId|int|require',
                'firstName|varchar|require',
                'lastName|varchar|require',
                'streetInfo|varchar|require',
                'countryId|int|require',
                'countryName|varchar|require',
                'zoneId|int|require',
                'zoneName|varchar|require',
                'cityId|int|require',
                'cityName|varchar|require',
                'districtId|int|require',
                'districtName|varchar|require',
                'addTime|varchar|require',
                'mobile|varchar |require',
                'isDefault|int|require',
                'areaCode|varchar|require',
                'countryDeep|int|require',
                'zoneDeep|int|require',
                'cityDeep|int|require',
                'districtDeep|int|require'
            })

    '''国家城市信息联查'''
    def area_info(self):
        headers={}
        headers['Authorization']= 'Bearer '+self.__get_user_token()
        url= '/api/area_info'
        response =requests.get(self.base_url+url,headers=headers)
        data= json.loads(response.content)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'], "success")
        self.assertNotEqual(data['data'], [])
        self.assertNotEqual(data['data']['areaInfo'], [])
        for item in data['data']['areaInfo']:
            filter=Mfilter(self)
            filter.run(item,{
                'id|int|require',
                'name|varchar|require',
                'parentId|int|require',
                'code|varchar|require',
                'deep|int|require',
                'subset|int|require',
                'areaCode|varchar|require'
            })

    '''地址更新'''
    def update_address(self):
        headers = {}
        headers['Authorization']='Bearer'+self.__get_user_token()
        postdata = {}
        postdata['first_name'] = 'wukefan'
        postdata['last_name'] = 'om'
        postdata['country_id'] = 1878
        postdata['zone_id'] = 2536
        postdata['city_id'] = 233059
        postdata['street_info'] = '<script>alert(document.cookie)</script>'
        postdata['mobile'] = 123213232
        postdata['area_code'] = 971
        postdata['address_id'] = 162
        url = '/api/update_address'
        response = requests.post(self.base_url + url, headers=headers, data=postdata)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], 'success')
        self.assertEqual(data['data']['addressId'], '162')

        for item in data['data']['addressInfo']:
            filter = Mfilter(self)
            filter.run(item, {
                'id|int|require',
                'customerId|int|require',
                'firstName|varchar|require',
                'lastName|varchar|require',
                'streetInfo|varchar|require',
                'countryId|int|require',
                'countryName|varchar|require',
                'zoneId|int|require',
                'zoneName|varchar|require',
                'cityId|int|require',
                'cityName|varchar|require',
                'districtId|int|require',
                'districtName|varchar|require',
                'addTime|varchar|require',
                'mobile|varchar |require',
                'isDefault|int|require',
                'areaCode|varchar|require',
                'countryDeep|int|require',
                'zoneDeep|int|require',
                'cityDeep|int|require',
                'districtDeep|int|require'
            })

    '''立即购买--验证优惠码接口'''
    def coupon_verify(self):
        headers={}
        headers['Authorization']='Bearer'+self.__get_user_token()
        url='/api/coupon/verify?code=666666&type=2&product_id=145&quantity=1'
        response=requests.get(self.base_url+url,headers=headers)
        data=json.loads(response.content)
        self.assertEqual(response.status_code,200)
        self.assertEqual(data['code'],0)
        self.assertEqual(data['message'], "success")
        self.assertNotEqual(data['data']['discount'],[])

    '''購物車--验证优惠码接口'''
    def Cart_coupon_verify(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/coupon/verify?code=666666'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], "success")
        self.assertNotEqual(data['data']['discount'], [])



    '''购物车确认订单'''
    def api_checkout(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url='/api/checkout'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        print data['data']['cartList']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], "success")
        self.assertEqual(data['data']['addressInfo']['id'], 162)
        filter = Mfilter(self)
        filter.run(data['data'], {
            'discountPrice|int|require',
            'freightPrice|float|require',
            'currencyUnits|varchar|require',
            'orderTotalPrice|float|require'
        })
        filter.run(data['data']['cartTotal'], {
            'currencyUnits|varchar|require',
            'totalPrice|int|require',
            'quantity|int|require'
        })
        filter.run(data['data']['addressInfo'], {
            'id|int|require',
            'customerId|int|require',
            'firstName|varchar|require',
            'lastName|varchar|require',
            'streetInfo|varchar|require',
            'countryId|int|require',
            'zoneId|int|require',
            'cityId|int|require',
            'districtId|int|require',
            'mobile|varchar|require',
            'addTime|varchar|require',
            'isDefault|int|require',
            'areaCode|varchar|require',
            'countryName|varchar|require',
            'countryDeep|int|require',
            'zoneName|varchar|require',
            'zoneDeep|int|require',
            'cityName|varchar|require',
            'cityDeep|int|require'
        })
        for item in data['data']['cartList']:
            filter.run(item, {
                'status|int|require',
                'name|varchar|require',
                'image|varchar|require',
                'tax_class_id|int|require',
                'currency_units|varchar|require',
                'price|int|require',
                'product_id|int|require',
                'product_quantity|int|require',
                'stock|int|require',
                'cart_id|int|require',
                'special|float|require',
                'quantity|int|require'
            })

    '''立即购买--确认订单'''
    def api_immediatebuy(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        url = '/api/immediatebuy?product_id=145'
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], "success")
        self.assertNotEqual(data['data']['product'],[])
        for item in data['data']['product']:
            self.assertEqual(item['product_id'], 145)
            filter = Mfilter(self)
            filter.run(item,{
                'product_id|int|require',
                'name|varchar|require',
                'image|varchar|require',
                'quantity|int|require',
                'product_quantity|int|require',
                'stock|int|require',
                'status|int|require',
                'price|int|require',
                'special|float|require',
                'currency_units|varchar|require',
                'total|int|require'

            })

    '''提交订单'''
    def order_store(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        postdata={}
        postdata['address_id']=162
        postdata['channel_id'] = 3
        url = '/api/order/store'
        response = requests.post(self.base_url + url,data=postdata,headers=headers,)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data']['order_id'],[] )
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run(data['data'], {
            'order_id|int|require'
        })



    '''立即购买--提交订单'''
    def immediateBuy(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        postdata={}
        postdata['channel_id']=(random.randint(2, 4))

        postdata['address_id']=162
        url = '/api/order/immediateBuy?product_id=145'
        response = requests.post(self.base_url + url, headers=headers,data=postdata)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertNotEqual(data['data']['order_id'], [])
        self.assertNotEqual(data['data'], [])
        filter = Mfilter(self)
        filter.run( data['data'], {
            'order_id|int|require'
        })


    '''(post)用户中心-订单列表查询多条'''
    def order_list(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        headers['channel_id'] = str(random.randint(2, 4))
        headers['lang'] = str(random.randint(1, 3))
        headers['currencycode'] = 'usd'
        postdata={}
        postdata['page']='1'
        postdata['limit'] = '21'
        url = '/api/order/list'
        response = requests.post(self.base_url + url, headers=headers,data=postdata)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        filter = Mfilter(self)
        filter.run( data['data'], {
            'total|int|require',
            'orders|array|require'
        })
        for item in data['data']['orders']:
            filter = Mfilter(self)
            filter.run(item, {
                'orderId|int|require',
                'orderSn|varchar|require',
                'status|varchar|require',
                'orderStatusId|int|require',
                'addTime|varchar|require',
                'totalPrice|float|require',
                'currencyUnits|varchar|require',
                'productNum|int|require',
                'products|array|require'
            })

    '''(get)用户中心-订单列表查询单条'''
    def order_list_status(self):
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        headers['channel_id'] = str(random.randint(2, 4))
        headers['lang'] = str(random.randint(1, 3))
        headers['currencycode'] = 'usd'
        url = '/api/order/list?order_status_id=1&page=1&limit=21'
        response = requests.post(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        filter = Mfilter(self)
        filter.run(data['data'], {
            'total|int|require',
            'orders|array|require'
        })
        for item in data['data']['orders']:
            self.assertEqual(item['orderStatusId'],1)
            filter = Mfilter(self)
            filter.run(item, {
                'orderId|int|require',
                'orderSn|varchar|require',
                'status|varchar|require',
                'orderStatusId|int|require',
                'addTime|varchar|require',
                'totalPrice|float|require',
                'currencyUnits|varchar|require',
                'productNum|int|require',
                'products|array|require'
            })
            content = json.loads(response.content)['data']['orders']
            for item in content:
                orderId = item['orderId']
                return orderId

    '''(get)用户中心-订单详情'''
    def order_detail01(self):
        orderId=self.order_list_status()
        headers = {}
        headers['Authorization'] = 'Bearer' + self.__get_user_token()
        headers['lang'] = str(random.randint(1, 3))
        headers['currencycode'] = 'usd'
        url = '/api/order/detail?order_id='+str(orderId)
        response = requests.get(self.base_url + url, headers=headers)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['code'], 0)
        self.assertEqual(data['message'], "success")
        self.assertEqual(data['data']['orderInfo']['id'], 431)
        # filter = Mfilter(self)
        # filter.run(data['data']['orderInfo'], {
        #     'total|int|require',
        #     'orders|array|require'
        # })
        # for item in data['data']['orders']:
        #     self.assertEqual(item['orderStatusId'], 1)
        #     filter = Mfilter(self)
        #     filter.run(item, {
        #         'orderId|int|require',
        #         'orderSn|varchar|require',
        #         'status|varchar|require',
        #         'orderStatusId|int|require',
        #         'addTime|varchar|require',
        #         'totalPrice|float|require',
        #         'currencyUnits|varchar|require',
        #         'productNum|int|require',
        #         'products|array|require'
        #     })


    # '''(post)用户中心-订单详情'''
    # def order_detail02(self):
    #     headers = {}
    #     headers['Authorization'] = 'Bearer' + self.__get_user_token()
    #     headers['channel_id'] = str(random.randint(2, 4))
    #     headers['lang'] = str(random.randint(1, 3))
    #     headers['currencycode'] = 'usd'
    #     url = '/api/order/list?order_status_id=1&page=1&limit=21'
    #     response = requests.post(self.base_url + url, headers=headers)
    #     data = json.loads(response.content)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['code'], 0)


    def tearDown(self):
        pass



if __name__ == "__main__":
    unittest.main()
