
#-------------------------------导入导出测试用例模块的封装-------------------------------
import unittest
from ddt import ddt,data
from dingding_send_request.send_request_dingding import * #导入发送请求模块中的所有内容
from dingding_test_data.dingding_excel_data.xlrd_openpyxl_excel_dingding import * #导入该模块中的所有内容
import logging
import time #时间戳
import warnings #警告模块
import datetime #获取'年月日时分秒'组合数据

kkk=int(time.time()) #创建时间戳(整数类型，去掉小数点)【只运行一次，全局变量】
# print('时间戳：',kkk)

# box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_导入导出.xlsx','导入导出接口') #本地文件运行
box_excel=Xlrd_Write_Excel('./dingding_test_data/dingding_excel_data/ddt_data_导入导出.xlsx','导入导出接口') #主函数运行-测试换境
testData=box_excel.read_excel()
print('读取Excel表格中数据的结果:',testData)

# print('---------------------------------------------------------------------------------------开始执行导入导出接口测试用例---------------------------------------------------------------------------------------')
print() #换行

now_time1=int(datetime.datetime.now().strftime('%Y')) #年
now_time2=int(datetime.datetime.now().strftime('%m')) #月
now_time3=int(datetime.datetime.now().strftime('%d')) #日

now_time4=int(datetime.datetime.now().strftime('%H')) #时
now_time5=int(datetime.datetime.now().strftime('%M')) #分
now_time6=int(datetime.datetime.now().strftime('%S')) #秒


now_time_all=str(now_time1)+str(now_time2)+str(now_time3)+str(now_time4)+str(now_time5)+str(now_time6) #年月日时分秒
now_time_all1=str(now_time1)+str(now_time2)+str(now_time3) #年月日
now_time_all2=str(now_time4)+str(now_time5)+str(now_time6) #时分秒

# print('年月日时分秒：',now_time_all)

