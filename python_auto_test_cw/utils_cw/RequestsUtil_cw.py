
#-----------------------------------封装请求方法工具类-----------------------------------

import requests #导入请求接口库
from utils_cw.LogUtil_cw import my_log #导入日志

#创建类
class Requests:
    #初始化
    def __init__(self):
        # pass #后续再增加
       self.log=my_log('Requests')

    #定义请求接口方法-公共方法
    #data-请求参数类型1、json-请求参数类型2
    def requests_api(self,url,json=None,headers=None,cookies=None,method='get'):
        #data=None-表示可以不传，为空，#method='get'-表示不传，默认为get
        print('requests_api-json:',json)

        global result #定义为全局变量
        if method=='get': #判断为get请求方法
            self.log.debug('日志-发送get请求')
            result=requests.get(url,params=json,headers=headers,cookies=cookies)
            print('requests_api-get-返回结果res:', result.json())
        elif method=='post': #判断为post请求方法
            self.log.debug('日志-发送post请求')
            result=requests.post(url,data=json,headers=headers,cookies=cookies) #这运行居然成功了
            # result=requests.post(url,data=data,json=json,headers=headers,cookies=cookies)
            print('requests_api-post-返回结果res:', result.json())
        else:
            print('请检查所输入的请求方法是否有误！')

        result_code=result.status_code #获取接口返回的状态

        #若获取的内容分为json格式、其它格式
        try:
            body=result.json()
        except Exception as e: #若获取json格式内容报异常，则获取文本内容
            body=result.text

        res=dict() #定义空字典
        res['code']=result_code #获取的状态码存到字典
        res['body']=body #获取的body内容存到字典

        return res #返回字典

    #get方法重构
    def get(self,url,**kwargs):#url参数-必传，**kwargs-表示传不定参数，传0个、1个、2个等都行
        return self.requests_api(url,method='get',**kwargs) #调用公共方法，并返回

    #post方法重构
    def post(self,url,**kwargs):#url参数-必传，**kwargs-表示传不定参数，传0个、1个、2个等都行
        return self.requests_api(url,method='post',**kwargs) #调用公共方法，并返回
































