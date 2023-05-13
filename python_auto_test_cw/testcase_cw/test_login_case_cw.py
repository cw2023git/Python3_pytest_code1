
#-----------------------------------登录测试用例模块封装-----------------------------------

from config_cw.Config_cw import ConfigYaml #导入配置文件
from config_cw import Config_cw #导入整个配置文件
import os
from common_cw.ExcelData_cw import Data #导入获取excel数据文件
from utils_cw.LogUtil_cw import my_log #导入日志文件
from common_cw import ExcelConfig_cw #导入封装excel列属性方法
from utils_cw.RequestsUtil_cw import Requests #导入请求接口库
import json
import pytest
from common_cw import Base_cw #导入基本方法
from utils_cw.AssertUtil_cw import AssertUtil #导入断言
import time #导入时间库
import allure #导入测试报告库


#获取测试用例文件路径
case_file=os.path.join(Config_cw.get_data_path(),ConfigYaml().get_excel_file()) #通过拼接路径，获取excel文件
print('获取测试用例文件路径:',case_file)

#获取测试用例sheet名称
sheet_name=ConfigYaml().get_excel_sheet()
print('获取测试用例sheet名称:',sheet_name)

#获取运行测试用例列表
# run_list=Data(case_file,sheet_name).get_run_data() #调用、初始化类，并获取全部测试用例数据(不采用)
data_init=Data(case_file,sheet_name) #调用、初始化类
run_list=data_init.get_run_data()    #此时获取到了全部需要执行的测试用例数据
print('获取运行测试用例列表-run_list:',run_list)

#日志
log=my_log() #直接调用此方法

#初始化dataconfig
data_key=ExcelConfig_cw.DataConfig

