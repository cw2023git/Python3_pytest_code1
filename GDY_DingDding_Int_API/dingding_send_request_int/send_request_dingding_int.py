
#--------------------------------读取Excel表中的数据作为request请求的参数--------------------------------

#其实，就是构造请求方式

from dingding_test_data_int.dingding_excel_data_int.xlrd_openpyxl_excel_dingding import * #导入xlrd_openpyxl_excel模块中的所有内容(只是为了调试运行用而已)
import requests
import json
import os
import configparser as cfparser #别名，导入读取配置文件模块

base_dir = os.path.dirname(os.path.dirname(__file__)) #获取当前路径
conf_file_path = os.path.join(base_dir,"config_file","config.ini") #获取配置文件完整路径

#--------------------读取config.ini配置文件--------------------
con_fig=cfparser.ConfigParser() #实例化cfparser，生成con_fig对象
con_fig.read(conf_file_path,encoding='utf-8') #读取配置文件内容

host_url=con_fig.get('hosts','host_url') #获取配置文件-“config.ini”中‘hosts’分组下‘host_url’的值

class Request():
    # 传入读取excel表返回的数据列表
    def send_request(self,api_data,json_data):
        global header #全局变量

        #获取配置文件 -“config.ini”中‘headers’分组下‘headers_cw32’的值
        if api_data['headers']=='headers_cw':header=con_fig.get('headers','headers_cw') #主管理员-蔡文（id=32）
        if api_data['headers']=='headers_ljh':header=con_fig.get('headers','headers_ljh') #被考核人-刘俊华（id=26）
        if api_data['headers']=='headers_lsx':header=con_fig.get('headers','headers_lsx') #部门主管-刘水线（id=31）【目标确认、结果值录入、一级部门主管评分、一级部门主管审批】
        if api_data['headers']=='headers_ljh':header=con_fig.get('headers','headers_ljh') #特定指标评分人-刘俊华（id=35）
        if api_data['headers']=='headers_sgf':header=con_fig.get('headers','headers_sgf') #管理记录人-孙贵芳（id=24）

        url1=host_url  #host，统一的一个地址
        url2=api_data['request_url']  #具体请求的一个地址
        method=api_data['method']     #接口的请求方式

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
            res = requests.session().request(url=url1 + url2, headers=eval(header), params=json_data, method=method,data=json_data, verify=False,timeout=0.5)
        else:
            res = requests.session().request(url=url1 + url2, headers=eval(header), params=param, method=method, data=body,verify=False,timeout=0.5) #时间单位：秒

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
    box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_导入导出.xlsx','导入导出接口')

    testData=box_excel.read_excel()
    print('读取Excel表中的数据：',testData)

    #传入返回的读取excel表的数据
    reponse=Request().send_request(testData[2],json_data) #表示传入的第几行excel表数据(数组下标)
    print('输出响应的状态码:',reponse.status_code) #输出响应的状态码
    print('响应的结果:',reponse.json()) #输出响应的结果


























































