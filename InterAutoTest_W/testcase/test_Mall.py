
import os
import json
from utils.RequestsUtil import *
import yaml
import pytest
from config.config import ConfigYaml
from utils.AssertUtil import AssertUtil
from common.Base import init_db

"""
login_4	登录	登录成功	http://211.103.136.242:8062/authorizations/
POST	json	{"username":"python","password":"12345678"}
"""
#登录
import requests

def test_login():
    url="http://211.103.136.242:8062/authorizations/"
    data={"username":"python","password":"12345678"}
    r=requests.post(url,json=data,headers=None,cookies=None)
    print(r.json())

    code=r['code'] #返回状态码
    body=r['body'] #获取返回结果中的‘body’的内容
    # 在这里写吧-调用‘断言’的方法（我也不知道对不对）
    AssertUtil.assert_code(code, 200)
    AssertUtil.assert_in_body(body, '"username":"python","password":"12345678"')

    #1、初始化数据库对象
    conn=init_db("db_1")

    #2、查询结果
    #分析：根据username=python，来获取到对应的user_id，根据接口中返回的user_id进行对比数据库中的id
    # res_db=conn.fetchone("select id from tb_users where username='python'") #显示一个数据，id
    # print('数据库查询结果：', res_db)  # 查询方式1

    res_db=conn.fetchone("select id,username from tb_users where username='python'") #显示多个数据，id、username
    print('数据库查询结果：',res_db) #查询方式1，，，那么返回的就是一个’元组‘，取数据时，很不方便，需要处理下
    # print('数据库查询结果：%s'%res_db) #查询方式2

    #3、验证（断言）
    user_id=body["user_id"]
    assert user_id==res_db["id"] #接口中返回的id跟数据库中的id进行对比，断言


    #调用‘RequestsUtil.py’文件中的post方法
    rrr = requests_post(url, json=data)
    print(rrr)  #此方法，有返回，直接输出请求结果即可

    #使用‘重构’的类
    res = Request()  #初始化类
    r = res.post(url, json=data)
    print(r)

    #使用读取配置文件方法
    conf_y=ConfigYaml()
    url_path=conf_y.get_config_url()
    url=url_path+"/authorizations/"



"""
info_2	个人信息	获取个人信息正确	http://211.103.136.242:8062/user/	登录	GET	json

headers:{
        'Authorization':'JWT'+this.token
}
"""
def test_info():
    url="http://211.103.136.242:8062/user/"
    token='sdsfsfsfsdf123233543' #乱写的
    headers={'Authorization':'JWT'+token}
    r=requests.get(url,headers=headers)
    print(r.json())

    #调用‘RequestsUtil.py’文件中的get方法
    rrr = requests_get(url, headers=headers)
    print(rrr)  #此方法，有返回，直接输出请求结果即可

    #使用‘重构’的类
    res=Request() #初始化类
    r=res.get(url,headers=headers)
    print(r)

"""
cate_1	商品列表数据	商品列表数据正确	http://211.103.136.242:8062/categories/115/skus/		
GET	json	"{""page"":""1""，
              ""page_size"":""10"",
              ""ordering"":""creat_time""}"
"""
def goods_list():
    url="http://211.103.136.242:8062/categories/115/skus/"
    data={"page":"1",
          "page_size":"10",
          "ordering":"creat_time"}
    token='sdsfsfsfsdf123233543' #乱写的
    headers={'Authorization':'JWT'+token}
    r=requests.get(url,json=data)
    print(r.json())

"""
cart_1	购物车	添加购物车成功	http://211.103.136.242:8064/cart/	登录	
POST	json	"{""sku_id"":""3"",""count"":""1"",""selected"":""true""}"
"""
def cart():
    url="http://211.103.136.242:8064/cart/"
    data={"sku_id":"3","count":"1","selected":"true"}
    token='sdsfsfsfsdf123233543' #乱写的
    headers={'Authorization':'JWT'+token}
    r=requests.post(url,json=data,headers=headers)
    print(r.json())

"""
order_1	订单	保存订单	http://211.103.136.242:8064/orders/	登录	
POST	json	{"address":"1","pay_method":"1"}
"""
def order():
    url="http://211.103.136.242:8064/orders/"
    data={"address":"1","pay_method":"1"}
    token='sdsfsfsfsdf123233543' #乱写的
    headers={'Authorization':'JWT'+token}
    r=requests.post(url,json=data,headers=headers)
    print(r.json())


if __name__ == '__main__':
    # login()
    # info()
    # goods_list()
    # cart()
    # order()

    #1、根据默认运行原则，调整py文件命名，函数命名
    #2、pytest.main()运行或者命令行直接pytest运行
    pytest.main()


