#封装类
class TestExcel:
    #定义运行接口的方法
    def run_api(self,url,method,params=None,header=None,cookie=None):
        print('run_api-params:',params)
        request=Requests() #初始化类
        if len(str(params).strip()) != 0: #判断params有没有内容
            # print('判断为请求参数中有内容:',params)
            params=json.loads(params) #转化为json格式
            # print('run_api-params:',type(params))

        if str(method).lower()=='get': #判断为get请求方式
            res=request.get(url,json=params,headers=header,cookies=cookie)
        elif str(method).lower()=='post': #判断为post请求方式
            res=request.post(url,json=params,headers=header,cookies=cookie)
        else:
            log.error("这是一个错误请求！",method)
        return res #返回请求接口响应内容

    #定义运行前置用例的方法
    def run_pre(self,pre_case): #传入前置用例参数
        #初始化数据
        url=ConfigYaml().get_config_url()+pre_case[data_key.url] #主域名 拼接 接口URL  替换后
        method=pre_case[data_key.method] #请求类型
        params=pre_case[data_key.params] #请求参数
        headers=pre_case[data_key.headers] #请求头
        cookies=pre_case[data_key.cookies] #cookies

        header=Base_cw.json_pars(headers) #进行json转移
        cookie=Base_cw.json_pars(cookies) #进行json转移

        res=self.run_api(url,method,params,header) #调用请求接口的方法
        print('前置用例执行:',res)
        return res #返回请求接口的结果

    #pytest参数化
    @pytest.mark.parametrize("case",run_list) #所有的测试用例数据，已获取、传入参数名-case
    def test_run(self,case):
        url=ConfigYaml().get_config_url()+case[data_key.url] #主域名 拼接 接口URL  替换后
        print('执行用例对应的接口完整地址：',url)
        case_id = case[data_key.case_id]  # 用例ID
        case_model = case[data_key.case_model]  # 模块
        case_name = case[data_key.case_name]  # 接口名称
        pre_exec = case[data_key.pre_exec]  # 前置条件（首先判断是否存在）
        method = case[data_key.method]  # 请求类型
        params_type = case[data_key.params_type]  # 请求参数类型
        params = case[data_key.params]  # 请求参数
        print('params:',params)
        expect_result = case[data_key.expect_result]  # 预期结果
        # actual_result = case[data_key.actual_result] #实际结果，没什么用
        # is_run = case[data_key.is_run] #是否运行，没什么用
        headers = case[data_key.headers]  # 请求头
        cookies = case[data_key.cookies]  # cookies
        code = case[data_key.code]  # 状态码
        db_verify = case[data_key.db_verify]  # '数据库验证'

        #先替换请求参数中固定内容
        if len(str(params).strip()) != 0:  #判断params有没有内容
            params_para = Base_cw.static_params_find(params)  #获取需替换的内容
            print('获取需替换的内容:', params_para)
            params = Base_cw.static_sub(params,
                                        str(params_para) + str(int(time.time())))  # headers-要传的信息，headers_data-要替换的内容
            print('结果替换后的请求参数内容：', params)
        else:
            print('判断为请求参数中无内容!')

        #验证前置条件【首先必须需要判断是否有‘前置条件’】
        if pre_exec: #判断存在有‘前置条件’-就执行，判断没有‘前置条件’-不执行
            print('前置条件用例名称：', pre_exec)
            pre_case=data_init.get_case_pre(pre_exec) #把‘前置条件’传入
            pre_res=self.run_pre(pre_case) #把前置用例传入，再运行此用例，运行前置条件对应的用例返回的响应内容
            # headers,cookies=self.get_correlation(headers,cookies,pre_res) #调用动态关联方法，返回替换的结果
            params=self.get_correlation(params,pre_res) #调用动态关联方法，返回替换的结果

        header=Base_cw.json_pars(headers) #进行json转义
        cookie=Base_cw.json_pars(cookies) #进行json转义

        res=self.run_api(url,method,params,header,cookie) #执行所要执行的用例，发送接口请求
        print('测试用例执行返回结果:',res)

        #allure测试报告
        allure.dynamic.feature(sheet_name) #sheet名称 feature 作为‘一级标签’
        allure.dynamic.story(case_model) #模块 story 作为‘二级标签’
        allure.dynamic.title(case_id+case_name) #用例ID + 接口名称 作为‘title’

        #请求URL 请求类型 期望结果 实际结果 作为‘描述’【作废】
        desc = "<font color='red'>请求URL:</font>{}<Br/>" \
               "<font color='red'>请求类型:</font>{}<Br/>" \
               "<font color='red'>期望结果:</font>{}<Br/>" \
               "<font color='red'>实际结果:</font>{}".format(url, method, expect_result, res)

        desc1 = "请求URL:{}\r\n请求类型:{}\r\n期望结果:{}\r\n实际结果:{}".format(url, method, expect_result, res)
        allure.dynamic.description(desc1)

        #结果断言验证
        #验证如下内容：验证码、返回结果内容、数据库相关的结果的验证
        #断言-验证状态码
        assert_util=AssertUtil() #调用、初始化类
        assert_util.assert_code(int(res['code']),int(code))

        #断言-验证返回结果内容
        assert_util.assert_in_body(str(res['body']),str(expect_result))
        # assert_util.assert_in_body(str(res['body']),'"code": 1, "msg": "提交成功"')

        #断言-数据库结果断言
        # Base_cw.assert_db("db_1", res['body'], db_verify)


    #动态关联：定义‘关联’公共方法
    # def get_correlation(self,headers,cookies,pre_res):
    def get_correlation(self,params,pre_res):
        #1、验证是否有关联
        # headers_para,cookies_para=Base_cw.params_find(headers,cookies) #获取需关联的内容，验证是否存在关联
        params_para=Base_cw.params_find(params) #获取需关联的内容，验证是否存在关联
        print('获取需关联的内容:', params_para)

        #2、有关联，执行前置用例，获取结果
        if len(params_para): #判断headers_para长度是否为0，为0表示无关联内容，无需执行前置用例
            # params_para=pre_res['body'][params_para[0]] #获取前置用例-接口返回指定的值
            params_para=str(pre_res['body']['data'][params_para[0]][0]['id']) #获取前置用例-接口返回指定的值
            print('获取前置用例-接口返回指定的值:',params_para)
            #结果替换
            params=Base_cw.res_sub(params,params_para) #params-要传的信息，params_data-要替换的内容
            print('结果替换后的请求参数内容：', params)

        return params #返回

if __name__ == '__main__':
    # pytest.main() #调试、运行，运行多个用例
    report_path=Config_cw.get_report_path()+os.sep+'result'    #拼接目录名称，存放测试结果（result-自动生成文件夹）
    print('result路径：',report_path)
    report_html_path=Config_cw.get_report_path()+os.sep+'html' #拼接目录名称，存放测试报告文件
    print('html路径：', report_html_path)

    # pytest.main(['-s','test_excel_case_cw.py','--alluredir',report_path]) #运行
    pytest.main(['-s','--alluredir',report_path]) #运行

    Base_cw.allure_report(report_path,report_html_path) #自动成成测试报告














































































































