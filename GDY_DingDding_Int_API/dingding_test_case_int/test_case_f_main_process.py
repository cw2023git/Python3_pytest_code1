
#-------------------------------主流程测试用例模块的封装-------------------------------
import unittest
from ddt import ddt,data
from dingding_send_request.send_request_dingding import * #导入发送请求模块中的所有内容
from dingding_test_data.dingding_excel_data.xlrd_openpyxl_excel_dingding import * #导入该模块中的所有内容
import logging
import time #时间戳
import warnings #警告模块

kkk=int(time.time()) #创建时间戳(整数类型，去掉小数点)【只运行一次，全局变量】
# print('时间戳：',kkk)

box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_主流程.xlsx','主流程接口') #本地文件运行
# box_excel=Xlrd_Write_Excel('./dingding_test_data/dingding_excel_data/ddt_data_主流程.xlsx','主流程接口') #主函数运行
testData=box_excel.read_excel()
print('读取Excel表格中数据的结果:',testData)

# print('---------------------------------------------------------------------------------------开始执行主流程接口测试用例---------------------------------------------------------------------------------------')
print() #换行

@ddt #数据驱动
class Test_case(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) #此方法治标不治本，只是隐藏了‘警告信息’

    @data(*testData) #@data把列表testData中每一行字典数据分离开来
    def test_case_f_main_process(self,data):#传入data数据
        logging.info('--------------test_case_f_main_process_'+str(data['id'])+'--------------')

        #读取文件
        with open('../dingding_json_data/dingding_json_data.json', 'r',encoding='utf-8') as r_json:
            json_data=json.load(r_json) #读取上个接口响应的数据

        #写入文件
        def write_function(public_methods):
            #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
            with open('../dingding_json_data/dingding_json_data.json', 'w') as w_json:
                json.dump(public_methods, w_json)

        time.sleep(0.5)  #每条用例等待0.5秒（防止请求速度过快，导致响应不及时，从而报异常）

        #【注意：数据初始化（钉钉版绩效，无法进行了，目前先这样吧】
        global employee_status,is_official #全局变量(不起作用)
        res = Request().send_request(data,json_data)  #发送请求，并返回响应的结果

        result = res.json()  #转化为json格式
        print('excel接口响应返回数据-result：', result)

        #给下一行写入数据
        if int(data['api_num1'])==1:
            if int(data['api_num2'])==1:
                main_process_data={'id':result['data']['list'][0]['id']} #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==2:
            if int(data['api_num2'])==1:
                main_process_data={'id':result['data']['list'][0]['id'],'node_id':1,'submit':1} #目标制定数据(提交)

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id'])+2,9,str(goal_setting)) #给下一行写入数据

        if int(data['api_num1'])==3:
            if  int(data['api_num2'])==1:
                main_process_data={'id':result['data']['list'][0]['id'],'agree':1,'c_node_id':2,'comment':'经过认真细致的斟酌，定的目标基本上问题不大，予以确认同意通过'+str(kkk)+'。'} #目标确认数据（同意）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id'])+2,9,str(target_confirmed)) #给下一行写入数据

        if int(data['api_num1'])==4:
            if int(data['api_num2'])==1:
                main_process_data={'id':result['data']['list'][0]['id'],'single':1} #执行中数据（开始评分）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id'])+2,9,str(in_execution)) #给下一行写入数据

        if int(data['api_num1'])==5:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['id'],'cache':0,'result_info':'[{"result": "20","dimension_key": 0,"index_key": 0,"index_id":'+str('"'+result['data']['flow'][3]['target'][0]['list'][0]['index_id']+'"')+'}]'} #结果值录入数据（提交）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(result_value_entry))  #给下一行写入数据

        if int(data['api_num1'])==6:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['id'],'total_score':100,'is_submit':1,'node_id':5,'point_info':'[{"score": 100,"score_remark": "昨天的天气有点阴沉沉。","dimension_key": '+str(result['data']['flow'][4]['target'][0]['list'][0]['dimension_key'])+',"index_key": '+str(result['data']['flow'][4]['target'][0]['list'][0]['index_key'])+',"index_id": '+'"'+str(result['data']['flow'][4]['target'][0]['list'][0]['index_id'])+'"'+'}]'} #评分-直接上级评分数据（提交）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(grade_direct_superior_rating))  #给下一行写入数据

        if int(data['api_num1'])==7:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['id'],'total_score':100,'is_submit':1,'node_id':6,'point_info':'[{"score": 100,"score_remark": "后天的天气应该会有所好转滴。","dimension_key": '+str(result['data']['flow'][5]['target'][0]['list'][0]['dimension_key'])+',"index_key": '+str(result['data']['flow'][5]['target'][0]['list'][0]['index_key'])+',"index_id": '+'"'+str(result['data']['flow'][5]['target'][0]['list'][0]['index_id'])+'"'+'}]'} #评分-特定指标评分数据（提交）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(grade_direct_superior_rating))  #给下一行写入数据

        if int(data['api_num1'])==8:
            if int(data['api_num2'])==1:
                main_process_data = {'id': str(result['data']['list'][0]['id']),'node_id':6,'comment':'在下苦思冥想之后，仍然决定撤销评分'+str(kkk)+'。'}  #撤销评分数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(cancel_the_score))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==9:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['id'],'total_score':100,'is_submit':1,'node_id':6,'point_info':'[{"score": 100,"score_remark": "后天的天气应该会有所好转滴。","dimension_key": '+str(result['data']['flow'][5]['target'][0]['list'][0]['dimension_key'])+',"index_key": '+str(result['data']['flow'][5]['target'][0]['list'][0]['index_key'])+',"index_id": '+'"'+str(result['data']['flow'][5]['target'][0]['list'][0]['index_id'])+'"'+'}]'} #评分-特定指标评分数据（再一次提交）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(grade_direct_superior_rating))  #给下一行写入数据

        if int(data['api_num1'])==10:
            if  int(data['api_num2'])==1:
                main_process_data={'id':result['data']['list'][0]['id'],'agree':1,'c_node_id':7,'comment':'通过对所评的分数进行了认真思考，认为分数符合实际情况，因此予以确认同意通过'+str(kkk)+'。'} #目标确认数据（同意）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id'])+2,9,str(examine_and_approve)) #给下一行写入数据

        if int(data['api_num1'])==11:
            if int(data['api_num2'])==1:
                main_process_data = {'id': str(result['data']['list'][0]['id']),'change_type':1,'point':250,'comment':'既然无处可逃，不如喜悦'+str(kkk)+'。','ding_msg':1}  #分数等级调整数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(personal_assessment_record_id3))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==12:
            if int(data['api_num2'])==1:
                # reset_flow1={'id':result['data']['list'][0]['id'],'type':1,'node_id':1,'employee_id_code':'["e1e7224"]','comment':'这个重置流程的是‘流程内重置’所进行的操作！'} #重置流程数据（流程内重置）-不可删
                main_process_data={'id':result['data']['list'][0]['id'],'type':2,'overwrite_mode':1,'comment':'这个重置流程的是‘重读维度流程’所进行的操作'+str(kkk)+'！'} #重置流程数据（重读维度流程）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(reset_flow1))  #给下一行写入数据

        if int(data['api_num1'])==13:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据
            if int(data['api_num2'])==2:
                main_process_data={'package_employee_id':result['data']['id'],'index_id':result['data']['dimension'][0]['index'][0]['id'],'dimension_xb':0,'title':'执行计划'+str(kkk),'remark':'学习都是要付出代价的'+str(kkk),'append':[]} #增加执行计划数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(delivery_of_program))  #给下一行写入数据

        if int(data['api_num1'])==14:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id2))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                main_process_data={'action_id':result['data']['dimension'][0]['index'][0]['schedule'][0]['id'],'package_employee_id':result['data']['id'],'index_id':result['data']['dimension'][0]['index'][0]['id'],'dimension_xb':0} #删除执行计划数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(delete_delivery_of_program))  #给下一行写入数据

        if int(data['api_num1'])==15:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据
            if int(data['api_num2'])==2:
                main_process_data={'package_employee_id':result['data']['id'],'index_id':result['data']['dimension'][0]['index'][0]['id'],'dimension_xb':0,'title':'管理记录'+str(kkk),'remark':'无论到哪里，都是一条引以为傲的风景线'+str(kkk)+'.','append':[]} #增加管理记录数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(management_record))  #给下一行写入数据

        if int(data['api_num1'])==16:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id2))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                main_process_data={'track_id':result['data']['dimension'][0]['index'][0]['mamage_record'][0]['id'],'package_employee_id':result['data']['id'],'index_id':result['data']['dimension'][0]['index'][0]['id'],'dimension_xb':0} #删除管理记录数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(delete_delivery_of_program))  #给下一行写入数据

        if int(data['api_num1'])==17:
            if int(data['api_num2'])==1:
                main_process_data = {'package_id': str(result['data']['list'][0]['id']),'search_str':'指标'}  #考核包数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(search_index1))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['list'][0]['pe_id'],'index_id':result['data']['list'][0]['index_id'],'target':'50','unit':'万(编辑'+str(kkk)+')','content':'批量修改目标值-是为了方便、快捷统一修改'+str(kkk)+'。','ding_msg':1} #批量修改目标值数据（目前改一条）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(modify_target_value_data_in_batches))  #给下一行写入数据

        if int(data['api_num1'])==18:
            if int(data['api_num2'])==1:
                main_process_data = {'id': str(result['data']['list'][0]['id']),'employee_id_code':26}  #搜索转交数据-目标制定人（要转出的用户code-目前写的是固定）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(search_over2))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['process']['target'][0]['pe_id'],'node_id':result['data']['process']['target'][0]['node_id'],'from_employee_id_code':str(result['data']['process']['target'][0]['employee_id']),'to_employee_id_code':str(32)} #批量转交目标制定数据（目前改一条）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(batch_transfer_target_setting))  #给下一行写入数据

        if int(data['api_num1'])==19:
            if int(data['api_num2'])==1:
                main_process_data = {'id': str(result['data']['list'][0]['id']),'employee_id_code':24}  #搜索转交数据-管理记录人（要转出的用户code-目前写的是固定）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(search_over3))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['dimension']['record_ids'][0]['pe_id'],'from_employee_id_code':24,'to_employee_id_code':32} #批量转交管理记录人数据（目前改一条）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(batch_transfer_to_management_recorder))  #给下一行写入数据

        if int(data['api_num1'])==20:
            if int(data['api_num2'])==1:
                main_process_data={'id':result['data']['list'][0]['id'],'node_id':1,'submit':1} #目标制定数据(提交)

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id'])+2,9,str(goal_setting)) #给下一行写入数据

        if int(data['api_num1'])==21:
            if  int(data['api_num2'])==1:
                main_process_data={'id':result['data']['list'][0]['id'],'agree':1,'c_node_id':2,'comment':'经过认真细致的斟酌，定的目标基本上问题不大，予以确认同意通过'+str(kkk)+'。'} #目标确认数据（同意）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id'])+2,9,str(target_confirmed)) #给下一行写入数据

        if int(data['api_num1'])==22:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id))  #给下一行写入数据
            if int(data['api_num2'])==2:
                main_process_data={'id':result['data']['id'],'cache':0,'result_info':'[{"result": "20","dimension_key": 0,"index_key": 0,"index_id":'+str('"'+result['data']['flow'][3]['target'][0]['list'][0]['index_id']+'"')+'}]'} #结果值录入数据（提交）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(result_value_entry))  #给下一行写入数据

        if int(data['api_num1'])==23:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id3))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                main_process_data = {'id': str(result['data']['id']),'dimension':'[{"name":"量化指标A","index_type":1,"index_num":0,"weight_type":0,"dimension_weight":100,"total_weight":0,"target_index":1,"index":[{"id":"'+str(result['data']['dimension'][0]['index'][0]['id'])+'","custom":1,"type":1,"name":"指标1('+'编辑'+str(kkk)+')","per_remark":"今天是个下雨天，天气还有点冷('+'编辑'+str(kkk)+')","remark":"需要注意穿衣保暖，不要冻感冒了('+'编辑'+str(kkk)+')","target":"100","unit":"光年","point_limit":0,"weight":50,"result_type":"supervisor","index_level_id":"","result_employee_id":"","result_employee_name":"","reviewer_id":35,"reviewer_name":"刘俊华","record_ids":[24],"mamage_record":[],"schedule":[],"need":0}]},{"name":"非量化指标B","index_type":2,"index_num":0,"weight_type":0,"dimension_weight":100,"total_weight":0,"target_index":1,"index":[{"id":"'+str(result['data']['dimension'][1]['index'][0]['id'])+'","custom":1,"type":2,"name":"指标2('+'编辑'+str(kkk)+')","per_remark":"明天的天气不知是个什么状况('+'编辑'+str(kkk)+')","remark":"不管明天的天气是个啥状况，总之，吃饱穿暖就对了('+'编辑'+str(kkk)+')","target":"","result":null,"result_type":"none","result_employee_id":0,"unit":"","weight":"50","point_limit":0,"reviewer_id":0,"record_ids":[],"need":0,"score_info":[{"id":5,"weight":100,"multi_executor":2,"employees":[{"point":null,"title":"一级部门主管评分：刘水线(100%)","remark":"","employee_id":31,"level":""},{"point":null,"title":"一级部门主管评分：李杰(100%)","remark":"","employee_id":23,"level":""}]}],"schedule":[],"mamage_record":[],"update_time":null,"index_level_id":"","result_employee_name":"","reviewer_name":""}]}]','reset_flow':0,'ding_msg':1,'comment':'调整目标-仅修改指标内容，不重置流程'+str(kkk)+'。'}  #调整目标,不重置流程-数据（注意：在''中不支持\n，否则数据无效）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(regulated_object1))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==24:
            if int(data['api_num2'])==1:
                main_process_data = {'id': result['data']['list'][0]['id'], 'employee_id_code': result['data']['list'][0]['employee_id']}  #员工考核记录详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(personal_assessment_record_id3))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                main_process_data = {'id': str(result['data']['id']),'dimension':'[{"name":"量化指标A","index_type":1,"index_num":0,"weight_type":0,"dimension_weight":100,"total_weight":0,"target_index":1,"index":[{"id":"'+str(result['data']['dimension'][0]['index'][0]['id'])+'","custom":1,"type":1,"name":"指标1('+'编辑'+str(kkk)+')","per_remark":"今天是个下雨天，天气还有点冷('+'编辑'+str(kkk)+')","remark":"需要注意穿衣保暖，不要冻感冒了('+'编辑'+str(kkk)+')","target":"100","unit":"光年","point_limit":0,"weight":50,"result_type":"supervisor","index_level_id":"","result_employee_id":"","result_employee_name":"","reviewer_id":35,"reviewer_name":"刘俊华","record_ids":[24],"mamage_record":[],"schedule":[],"need":0}]},{"name":"非量化指标B","index_type":2,"index_num":0,"weight_type":0,"dimension_weight":100,"total_weight":0,"target_index":1,"index":[{"id":"'+str(result['data']['dimension'][1]['index'][0]['id'])+'","custom":1,"type":2,"name":"指标2('+'编辑'+str(kkk)+')","per_remark":"明天的天气不知是个什么状况('+'编辑'+str(kkk)+')","remark":"不管明天的天气是个啥状况，总之，吃饱穿暖就对了('+'编辑'+str(kkk)+')","target":"","result":null,"result_type":"none","result_employee_id":0,"unit":"","weight":"50","point_limit":0,"reviewer_id":0,"record_ids":[],"need":0,"score_info":[{"id":5,"weight":100,"multi_executor":2,"employees":[{"point":null,"title":"一级部门主管评分：刘水线(100%)","remark":"","employee_id":31,"level":""},{"point":null,"title":"一级部门主管评分：李杰(100%)","remark":"","employee_id":23,"level":""}]}],"schedule":[],"mamage_record":[],"update_time":null,"index_level_id":"","result_employee_name":"","reviewer_name":""}]}]','reset_flow':1,'ding_msg':1,'comment':'调整目标-修改指标，并重置考核流程'+str(kkk)+'。'}  #调整目标,重置流程-数据（注意：在''中不支持\n，否则数据无效）

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(regulated_object1))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==25:
            if int(data['api_num2'])==1:
                main_process_data = {'id': str(result['data']['list'][0]['id']),'target_id':'[26,31]','content':'人生的价值犹如一条河水,我们站在河边各有各的位置'+str(kkk)+'。','ding_msg':1}  #沟通协商(沟通反馈)数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(main_process_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(personal_assessment_record_id3))  #给下一行写入数据(覆盖)


        #手动修改归档状态接口（暂停，备份）
        if int(data['api_num1'])==233:
            if int(data['api_num2'])==1:
                main_process_data = {'package_id': str(result['data']['list'][0]['package_id'])}  #手动修改归档状态数据
                box_excel.write_excel(int(data['id']) + 2, 9, str(main_process_data))  #给下一行写入数据(覆盖)


        box_excel.write_excel(int(data['id'])+1,12,str(result))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
        box_excel.write_excel(int(data['id'])+1,13,str(result['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’

        #对断言进行异常捕获，断言正常的回写用例已通过，断言异常的回写用例未通过
        try:
            self.assertEqual(int(result['code']),int(data['expected_result']))

            if int(data['api_num1'])==1:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==2:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg'])}))
            if int(data['api_num1'])==3:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==4:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==5:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==6:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==7:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==8:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==9:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==10:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==11:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==12:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==13:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==14:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==15:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==16:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==17:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"name:" + str(result['data']['list'][0]['name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"employee_id:" + str(result['data']['list'][0]['employee_id']), "index_name:" + str(result['data']['list'][0]['index_name']),'pe_id:'+str(result['data']['list'][0]['pe_id'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==18:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"name:" + str(result['data']['list'][0]['name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "pe_id:" + str(result['data']['process']['target'][0]['pe_id']), "employee_id:" + str(result['data']['process']['target'][0]['employee_id']),'msg:'+str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==19:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"name:" + str(result['data']['list'][0]['name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "pe_id:" + str(result['data']['dimension']['record_ids'][0]['pe_id']),'msg:'+str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==20:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg'])}))
            if int(data['api_num1'])==21:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==22:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:" + str(result['data']['list'][0]['id']),"employee_id:" + str(result['data']['list'][0]['employee_id']),"employee_name:" + str(result['data']['list'][0]['employee_name']),"package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==23:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==24:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==25:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))


            #手动修改归档状态接口（暂停，备份）
            if int(data['api_num1'])==233:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"id:" + str(result['data']['list'][0]['id']), "package_name:" + str(result['data']['list'][0]['package_name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))

        except AssertionError as f: #断言异常的
            box_excel.write_excel(int(data['id'])+1,15,'用例未通过') #注意：写入的文件，必须是处于关闭状态，否则程序无法写入
            raise f #当断言时，会显示出失败的、成功的数量

        else: #否则，断言是正常的
            box_excel.write_excel(int(data['id'])+1,15,'用例已通过')

#调试运行
if __name__ == '__main__':
    unittest.main()

#在Excel中的数据
#运行前（真正运行,编辑时的数据）：{'cate_id': 16, 'name': '修改指标分类名称1644919283'}
#运行后（重新写入的最新数据，提供下次运行使用）：{'cate_id': 16+1, 'name': '修改指标分类名称1644919453'}


