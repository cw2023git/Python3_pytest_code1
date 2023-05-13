
from config.config import ConfigYaml
from config import config
import os
from common.ExcelData import Data
from utils.LogUtils import my_log
from common import ExcelConfig
from utils.RequestsUtil import Request
import json
import pytest
from common import Base
from utils.AssertUtil import AssertUtil #导入断言
import allure #导入测试报告库

#1、初始化信息
#（1）、初始化测试用例文件
# case_file=os.path.join("../data",ConfigYaml().get_excel_file()) #获取excel文件（相对路径）
case_file=os.path.join(config.get_data_path(),ConfigYaml().get_excel_file()) #获取excel文件（绝对路径-建议采用）

#（2）、测试用例sheet名称
sheet_name=ConfigYaml().get_excel_sheet() #获取sheet名称

#（3）、获取运行测试用例列表
data_init=Data(case_file,sheet_name)
run_list=data_init.get_run_data()

#（4）、日志
log=my_log()

#初始化dataconfig
data_key=ExcelConfig.DataConfig

#2、测试用例方法、参数化运行
#先完成一个用例的执行（若代码通了，再执行所有的用例）
#（1）、初始化信息，如：url，data
"""
class TestExcel:
    def test_run(self):
        data_key=ExcelConfig.DataConfig
        #run_list第1个用例，用例，key获取values
        url=ConfigYaml().get_config_url()+run_list[0][data_key.url] #请求URL
        print(url)
        case_id = run_list[0][data_key.case_id] #用例ID
        case_model = run_list[0][data_key.case_model] #模块
        case_name = run_list[0][data_key.case_name] #接口名称
        pre_exec = run_list[0][data_key.pre_exec] #前置条件
        method = run_list[0][data_key.method] #请求类型
        params_type = run_list[0][data_key.params_type] #请求参数类型
        params = run_list[0][data_key.params] #请求参数
        expect_result = run_list[0][data_key.expect_result] #预期结果
        # actual_result = run_list[0][data_key.actual_result] #实际结果，没什么用
        # is_run = run_list[0][data_key.is_run] #是否运行，没什么用
        headers = run_list[0][data_key.headers] #请求头
        cookies = run_list[0][data_key.cookies] #cookies
        code = run_list[0][data_key.code] #状态码
        db_verify = run_list[0][data_key.db_verify] #'数据库验证'

        #（2）、接口请求
        request=Request() #初始化类
        #1）、params 转义json
        if len(str(params).strip()) is not 0:#验证params有没有内容
           params=json.loads(params)
        #2）、method post/get
        if str(method).lower()=="get":
            res=request.get(url,json=params)
        elif str(method).lower()=="post":
            res=request.post(url,json=params)
        else:
            log.error("这是一个错误请求！",method)
        print(res)
"""

