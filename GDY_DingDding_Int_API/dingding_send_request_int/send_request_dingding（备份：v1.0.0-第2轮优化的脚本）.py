
#--------------------------------读取Excel表中的数据作为request请求的参数--------------------------------

#其实，就是构造请求方式

from dingding_test_data.dingding_excel_data.xlrd_openpyxl_excel_dingding import * #导入xlrd_openpyxl_excel模块中的所有内容(只是为了调试运行用而已)
import requests
import json

class Request():
    # 传入读取excel表返回的数据列表
    def send_request(self,api_data,json_data):
    # def send_request(self,api_data):
        url1=api_data['host_url']     #host，统一的一个地址
        url2=api_data['request_url']  #具体请求的一个地址
        method=api_data['method']     #接口的请求方式

        #判断请求头header是否为空
        if api_data['headers']=='':
            header=None
        else:
            header=eval(api_data['headers']) #eval()函数把字符串转化为字典

        #判断参数params是否为空
        if api_data['params']=='':
            param=None
        else:
            # eval函数就是实现list、dict、tuple与str之间的转化
            param=eval(api_data['params']) #eval()函数把字符串转化为字典

        #判断body数据是否为空
        if api_data['body']=='':
            body_data=None
        else:
            body_data=eval(api_data['body'])#eval()函数把字符串转化为字典
            # print('body_data:',body_data)

        #判断数据类型（json、data）
        type=api_data['data_type'] #获取数据对应的类型
        if type=='data': #判断为data格式数据
            body=json.dumps(body_data) #把python字符串型转化为json格式数据
            # print('body-data:',body)
        elif type=='json': #判断为json表单数据
            body=body_data
            # print('body-json:',body)
        else: #判断为空的，也默认为json数据
            body=body_data

        #构造发送请求
        # res=requests.session().request(url=url1+url2,headers=header,params=param,method=method,data=body,verify=False)
        if api_data['params']=="" and api_data['body']=="":
            res = requests.session().request(url=url1 + url2, headers=header, params=json_data, method=method,data=json_data, verify=False,timeout=0.5)
        else:
            res = requests.session().request(url=url1 + url2, headers=header, params=param, method=method, data=body,verify=False,timeout=0.5) #时间单位：秒

        return res #返回响应的结果

#调试运行
if __name__ == '__main__':
    json_data=1

    #读取excel表中的数据，并返回
    # box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_指标.xlsx','指标库接口')
    # box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_考评组.xlsx','考评组')
    # box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_考核包.xlsx','考核管理')
    # box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_数据统计.xlsx','数据统计')
    # box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_数据同步接口.xlsx','数据同步接口')
    # box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_主流程.xlsx','主流程接口')
    # box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_导入导出.xlsx','导入导出接口')
    box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_主流程.xlsx','主流程接口')

    testData=box_excel.read_excel()
    print('读取Excel表中的数据：',testData)

    #传入返回的读取excel表的数据
    reponse=Request().send_request(testData[0],json_data) #表示传入的第几行excel表数据(数组下标)
    print('输出响应的状态码:',reponse.status_code) #输出响应的状态码
    print('响应的结果:',reponse.json()) #输出响应的结果


























































