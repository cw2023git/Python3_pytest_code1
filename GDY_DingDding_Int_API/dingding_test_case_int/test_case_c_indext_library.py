
#-------------------------------指标库测试用例模块的封装-------------------------------
import unittest
from ddt import ddt,data
from dingding_send_request_int.send_request_dingding_int import * #导入发送请求模块中的所有内容
from dingding_test_data_int.dingding_excel_data_int.xlrd_openpyxl_excel_dingding import * #导入该模块中的所有内容
import logging
import time #时间戳
import warnings #警告模块

kkk=int(time.time()) #创建时间戳(整数类型，去掉小数点)【只运行一次，全局变量】
# print('时间戳：',kkk)

box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_指标.xlsx','指标库接口') #本地文件运行
# box_excel=Xlrd_Write_Excel('./dingding_test_data/dingding_excel_data/ddt_data_指标.xlsx','指标库接口') #主函数运行-正式环境
testData=box_excel.read_excel()
print('读取Excel表格中数据的结果:',testData)

# print('---------------------------------------------------------------------------------------开始执行指标库接口测试用例---------------------------------------------------------------------------------------')
print() #换行

@ddt #数据驱动
class Test_case(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) #此方法治标不治本，只是隐藏了‘警告信息’

    @data(*testData) #@data把列表testData中每一行字典数据分离开来
    def test_case_c_indext_library(self,data):#传入data数据
        logging.info('--------------test_case_c_indext_library_'+str(data['id'])+'--------------')

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
        res = Request().send_request(data,json_data)  #发送请求，并返回响应的结果
        result = res.json()  #转化为json格式
        print('excel接口响应返回数据-result：', result)

        if int(data['api_num1'])==1:
            if int(data['api_num2'])==1:
                indicators_of_library_data = {"name": "新增指标分类" + str(kkk)}  #新增指标分类数据

                write_function(indicators_of_library_data)

