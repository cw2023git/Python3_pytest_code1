
#1、创建封装get方法
#2、发送requests get请求
#3、获取结果相应内容
#4、内存存到字典
#5、字典返回

import requests
from utils.LogUtils import my_log

def requests_get(url,headers):
    r=requests.get(url,headers=headers)
    code=r.status_code
    try:
        body=r.json()
    except Exception as e:
        body=r.text
    res=dict() #定义空字典
    res['code']=code
    res['body']=body
    return res


#1、创建封装post方法
#2、发送requests post请求
#3、获取结果相应内容
#4、内存存到字典
#5、字典返回

def requests_post(url,json=None,headers=None):
    r=requests.post(url,json=json,headers=headers)
    code = r.status_code
    try:
        body=r.json()
    except Exception as e:
        body=r.text
    res = dict()  # 定义空字典
    res['code'] = code
    res['body'] = body
    return res

#重构：是指重新写，把之前get方法、pots方法，有重复部分进行整合、重组，让整个代码看起来，整洁
#1、创建类
class Request:
    #2、定义公共方法
    def __init__(self): #这个是初始化方法
        self.log=my_log("Requests")

    #增加方法的参数，根据参数来验证方法get/post，方法请求
    def requests_api(self,url,data=None,json=None,headers=None,cookies=None,method="get"):#method="get"-表示传入一个默认值，
                                                                                          #当不传method参数时，默认使用get请求
       global r #设置为全局变量
       if method=="get": #get请求
           self.log.debug("发布get请求")
           r = requests.get(url,data=data,json=json, headers=headers,cookies=cookies)
       elif method=="post": #post请求
           self.log.debug("发布post请求")
           r = requests.post(url,data=data, json=json, headers=headers,cookies=cookies)
       code = r.status_code
       try:
           body = r.json()
       except Exception as e:
           body = r.text
       res = dict()  # 定义空字典
       res['code'] = code
       res['body'] = body
       return res

    #3、重构get/post方法
    #get
    #1、定义方法
    def get(self,url,**kwargs):
    #2、定义参数
    #使用‘**kwargs’，不定参数即可

    #3、调用公共方法
        return self.requests_api(url,method="get",**kwargs)

    def post(self,url,**kwargs):
    #2、定义参数
    #使用‘**kwargs’，不定参数即可

    #3、调用公共方法
        return self.requests_api(url,method="post",**kwargs)