# #再完成多个用例的执行
# class TestExcel:
#     #1、增加pytest参数化，注解
#     #2、修改方法参数
#     #3、重构函数内容
#     #4、pytest.main()运行多个用例
# #（1）、初始化信息，如：url，data
#
#     #1、增加pytest参数化，注解
#     @pytest.mark.parametrize("case",run_list)
#
#     #2、修改方法参数
#     def test_run(self,case):
#         #3、重构函数内容(用case替换run_list[0])
#         data_key=ExcelConfig.DataConfig
#         #run_list第1个用例，用例，key获取values
#         # url=ConfigYaml().get_config_url()+run_list[0][data_key.url] #请求URL  替换前
#         url=ConfigYaml().get_config_url()+case[data_key.url] #请求URL  替换后
#         print(url)
#         case_id = case[data_key.case_id] #用例ID
#         case_model = case[data_key.case_model] #模块
#         case_name = case[data_key.case_name] #接口名称
#         pre_exec = case[data_key.pre_exec] #前置条件
#         method = case[data_key.method] #请求类型
#         params_type = case[data_key.params_type] #请求参数类型
#         params = case[data_key.params] #请求参数
#         expect_result = case[data_key.expect_result] #预期结果
#         # actual_result = case[data_key.actual_result] #实际结果，没什么用
#         # is_run = case[data_key.is_run] #是否运行，没什么用
#         headers = case[data_key.headers] #请求头
#         cookies = case[data_key.cookies] #cookies
#         code = case[data_key.code] #状态码
#         db_verify = case[data_key.db_verify] #'数据库验证'
#
#         #（2）、接口请求
#         request=Request() #初始化类
#         #1）、params 转义json
#         if len(str(params).strip()) is not 0:#验证params有没有内容
#            params=json.loads(params)
#
#         #2）、method post/get
#         if str(method).lower()=="get":
#             res=request.get(url,json=params)
#         elif str(method).lower()=="post":
#             res=request.post(url,json=params)
#         else:
#             log.error("这是一个错误请求！",method)
#         print(res)
#
# #再完成多个用例的执行-不使用关联，直接使用token
# class TestExcel:
#     #1、增加pytest参数化，注解
#     #2、修改方法参数
#     #3、重构函数内容
#     #4、pytest.main()运行多个用例
# #（1）、初始化信息，如：url，data
#
#     #1、增加pytest参数化，注解
#     @pytest.mark.parametrize("case",run_list)
#
#     #2、修改方法参数
#     def test_run(self,case):
#         #3、重构函数内容(用case替换run_list[0])
#         data_key=ExcelConfig.DataConfig
#         #run_list第1个用例，用例，key获取values
#         # url=ConfigYaml().get_config_url()+run_list[0][data_key.url] #请求URL  替换前
#         url=ConfigYaml().get_config_url()+case[data_key.url] #请求URL  替换后
#         print(url)
#         case_id = case[data_key.case_id] #用例ID
#         case_model = case[data_key.case_model] #模块
#         case_name = case[data_key.case_name] #接口名称
#         pre_exec = case[data_key.pre_exec] #前置条件
#         method = case[data_key.method] #请求类型
#         params_type = case[data_key.params_type] #请求参数类型
#         params = case[data_key.params] #请求参数
#         expect_result = case[data_key.expect_result] #预期结果
#         # actual_result = case[data_key.actual_result] #实际结果，没什么用
#         # is_run = case[data_key.is_run] #是否运行，没什么用
#         headers = case[data_key.headers] #请求头
#         cookies = case[data_key.cookies] #cookies
#         code = case[data_key.code] #状态码
#         db_verify = case[data_key.db_verify] #'数据库验证'
#
#         # 1、判断headers是否存在，若存在，则进行json转义，若不存在，则无需操作
#         if headers:
#             header=json.loads(headers)
#         else:
#             header=headers
#
#         # 3、判断/增加cookies
#         if cookies:
#             cookie=json.loads(cookies)
#         else:
#             cookie=cookies
#
#         #（2）、接口请求
#         request=Request() #初始化类
#         #1）、params 转义json
#         if len(str(params).strip()) is not 0:#验证params有没有内容
#            params=json.loads(params)
#
#         #2）、method post/get
#         if str(method).lower()=="get":
#             # 2、增加headers
#             # 增加cookies
#             res=request.get(url,json=params,headers=header,cookies=cookie)
#         elif str(method).lower()=="post":
#             res=request.post(url,json=params,headers=header,cookies=cookie)
#         else:
#             log.error("这是一个错误请求！",method)
#         print(res)


#再完成多个用例的执行-动态关联
class TestExcel:
    #1、增加pytest参数化，注解
    #2、修改方法参数
    #3、重构函数内容
    #4、pytest.main()运行多个用例

    def run_api(self,url,method,params=None,header=None,cookie=None):
        """
        发送请求api
        :return:
        """
        # （2）、接口请求
        request = Request()  # 初始化类
        # 1）、params 转义json
        if len(str(params).strip()) is not 0:  # 验证params有没有内容
            params = json.loads(params)

        # 2）、method post/get
        if str(method).lower() == "get":
            # 2、增加headers
            # 增加cookies
            res = request.get(url, json=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=header, cookies=cookie)
        else:
            log.error("这是一个错误请求！", method)
        return res

    def run_pre(self,pre_case):
        #初始化数据
        url = ConfigYaml().get_config_url() + pre_case[data_key.url] #请求URL  替换后
        method = pre_case[data_key.method]  # 请求类型
        params = pre_case[data_key.params]  # 请求参数
        headers = pre_case[data_key.headers]  # 请求头
        cookies = pre_case[data_key.cookies]  # cookies

        # 1、判断headers是否存在，若存在，则进行json转义，若不存在，则无需操作
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = headers
        header=Base.json_pars(headers)

        # 3、判断/增加cookies
        # if cookies:
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies
        cookie=Base.json_pars(cookies)
        res=self.run_api(url,method,params,header)
        print('前置用例执行：',res)
        return res #返回