# 其实此框架并未实现代码、数据之间的分离

                # box_excel.write_excel(int(data['id'])+1,9,str(index_add1)) #把设计好的数据写入Excel（写入本行）

        if int(data['api_num1'])==2:
            if int(data['api_num2'])==1:
                if result['code']==1 and result['data']['total']!=0:
                    class_list_len=len(result['data']['list'])  #分类-获取接口返回数据的长度
                    # print('获取接口返回数据的长度:',class_list_len)
                    indicators_of_library_data={"cate_id": result['data']['list'][class_list_len-1]['id'], "name": "新增指标分类(编辑)" + str(kkk)} #拼接body数据-分类名称

                    #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                    write_function(indicators_of_library_data)

                    # box_excel.write_excel(int(data['id'])+2, 9, str(index_joint)) #给下一行写入数据(覆盖)
                    # box_excel.write_excel(int(data['id'])+2, 13, '1') #给下一行写入‘期望结果’数据
                else:
                    print('此指标分类不存在！')
                    box_excel.write_excel(int(data['id'])+2, 13, '0')  #给下一行写入‘期望结果’数据

        if int(data['api_num1'])==3:
            if int(data['api_num2'])==1:
                if result['code'] == 1 and result['data']['total'] != 0:#删除指标分类接口前，最好要判断下是否存在指标，若存在指标，删除不掉
                    class_list_len = len(result['data']['list'])  #分类-获取接口返回数据的长度
                    # print('获取接口返回数据的长度:',class_list_len)
                    indicators_of_library_data = {"cate_id": result['data']['list'][class_list_len - 1]['id'],'name':result['data']['list'][class_list_len - 1]['name']}  #拼接body数据-分类名称

                    #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                    write_function(indicators_of_library_data)

                    # box_excel.write_excel(int(data['id']) + 2, 9, str(index_joint))  #给下一行写入数据(覆盖)
                else:
                    print('此指标分类不存在！')
                    box_excel.write_excel(int(data['id']) + 2, 13, '0')  #给下一行写入‘期望结果’数据

        if int(data['api_num1'])==4:
            if int(data['api_num2'])==1:
                indicators_of_library_data={"tag[0][tag_name]":"采矿"+str(kkk),"tag[1][tag_name]":"提炼"+str(kkk)} #新增指标分类数据

                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id'])+1,9,str(indicators_of_library_data)) #把设计好的数据写入Excel（写入本行）

        if int(data['api_num1'])==6:
            if int(data['api_num2'])==1:
                indicators_of_library_data={"cate_id":result['data']['list'][0]['id'],"name":"修风扇"+str(kkk),"per_remark":"考核标准：今天要完成10万营业额的目标"+str(kkk),"remark":"今天太阳较大，需注意防晒"+str(kkk),"type":"1","target":"10万","result_type":"none","weight":"55"} #拼接body数据-新增指标数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(index_joint))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==7:
            if int(data['api_num2'])==1:
                indicators_of_library_data={"index_id":result['data']['list'][0]['id']} #指标详情数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id']) + 2, 8, str(index_joint))  #给下一行写入数据(覆盖)
            if int(data['api_num2'])==2:
                indicators_of_library_data={"index_id":result['data']['id'],"cate_id":result['data']['cate_id'],"name":"修风扇(修)"+str(kkk),"per_remark":"考核标准：今天要完成10万营业额的目标(修改)"+str(kkk),"remark":"今天太阳较大，需注意防晒(修改)"+str(kkk),"type":"1","target":"10万(修改)","result_type":"none","weight":"55"} #拼接body数据-编辑指标数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(index_joint2))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==8:
            if int(data['api_num2'])==1:
                indicators_of_library_data={"index_ids":result['data']['list'][int(result['data']['total'])-1]['id']} #拼接body数据-删除指标数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(index_joint2))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==9:
            if int(data['api_num2'])==1:
                indicators_of_library_data={"name":"冰敦敦"+str(kkk),"scope":'[{"name":"C","value":60},{"name":"B","value":70}]'} #指标等级新增编辑数据

                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id']) + 1, 9, str(indicators_of_library_data))  #给本行写入数据(覆盖)

        if int(data['api_num1'])==10:
            if int(data['api_num2'])==1:
                indicators_of_library_data={"id":result['data']['list'][0]['id'],"name":"冰敦(改)"+str(kkk),"scope":'[{"name":"差","value":60},{"name":"良","value":70},{"name":"优","value":80}]'} #指标等级新增编辑数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(index_joint2))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==11:
            if int(data['api_num2'])==1:
                indicators_of_library_data={"id":result['data']['list'][int(result['data']['total'])-1]['id']} #删除指标等级数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(indicators_of_library_data)

            if int(data['api_num2']) == 3:
                #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                indicators_of_library_data = 'null'  #删除指标等级数据

                write_function(indicators_of_library_data)

                # box_excel.write_excel(int(data['id']) + 2, 9, str(index_joint2))  #给下一行写入数据(覆盖)


        box_excel.write_excel(int(data['id'])+1,12,str(result))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
        box_excel.write_excel(int(data['id'])+1,13,str(result['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’

        #对断言进行异常捕获，断言正常的回写用例已通过，断言异常的回写用例未通过
        try:
            self.assertEqual(int(result['code']),int(data['expected_result']))

            if int(data['api_num1'])==1:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "name:" + str(result['data']['name'])}))
            if int(data['api_num1'])==2:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "id:" + str(result['data']['list'][int(result['data']['total'])-1]['id']), "name:" + str(result['data']['list'][int(result['data']['total'])-1]['name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==3:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "id:" + str(result['data']['list'][int(result['data']['total'])-1]['id']), "name:" + str(result['data']['list'][int(result['data']['total'])-1]['name'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==4:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==5:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
            if int(data['api_num1'])==6:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==7:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "id:" + str(result['data']['id'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==8:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==9:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==10:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
            if int(data['api_num1'])==11:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11,str({"code:" + str(result['code']), "msg:" + str(result['msg']), "total:" + str(result['data']['total'])}))


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








