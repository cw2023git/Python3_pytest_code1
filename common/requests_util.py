
import requests,json

#封装就意味着，这个方法要能够适应所有的请求
class request_util():
    #全局变量，类变量，通过类名调用
    sess=requests.session()                                 #**kwargs-可变长度参数，即：参数可以多个、可以0个
    def send_requests(self,method,url,datas=None,**kwargs): #datas=None,表示datas允许为空的
       method=str(method).lower() #先转换成字符串，再转换成小写
       res=None #初始值为空的
       if method=='get':
           res=request_util.sess.request(method=method,url=url,params=datas,**kwargs)
       elif method=='post':
           #判断不同的请求头类型，使用不同的数据格式
           if Content-Type=='application/x-www-form-urlencoded':
           if Content-Type=='text/plain':
           if Content-Type=='application/json':

              datas=json.dumps(datas) #此处，数据不管是否‘嵌套字典’，都转换成json格式字符串（为了兼容这两种数据）
           res=request_util.sess.request(method=method, url=url, data=datas, **kwargs)#统一用data
       else:
           pass
       return res #返回
