#（1）、初始化信息，如：url，data

    #1、增加pytest参数化，注解
    @pytest.mark.parametrize("case",run_list)

    #2、修改方法参数
    def test_run(self,case):
        #3、重构函数内容(用case替换run_list[0])
        # data_key=ExcelConfig.DataConfig
        #run_list第1个用例，用例，key获取values
        # url=ConfigYaml().get_config_url()+run_list[0][data_key.url] #请求URL  替换前
        url=ConfigYaml().get_config_url()+case[data_key.url] #请求URL  替换后
        print(url)
        case_id = case[data_key.case_id] #用例ID
        case_model = case[data_key.case_model] #模块
        case_name = case[data_key.case_name] #接口名称
        pre_exec = case[data_key.pre_exec] #前置条件
        method = case[data_key.method] #请求类型
        params_type = case[data_key.params_type] #请求参数类型
        params = case[data_key.params] #请求参数
        expect_result = case[data_key.expect_result] #预期结果
        # actual_result = case[data_key.actual_result] #实际结果，没什么用
        # is_run = case[data_key.is_run] #是否运行，没什么用
        headers = case[data_key.headers] #请求头
        cookies = case[data_key.cookies] #cookies
        code = case[data_key.code] #状态码
        db_verify = case[data_key.db_verify] #'数据库验证'

        # 1、验证前置条件
        if pre_exec: #判断存在，那么就执行，#判断不存在，就不需要往下执行
            pass
        # 2、找到执行用例
            # 前置测试用例
            pre_case = data_init.get_case_pre(pre_exec)
            print("前置条件信息：",pre_case)
            pre_res=self.run_pre(pre_case)
            headers,cookies=self.get_correlation(headers,cookies,pre_res)

        header = Base.json_pars(headers)
        cookie = Base.json_pars(cookies)
        res = self.run_api(url, method, params, header,cookie)
        print('测试用例执行：', res)

        #Allure测试报告
        # sheet名称 feature 作为‘一级标签’
        allure.dynamic.feature(sheet_name)
        # 模块 story 作为‘二级标签’
        allure.dynamic.story(case_model)
        # 用例ID + 接口名称 作为‘title’
        allure.dynamic.title(case_id+case_name)

        # 请求URL 请求类型 期望结果 实际结果 作为‘描述’
        # allure.dynamic.description(url+method+expect_result+res) #若直接运行，是有问题的
        #改为如下：
        # desc="请求URL:{},请求类型:{},期望结果:{},实际结果:{}".format(url,method,expect_result,res)
        # desc="请求URL:{} <Br/>请求类型:{}<Br/>期望结果:{}<Br/>实际结果:{}".format(url,method,expect_result,res)
        desc="<font color='red'>请求URL:</font>{}<Br/>" \
             "<font color='red'>请求类型:</font>{}<Br/>" \
             "<font color='red'>期望结果:</font>{}<Br/>" \
             "<font color='red'>实际结果:</font>{}".format(url,method,expect_result,res)
        allure.dynamic.description(desc)

        #断言验证
        #验证如下内容：验证码、返回结果内容、数据库相关的结果的验证
        #断言-验证状态码
        assert_util=AssertUtil()
        assert_util.assert_code(int(res["code"]),int(code))

        #断言-验证返回结果内容
        assert_util.assert_in_body(str(res["body"]),str(expect_result))

        #断言-数据库结果断言
        #这部分，已在‘Base.py’封装好了
        # from common.Base import init_db
        #
        # #1、初始化数据库
        # sql=init_db("db_1")
        #
        # #2、查询sql、excel定义好的
        # db_res=sql.fetchone(db_verify)
        # log.debug("数据库查询结果:{}".format(str(db_res))) #format-
        #
        # #3、数据库的结果与接口返回的结果验证
        # #（1）获取数据库结果的key
        # verify_list=list(dict(db_res).keys())
        # #（2）根据key，获取数据框结果，接口结果
        # for line in verify_list:
        #     res_line=res["body"][line] #获取接口的结果
        #     res_db_line=dict(db_res)[line] #获取数据库的结果
        #
        #     #（3）验证
        #     assert_util.assert_body(res_line,res_db_line)


        # # 1、判断headers是否存在，若存在，则进行json转义，若不存在，则无需操作
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = headers
        #
        # # 3、判断/增加cookies
        # if cookies:
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies

        # #（2）、接口请求
        # request=Request() #初始化类
        # #1）、params 转义json
        # if len(str(params).strip()) is not 0:#验证params有没有内容
        #    params=json.loads(params)
        #
        # #2）、method post/get
        # if str(method).lower()=="get":
        #     # 2、增加headers
        #     # 增加cookies
        #     res=request.get(url,json=params,headers=header,cookies=cookie)
        # elif str(method).lower()=="post":
        #     res=request.post(url,json=params,headers=header,cookies=cookie)
        # else:
        #     log.error("这是一个错误请求！",method)
        # print(res)

