
#-------------------------------数据同步接口测试用例模块的封装-------------------------------
import unittest
from ddt import ddt,data
from dingding_send_request_int.send_request_dingding_int import * #导入发送请求模块中的所有内容
from dingding_test_data_int.dingding_excel_data_int.xlrd_openpyxl_excel_dingding import * #导入该模块中的所有内容
import logging
import time #时间戳
import warnings #警告模块

kkk=int(time.time()) #创建时间戳(整数类型，去掉小数点)【只运行一次，全局变量】
# print('时间戳：',kkk)

box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_数据同步接口.xlsx','数据同步接口') #本地文件运行
# box_excel=Xlrd_Write_Excel('./dingding_test_data/dingding_excel_data/ddt_data_数据同步接口.xlsx','数据同步接口') #主函数运行

testData=box_excel.read_excel()
print('读取Excel表格中数据的结果:',testData)

# print('---------------------------------------------------------------------------------------开始执行数据同步接口测试用例---------------------------------------------------------------------------------------')
print() #换行

@ddt #数据驱动
class Test_case(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) #此方法治标不治本，只是隐藏了‘警告信息’

    @data(*testData) #@data把列表testData中每一行字典数据分离开来
    def test_case_a_data_synchronization_interface(self,data):#传入data数据
        logging.info('--------------test_case_a_data_synchronization_interface_'+str(data['id'])+'--------------')

        #读取文件
        with open('../dingding_json_data/dingding_json_nulldata.json', 'r',encoding='utf-8') as r_json:
            json_data=json.load(r_json) #读取上个接口响应的数据

        #写入文件
        def write_function(public_methods):
            #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
            with open('../dingding_json_data/dingding_json_data.json', 'w') as w_json:
                json.dump(public_methods, w_json)

        time.sleep(0.5)  #等待0.5秒（防止请求速度过快，导致响应不及时，从而报异常）

        #【注意：数据初始化（钉钉版绩效，无法进行了，目前先这样吧】
        global employee_status,is_official #全局变量(不起作用)
        res = Request().send_request(data,json_data)  #发送请求，并返回响应的结果
        result = res.json()  #转化为json格式
        print('excel接口响应返回数据-result：', result)


        box_excel.write_excel(int(data['id'])+1,11,str(result))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
        box_excel.write_excel(int(data['id'])+1,12,str(result['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’

        #对断言进行异常捕获，断言正常的回写用例已通过，断言异常的回写用例未通过
        try:
            self.assertEqual(int(result['code']),int(data['expected_result']))

            if int(data['api_num1']) == 1:
                if int(data['api_num2']) == 1:
                    box_excel.write_excel(int(data['id']) + 1, 10,str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))

        except AssertionError as f: #断言异常的
            box_excel.write_excel(int(data['id'])+1,14,'用例未通过') #注意：写入的文件，必须是处于关闭状态，否则程序无法写入
            raise f #当断言时，会显示出失败的、成功的数量

        else: #否则，断言是正常的
            box_excel.write_excel(int(data['id'])+1,14,'用例已通过')

#调试运行
if __name__ == '__main__':
    unittest.main()

#在Excel中的数据
#运行前（真正运行,编辑时的数据）：{'cate_id': 16, 'name': '修改指标分类名称1644919283'}
#运行后（重新写入的最新数据，提供下次运行使用）：{'cate_id': 16+1, 'name': '修改指标分类名称1644919453'}




