
#-------------------------------考核表测试用例模块的封装-------------------------------
import unittest
from ddt import ddt,data
from dingding_send_request_int.send_request_dingding_int import * #导入发送请求模块中的所有内容
from dingding_test_data_int.dingding_excel_data_int.xlrd_openpyxl_excel_dingding import * #导入该模块中的所有内容
import logging
import time #时间戳
import warnings #警告模块
import os

kkk=int(time.time()) #创建时间戳(整数类型，去掉小数点)【只运行一次，全局变量】
# print('时间戳：',kkk)

box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_考核表.xlsx','考核表接口') #本地文件运行
# box_excel=Xlrd_Write_Excel('./dingding_test_data/dingding_excel_data/ddt_data_考核表.xlsx','考核表接口') #主函数运行
testData=box_excel.read_excel()
print('读取Excel表格中数据的结果:',testData)

# print('---------------------------------------------------------------------------------------开始执行考核表接口测试用例---------------------------------------------------------------------------------------')
print() #换行

@ddt #数据驱动
class Test_case(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) #此方法治标不治本，只是隐藏了‘警告信息’

    @data(*testData) #@data把列表testData中每一行字典数据分离开来
    def test_case_d_assessment_group(self,data):#传入data数据
        logging.info('--------------test_case_d_assessment_group_'+str(data['id'])+'--------------')

        #读取文件
        with open('../dingding_json_data/dingding_json_data.json', 'r',encoding='utf-8') as r_json:
            json_data=json.load(r_json) #读取上个接口响应的数据

        #写入文件
        def write_function(public_methods):
            #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
            with open('../dingding_json_data/dingding_json_data.json', 'w') as w_json:
                json.dump(public_methods, w_json)

        time.sleep(0.5) #每条用例等待0.5秒（防止请求速度过快，导致响应不及时，从而报异常）

        #【注意：数据初始化（钉钉版绩效，无法进行了，目前先这样吧】
        global add_edit_assessment_group,assessment_group_total  #全局变量(不起作用)
        res = Request().send_request(data,json_data)  #发送请求，并返回响应的结果
        result = res.json()  #转化为json格式
        print('excel接口响应返回数据-result：', result)

        if int(data['api_num1']) == 1:
            if int(result['code']) == 1:
                if len(result['data']['list'])==0:
                    print('未添加考评组主管理人员')
                    box_excel.write_excel(int(data['id']) + 1, 11,str(result)) #把响应返回的全部结果，逐一写入到excel表中‘response_result’
                    box_excel.write_excel(int(data['id']) + 1, 12,str(result['code'])) #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
                    box_excel.write_excel(int(data['id']) + 1, 14, '用例已中断')
                    os._exit(0) #结束整个程序

        if int(data['api_num1'])==2:
            #维度配置数组列表
            dimension_data='[{"name":"量化指标A","index_type":1,"index_num":0,"weight_type":0,"all_dimension_index_weight":0,"dimension_weight":100,"total_weight":0,"target_index":1,"index":[{"id":"0","custom":1,"type": 1,"name": "指标1","per_remark": "今天是个下雨天，天气还有点冷","remark": "需要注意穿衣保暖，不要冻感冒了","target": "100","result_type":"supervisor","result_employee_id":1,"unit": "光年","weight":50,"reviewer_id":35,"need":0,"enable_ds": 0,"index_level_id": "","point_limit": 0,"record_ids": [24]}]},{"name": "非量化指标B","index_type": 2,"dimension_weight": 100,"index_num": 0,"weight_type": "","target_index": 1,"index": [{"id": 0,"custom": 1,"type": 2,"name": "指标2","per_remark": "明天的天气不知是个什么状况","remark": "不管明天的天气是个啥状况，总之，吃饱穿暖就对了","target": "","unit": "","point_limit": "","weight": "50","result_type": "none","index_level_id": "","result_employee_id": "","result_employee_name": "","reviewer_id": "","reviewer_name": "","record_ids": [],"need": 0}]}]'

            #流程数组列表
            process_array='{"type": 1,"process_scoring":["target", "execution", "score_supervisor", "review", "cc"],"process_index": ["target", "confirm", "execution", "score", "review", "cc"],"target": {"enable":1,"type": 2,"action": {"result_source": 1,"reviewer": 1},"multi_executor": 1,"manager_level": 1,"employee_ids": []},"confirm": {"enable": 1,"confirmor": [{"type": 1,"manager_level": 1,"multi_executor": 2,"action": ["index","transfer"],"employee_ids": []}],"unique":0},"execution": {"enable": 1},"score_self": {"enable": 0,"weight": 0,"action": ["comment","summary"],"rating": 0,"unique": 0},"score_mutual": {"enable": 0},"score_supervisor": {"enable": 1,"unique": 0,"supervisor": [{"type": 1,"manager_level": 1,"supervisor_confirm": 1,"role_name": "","employee_ids":[],"weight": 100,"multi_executor": 2,"rule": 1,"action": ["comment"],"rating": 0,"transfer": 1}]},"special_scorer": {"enable":0,"action": ["comment","summary"]},"review": {"enable": 1,"unique": 0,"reviewer": [{"type": 1,"action": ["transfer","refuse"],"manager_level": 1,"supervisor_confirm": 1,"multi_executor": 2,"employee_ids":[],"role_name": ""}]},"cc": {"enable": 1,"employee": {"type": 1,"manager_level": 1,"employee_ids":[],"role_name": "","condition":1}}}'

            #考评组配置
            evaluation_group_configuration='{"index_score": {"action":["comment","summary"]}}'

            #新建编辑考评组-请求参数
            if int(data['api_num2'])==0:#新建
                performance_evaluation_data={"name":"自动创建考评表"+str(kkk),"cycle_type":1,"manager_ids_code":"","employee_ids_code":"26,34","calc_type":1,"calc_dimension":0,"dimension":dimension_data,"process":process_array,"config":evaluation_group_configuration,"auto_move":1}

                write_function(performance_evaluation_data)

                # box_excel.write_excel(int(data['id'])+1,9,str(performance_evaluation_data)) #把设计好的数据写入Excel（写入本行）

            if int(data['api_num2'])==2:#编辑
                assessment_group_total = result['data']['total'] #获取考评组列表总数
                performance_evaluation_data={"id":result['data']['list'][assessment_group_total-1]['id'],"name":"自动创建考评表(编辑)"+str(kkk),"cycle_type": 1,"manager_ids_code": "","employee_ids_code": "26,34","calc_type": 1, "calc_dimension": 0,"dimension": dimension_data, "process": process_array,"config": evaluation_group_configuration,"auto_move":1}

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(performance_evaluation_data)

                # box_excel.write_excel(int(data['id'])+2,9,str(add_edit_assessment_group)) #给下一行写入数据(覆盖)

            if int(data['api_num2'])==3:
                assessment_group_total = result['data']['total']  #获取考评组列表总数
                performance_evaluation_data={"id":result['data']['list'][assessment_group_total-1]['id']} #考评组ID

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(performance_evaluation_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(details_of_assessment_section))  #给下一行写入数据(覆盖)

            if int(data['api_num2'])==5:
                #只删除被考核人为空的考评表
                for i in range(0,int(result['data']['total'])):
                    if result['data']['list'][i]['employee_num']==0:
                        performance_evaluation_data={"id":result['data']['list'][i]['id']} #考评组ID

                        # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                        write_function(performance_evaluation_data)

                        # box_excel.write_excel(int(data['id']) + 2, 9, str(details_of_assessment_section))  #给下一行写入数据(覆盖)
                        break

            if int(data['api_num2'])==7:
                assessment_group_total = result['data']['total']  #获取考评组列表总数（倒数第1个考评组ID）
                performance_evaluation_data={"employee_id_code":"all","group_id":result['data']['list'][assessment_group_total - 1]['id'],"raw_data":0} #拼接body数据，用于预览全员
                # preview2={"employee_id":52,"group_id":result['data']['list'][assessment_group_total - 2]['id'],"raw_data":0} #拼接body数据，用于预览单个员工

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(performance_evaluation_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(preview1))  #给下一行写入数据(覆盖)

        box_excel.write_excel(int(data['id'])+1,11,str(result))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
        box_excel.write_excel(int(data['id'])+1,12,str(result['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’

        #对断言进行异常捕获，断言正常的回写用例已通过，断言异常的回写用例未通过
        try:
            self.assertEqual(int(result['code']),int(data['expected_result']))

            #把响应结果数据写入指定位置
            if int(data['api_num1'])==1:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 10, str({"code:" + str(result['code']),"msg:" + str(result['msg']),"name:" + str(result['data']['list'][0]['name'])}))
            if int(data['api_num1'])==2:
                if int(data['api_num2'])==1 or int(data['api_num2'])==11:
                    box_excel.write_excel(int(data['id']) + 1 ,10, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"result:"+str(result['data']['result'])}))
                if int(data['api_num2'])==0 or int(data['api_num2'])==2 or int(data['api_num2'])==3:
                    assessment_group_total=result['data']['total'] #获取考评组列表总数
                    box_excel.write_excel(int(data['id']) + 1, 10, str({"id:"+str(result['data']['list'][assessment_group_total-1]['id']),"name:"+str(result['data']['list'][assessment_group_total-1]['name'])}))
                if int(data['api_num2'])==4:
                    box_excel.write_excel(int(data['id']) + 1, 10, str({"code:" + str(result['code']),"msg:"+str(result['msg']),"name:"+str(result['data']['name']),"id:"+str(result['data']['id'])})) #给本行写入响应结果数据(覆盖)
                if int(data['api_num2'])==5 or int(data['api_num2'])==7:
                    box_excel.write_excel(int(data['id']) + 1, 10, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"name:" + str(result['data']['list'][0]['name'])}))  #给本行写入响应结果数据(覆盖)
                if int(data['api_num2'])==6:
                    box_excel.write_excel(int(data['id']) + 1, 10, str({"code:" + str(result['code']),"msg:"+str(result['msg']),"list:"+str(result['data']['list'])})) #给本行写入响应结果数据(覆盖)
                if int(data['api_num2'])==8:
                    box_excel.write_excel(int(data['id']) + 1, 10, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"id:"+str(result['data']['list'][0]['employee']['id']),"name:"+str(result['data']['list'][0]['employee']['name'])}))  #给本行写入响应结果数据(覆盖)
                if int(data['api_num2'])==9:
                    box_excel.write_excel(int(data['id']) + 1, 10, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))  #给本行写入响应结果数据(覆盖)


        except AssertionError as f: #断言异常
            # box_excel.write_excel(int(data['id']) + 1, 12,0) #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
            box_excel.write_excel(int(data['id'])+1,14,'用例未通过') #注意：写入的文件，必须是处于关闭状态，否则程序无法写入
            raise f #当断言时，会显示出失败的、成功的数量

        else: #否则，断言是正常的
            # box_excel.write_excel(int(data['id']) + 1, 12,1) #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
            box_excel.write_excel(int(data['id'])+1,14,'用例已通过')

#调试运行
if __name__ == '__main__':
    unittest.main()

#在Excel中的数据
#运行前（真正运行,编辑时的数据）：{'cate_id': 16, 'name': '修改指标分类名称1644919283'}
#运行后（重新写入的最新数据，提供下次运行使用）：{'cate_id': 16+1, 'name': '修改指标分类名称1644919453'}



