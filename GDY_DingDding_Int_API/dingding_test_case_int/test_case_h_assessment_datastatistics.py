
#-------------------------------数据统计(数据中台)测试用例模块的封装-------------------------------
import unittest
from ddt import ddt,data
from dingding_send_request.send_request_dingding import * #导入发送请求模块中的所有内容
from dingding_test_data.dingding_excel_data.xlrd_openpyxl_excel_dingding import * #导入该模块中的所有内容
import logging
import time #时间戳
import warnings #警告模块
import os
import datetime #获取'年月日时分秒'组合数据

kkk=int(time.time()) #创建时间戳(整数类型，去掉小数点)【只运行一次，全局变量】
# print('时间戳：',kkk)

# box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_数据统计(数据中台).xlsx','数据统计(数据中台)') #本地文件运行
box_excel=Xlrd_Write_Excel('./dingding_test_data/dingding_excel_data/ddt_data_数据统计(数据中台).xlsx','数据统计(数据中台)') #主函数运行
testData=box_excel.read_excel()
print('读取Excel表格中数据的结果:',testData)

# print('---------------------------------------------------------------------------------------开始执行数据统计(数据中台)接口测试用例---------------------------------------------------------------------------------------')
print() #换行

now_time1=int(datetime.datetime.now().strftime('%Y')) #年