@ddt #数据驱动
class Test_case(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) #此方法治标不治本，只是隐藏了‘警告信息’

    @data(*testData) #@data把列表testData中每一行字典数据分离开来
    def test_case_i_import_and_export(self,data):#传入data数据
        logging.info('--------------test_case_i_import_and_export_'+str(data['id'])+'--------------')

        #读取文件
        def read_function():
            with open('./dingding_json_data/dingding_json_data.json', 'r', encoding='utf-8') as r_json:
                json_data1 = json.load(r_json)  #读取上个接口响应的数据
            return json_data1  #返回响应数据

        json_data = read_function()  #调用读取文件函数

        #写入文件
        def write_function(public_methods):
            #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
            with open('./dingding_json_data/dingding_json_data.json', 'w') as w_json:
                json.dump(public_methods, w_json)

        time.sleep(0.5)  #等待0.5秒（防止请求速度过快，导致响应不及时，从而报异常）

        #【注意：数据初始化（钉钉版绩效，无法进行了，目前先这样吧】
        global employee_status,is_official #全局变量(不起作用)
        global res
        res = Request().send_request(data,json_data)  #发送请求，并返回响应的结果
        # result = res.json()  #转化为json格式
        # print('excel接口响应返回数据-result：', result)

        #给下一行写入数据
        if int(data['api_num1'])==1:
            if int(data['api_num2'])==1:
                with open(os.path.join(os.path.dirname(os.path.abspath("__file__")), "指标导入模板"+str(now_time_all)+".xlsx"), "wb") as f:
                    f.write(res.content)
            if int(data['api_num2'])==2:
                with open(os.path.join(os.path.dirname(os.path.abspath("__file__")), "数据中台导入模板-"+str(now_time_all)+".xlsx"), "wb") as f:
                    f.write(res.content)
            if int(data['api_num2'])==3:
                with open(os.path.join(os.path.dirname(os.path.abspath("__file__")), "指标下载("+str(now_time_all1)+"_"+str(now_time_all2)+").xlsx"), "wb") as f:
                    f.write(res.content)
            if int(data['api_num2'])==4:
                with open(os.path.join(os.path.dirname(os.path.abspath("__file__")), str(now_time1)+"年度考核统计("+str(now_time_all)+").xlsx"), "wb") as f:
                    f.write(res.content)
            if int(data['api_num2'])==5:
                with open(os.path.join(os.path.dirname(os.path.abspath("__file__")), str(now_time1)+"年"+str(now_time2)+"月"+str(now_time3)+"日绩效考核执行计划数据（"+str(now_time_all)+"）.xlsx"), "wb") as f:
                    f.write(res.content)
            if int(data['api_num2'])==6:
                with open(os.path.join(os.path.dirname(os.path.abspath("__file__")), str(now_time1)+"年"+str(now_time2)+"月"+str(now_time3)+"日绩效考核考核结果（"+str(now_time_all)+"）.xlsx"), "wb") as f:
                    f.write(res.content)
            if int(data['api_num2'])==7:
                with open(os.path.join(os.path.dirname(os.path.abspath("__file__")), str(now_time1)+"年"+str(now_time2)+"月"+str(now_time3)+"日绩效考核明细（"+str(now_time_all)+"）.xlsx"), "wb") as f:
                    f.write(res.content)


        if int(data['api_num1'])==2:
            result = res.json()  #转化为json格式

            if int(data['api_num2'])==0:
                import_and_export_data={'cate_name':str(result['data']['list'][0]['name'])} #导出指标数据
                write_function(import_and_export_data)

            if int(data['api_num2'])==1:
                import_and_export_data={'token':str(result['data']['token'])} #导出指标数据
                write_function(import_and_export_data)

            if int(data['api_num2'])==3:
                import_and_export_data={'token':str(result['data']['token']),'year':int(now_time1)} #导出用户年度考核统计数据
                write_function(import_and_export_data)

            if int(data['api_num2'])==4:
                import_and_export_data =str(result['data']['token'])  #用于‘导出执行计划’数据1
                write_function(import_and_export_data)

            if int(data['api_num2'])==5:
                export_index22 = read_function()  #调用读取文件函数
                import_and_export_data ={'token':str(export_index22),'package_id':result['data']['list'][0]['package_id'],'employee_ids_code':'["26"]'}  #用于‘导出执行计划’数据2（被考核人-刘俊华）

                write_function(import_and_export_data)


            if int(data['api_num2'])==6:
                import_and_export_data =str(result['data']['token'])  #用于‘考核结果导出’数据1

                write_function(import_and_export_data)

            if int(data['api_num2'])==7:
                export_index22 = read_function()  #调用读取文件函数
                import_and_export_data ={'token':str(export_index22),'package_id':result['data']['list'][0]['package_id']}  #用于‘考核结果导出’数据2

                write_function(import_and_export_data)

            if int(data['api_num2'])==8:
                import_and_export_data =str(result['data']['token'])  #用于‘导出考核明细’数据1

                write_function(import_and_export_data)

            if int(data['api_num2'])==9:
                export_index22 = read_function()  #调用读取文件函数

                import_and_export_data ={'token':str(export_index22),'package_id':result['data']['list'][0]['package_id']}  #用于‘导出考核明细’数据2

                write_function(import_and_export_data)

            box_excel.write_excel(int(data['id'])+1,12,str(result))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
            box_excel.write_excel(int(data['id'])+1,13,str(result['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’

            #对断言进行异常捕获，断言正常的回写用例已通过，断言异常的回写用例未通过
            try:
                self.assertEqual(int(result['code']),int(data['expected_result']))

                if int(data['api_num1'])==2:
                    if int(data['api_num2'])==0:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:"+str(result['data']['total']),"name:"+str(result['data']['list'][0]['name'])}))
                    if int(data['api_num2'])==1:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "expire:" + str(result['data']['expire']),"token:"+str(result['data']['token'])}))
                    if int(data['api_num2'])==3:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "expire:" + str(result['data']['expire']),"token:"+str(result['data']['token'])}))
                    if int(data['api_num2'])==4:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "expire:" + str(result['data']['expire']),"token:"+str(result['data']['token'])}))
                    if int(data['api_num2'])==5:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name']),"msg:"+str(result['msg'])}))
                    if int(data['api_num2'])==6:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "expire:" + str(result['data']['expire']),"token:"+str(result['data']['token'])}))
                    if int(data['api_num2'])==7:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name']),"msg:"+str(result['msg'])}))
                    if int(data['api_num2'])==8:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "expire:" + str(result['data']['expire']),"token:"+str(result['data']['token'])}))
                    if int(data['api_num2'])==9:
                        box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name']),"msg:"+str(result['msg'])}))

            except AssertionError as f: #断言异常的
                box_excel.write_excel(int(data['id'])+1,15,'用例未通过') #注意：写入的文件，必须是处于关闭状态，否则程序无法写入
                raise f #当断言时，会显示出失败的、成功的数量

            else: #否则，断言是正常的
                box_excel.write_excel(int(data['id'])+1,15,'用例已通过')


        # if int(data['api_num1'])==3:#导入指标、导入数据中台数据-接口测试脚本暂不写（目前解决不了）


#调试运行
if __name__ == '__main__':
    unittest.main()

#在Excel中的数据
#运行前（真正运行,编辑时的数据）：{'cate_id': 16, 'name': '修改指标分类名称1644919283'}
#运行后（重新写入的最新数据，提供下次运行使用）：{'cate_id': 16+1, 'name': '修改指标分类名称1644919453'}