# TestExcel().test_run()

    #动态关联：#4、定义关联的公共方法
    def get_correlation(self,headers,cookies,pre_res):
        """
        关联
        :param headers:
        :param cookies:
        :param pre_res:
        :return:
        """
        #1、验证是否有关联
        headers_para,cookies_para=Base.params_find(headers,cookies) #这种赋值的写法，头回见

        #2、有关联，执行前置用例，获取结果
        if len(headers_para):#headers
            headers_data=pre_res["body"][headers_para[0]]
        #3、结果替换
            headers=Base.res_sub(headers,headers_data) #headers-要传的信息，headers_data-要替换的内容

        if len(cookies_para):#cookies
            cookies_data=pre_res["body"][cookies_para[0]]
        #3、结果替换
            cookies=Base.res_sub(headers,cookies_data)
        return headers,cookies


#4、pytest.main()运行多个用例
if __name__ == '__main__':
    # pass
    report_path=config.get_report_path()+os.sep+"result"
    report_html_path=config.get_report_path()+os.sep+"html"
    # pytest.main()
    # pytest.main(["-s","test_excel_case.py","--alluredir","./report/result"])
    pytest.main(["-s","test_excel_case.py","--alluredir",report_path])

    Base.allure_report(report_path,report_html_path)
    # Base.allure_report("./report/result","report/html")

    # Base.send_mail(title='接口测试报告结果',content=report_html_path)



#固定headers请求
#现在执行第2个用例，用例ID：info_2，直接使用token'{"Authorization":"JWT直接复制、粘贴token"}'
#1、判断headers是否存在，若存在，则进行json转义，若不存在，则无需操作
#2、增加headers
#3、判断/增加cookies
#4、发送请求


#动态关联
#1、验证前置条件
#if pre_exec:
#   pass

#2、找到执行用例

#3、发送请求，获取需要前置的用例结果
#发送获取前置测试用例、用例结果
#数据初始化，get/post，重构代码

#4、替换headers变量【核心】
#1、验证请求中是否有‘${}$’，返回${}$中的内容
#2、根据内容（如：token），查询，前置条件测试用例返回接口token=值
#3、根据变量结果内容，替换

#此步骤是是用了‘关联’的操作【以下只是演练】
#1、验证请求中是否有‘${}$’，返回${}$中的内容
# str1='{"Authorization":"JWT ${token}$"}'  #目的是找到${token}$中的内容，如：token
# if "${" in str1:
#     print('判断、找到此内容：',str1) #并返回所找到的内容，再使用正则表达式提取
#
# import re #导入正则表达式库
# pattern=re.compile('\${(.*)}\$')
# re_res=pattern.findall(str1)
# print('正则表达式匹配到的内容：',re_res) #结果：['token'] 返回的是一个列表
# print('正则表达式匹配到的内容：',re_res[0]) #结果：['token'] 返回的是一个列表，所以还得加个下标
#
#
# #2、根据内容（如：token），查询，前置条件测试用例返回接口token=值
# token="123" #假设，我们已经获取到了上一个用例返回的token值
#
# #3、根据变量结果内容，替换
# res=re.sub(pattern,token,str1)
# print('替换后的结果：',res)

#5、发送请求


#以下是真正运用在代码之中
#1、定义查询的公共方法
#2、定义替换的公共方法
#3、定义验证请求中是否有‘${}$’，返回${}$中的内容的公共方法
#4、定义关联的公共方法


