@ddt #数据驱动
class Test_case(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) #此方法治标不治本，只是隐藏了‘警告信息’

    @data(*testData) #@data把列表testData中每一行字典数据分离开来
    def test_case_h_assessment_datastatistics(self,data):#传入data数据
        logging.info('--------------test_case_h_assessment_datastatistics_'+str(data['id'])+'--------------')

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

        time.sleep(0.5) #等待0.5秒（防止请求速度过快，导致响应不及时，从而报异常）

        #【注意：数据初始化（钉钉版绩效，无法进行了，目前先这样吧】
        res = Request().send_request(data,json_data)  #发送请求，并返回响应的结果
        result = res.json()  #转化为json格式
        print('excel接口响应返回数据-result：', result)

        """
        if int(data['api_num1']) == 3:
            tag_list_total = result['data']['total']  #获取统计分类列表总数
            for i in range(0, tag_list_total - 1):
                if int(i) <= int(tag_list_total - 1):
                    if str(result['data']['list'][i]['name']) == str(data['body']):
                        print('新增统计分类成功！')
                else:
                    print('新增统计分类失败!')
        """

        if int(data['api_num1'])==1:
            if int(data['api_num2'])==1:
                statistical_classification_data={"name":"国家"+str(kkk),"type":1,"calc_type":1,"employee_ids_code":'[]',"tag_ids[0]":str(result['data']['list'][0]['id'])} #拼接统计分类数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(statistical_classification))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                statistical_classification_data={"id":result['data']['id']} #统计分类详情

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(details_of_statistical_classification))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 2:
            if int(data['api_num2'])==1:
                statistical_classification_data=str(result['data']['list'][0]['id']) #拼接统计分类数据("tag_ids[0]":str(result['data']['list'][0]['id']))

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(tag_data))  #给下一行写入数据(覆盖)
            if int(data['api_num2']) == 2:
                json_dat_get_alone = read_function()  #调用读取文件函数

                statistical_classification_data = {"id": result['data']['list'][int(result['data']['total'])-1]['id'],"name": "国家(更新)" + str(kkk), "type": 1, "calc_type": 1,"employee_ids_code": '[]',"tag_ids[0]":json_dat_get_alone}  #拼接统计分类数据（编辑）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(statistical_classification))  #给下一行写入数据(覆盖)
            if int(data['api_num2']) == 3:
                statistical_classification_data={"id":result['data']['id']} #拼接数据-统计分类详情

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(statistical_classification))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 3:
            if int(data['api_num2']) == 1:
                statistical_classification_data={"id": result['data']['list'][0]['id']} #删除统计分类数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 9,str({"id": result['data']['list'][0]['id']}))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 4:
            if int(data['api_num2']) == 0:
                statistical_classification_data = {'tag[0][tag_name]': '广东省' + str(kkk), 'tag[1][tag_name]': '福建省' + str(kkk),'tag[2][tag_name]': '浙江省' + str(kkk)}  #新增标签数据

                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 1, 9, str(statistical_classification_data))  #把设计好的数据写入Excel（写入本行）

        if int(data['api_num1']) == 5:
            if int(data['api_num2']) == 1:
                statistical_classification_data={"id":result['data']['list'][int(result['data']['total'])-1]['id'],"time_type":2,"year":int(now_time1)} #拼接数据-展示年 季度 月 统计数据(默认：年)

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(statistical_classification))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 6:
            if int(data['api_num2']) == 1:
                statistical_classification_data={"cate_id":result['data']['list'][int(result['data']['total'])-1]['id'],"year":str(now_time1),"year_config":'{"month_01": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list":[]},"month_02": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_03": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_04": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_05": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_06": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_07": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_08": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_09": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_10": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_11": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []},"month_12": {"base": "0.00","target": "0.00","challenges": "0.00","result": "0.00","calc_type": 1,"source_type": 1,"manual": "0.00","performance": "0.00","index_list": []}}'} #保存年度统计配置

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(statistical_classification))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 7:
            if int(data['api_num2']) == 1:
                statistical_classification_data={"cate_id":result['data']['list'][int(result['data']['total'])-1]['id'],"year":str(now_time1)} #拼接数据-展示年 季度 月 统计数据(默认：年)

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(statistical_classification))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 8:
            if int(data['api_num2']) == 1:
                statistical_classification_data={"cate_id":result['data']['list'][int(result['data']['total'])-1]['id']} #查询分类有哪些年-数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(statistical_classification))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 9:
            if int(data['api_num2']) == 1:
                statistical_classification_data={"package_id":result['data']['list'][0]['id']} #考核包考核统计-数据（固定选择第1个考核包）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(statistical_classification_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(statistical_classification))  #给下一行写入数据(覆盖)

        if int(data['api_num1']) == 10:
            if int(data['api_num2']) == 1:
                statistical_classification_data={"year":int(now_time1),"page":1,"page_size":100} #获取用户年度统计-数据

                write_function(statistical_classification_data)
                # box_excel.write_excel(int(data['id']) + 1, 8, str(statistical_classification_data))  #给本行写入数据(覆盖)

        box_excel.write_excel(int(data['id'])+1,12,str(result))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
        box_excel.write_excel(int(data['id'])+1,13,str(result['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’

        #对断言进行异常捕获，断言正常的回写用例已通过，断言异常的回写用例未通过
        try:
            self.assertEqual(int(result['code']),int(data['expected_result']))

            #把响应结果数据写入指定位置
            if int(data['api_num1'])==1:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])})) #标签列表响应数据
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"name:"+str(result['data']['name']),"id:"+str(result['data']['id'])})) #新增统计分类
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"name:"+str(result['data']['name']),"id:"+str(result['data']['id'])})) #统计分类详情
            if int(data['api_num1'])==2:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])})) #标签列表响应数据
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])})) #统计分类列表响应数据
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"name:"+str(result['data']['name']),"id:"+str(result['data']['id'])})) #更新统计分类
                if int(data['api_num2'])==4:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"name:"+str(result['data']['name']),"id:"+str(result['data']['id'])})) #统计分类详情
            if int(data['api_num1'])==3:
               if int(data['api_num2'])==1:
                   box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])})) #统计分类列表响应数据
               if int(data['api_num2']) == 2:
                   box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg'])}))
               if int(data['api_num2']) == 3:
                   box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"list:"+str(result['data']['list'])}))
            if int(data['api_num1'])==4:
               if int(data['api_num2'])==0:
                   box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:"+str(result['data']['total'])}))
               if int(data['api_num2'])==1:
                   box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
               if int(data['api_num2'])==2:
                   box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:"+str(result['data']['total'])}))
            if int(data['api_num1']) == 5:
                if int(data['api_num2']) == 1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2']) == 2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1']) == 6:
                if int(data['api_num2']) == 1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:" + str(result['data']['total'])}))
                if int(data['api_num2']) == 2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"list:"+str(result['data']['list'])}))
            if int(data['api_num1']) == 7:
                if int(data['api_num2']) == 1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:" + str(result['data']['total'])}))
                if int(data['api_num2']) == 2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg'])}))
            if int(data['api_num1']) == 8:
                if int(data['api_num2']) == 1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:" + str(result['data']['total'])}))
                if int(data['api_num2']) == 2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"data:"+str(result['data'])}))
            if int(data['api_num1']) == 9:
                if int(data['api_num2']) == 1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:" + str(result['data']['total'])}))
                if int(data['api_num2']) == 2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1']) == 10:
                if int(data['api_num2']) == 1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:" + str(result['data']['total'])}))
                if int(data['api_num2']) == 2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:" + str(result['data']['total'])}))

        except AssertionError as f: #断言异常
            # box_excel.write_excel(int(data['id']) + 1, 13, 0)  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
            box_excel.write_excel(int(data['id'])+1,15,'用例未通过') #注意：写入的文件，必须是处于关闭状态，否则程序无法写入
            raise f #当断言时，会显示出失败的、成功的数量

        else: #否则，断言是正常的
            # box_excel.write_excel(int(data['id']) + 1, 13,1) #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
            box_excel.write_excel(int(data['id'])+1,15,'用例已通过')

#调试运行
if __name__ == '__main__':
    unittest.main()

#在Excel中的数据
#运行前（真正运行,编辑时的数据）：{'cate_id': 16, 'name': '修改指标分类名称1644919283'}
#运行后（重新写入的最新数据，提供下次运行使用）：{'cate_id': 16+1, 'name': '修改指标分类名称1644919453'}
#列表-用中括号[]，嵌套时，需要单引号
#字典(json)-用大括号{}，嵌套时，无需单引号














































