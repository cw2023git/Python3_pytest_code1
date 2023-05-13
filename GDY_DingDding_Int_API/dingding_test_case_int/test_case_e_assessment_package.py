
#-------------------------------考核包测试用例模块的封装-------------------------------
import unittest
from ddt import ddt,data
from dingding_send_request.send_request_dingding import * #导入发送请求模块中的所有内容
from dingding_test_data.dingding_excel_data.xlrd_openpyxl_excel_dingding import * #导入该模块中的所有内容
import logging
import time #时间戳
import warnings #警告模块
import os
import calendar #计算每个月的天数
import sys
import datetime #获取当天日期（只要今天几号）

now_year=int(datetime.datetime.now().strftime('%Y'))  #只要今天具体是几年 即可
now_month=int(datetime.datetime.now().strftime('%m'))  #只要今天具体是几月 即可
now_day=int(datetime.datetime.now().strftime('%d'))  #只要今天具体是几号 即可

now_year1=int(datetime.datetime.now().strftime('%Y'))  #只要今天具体是几年 即可
now_month1=int(datetime.datetime.now().strftime('%m'))  #只要今天具体是几月 即可
now_day1=int(datetime.datetime.now().strftime('%d'))  #只要今天具体是几号 即可

kkk=int(time.time()) #创建时间戳(整数类型，去掉小数点)【只运行一次，全局变量】
# print('时间戳：',kkk)

# box_excel=Xlrd_Write_Excel('../dingding_test_data/dingding_excel_data/ddt_data_考核包.xlsx','考核管理') #本地文件运行
box_excel=Xlrd_Write_Excel('./dingding_test_data/dingding_excel_data/ddt_data_考核包.xlsx','考核管理') #主函数运行
testData=box_excel.read_excel()
print('读取Excel表格中数据的结果:',testData)

# print('---------------------------------------------------------------------------------------开始执行考核包接口测试用例---------------------------------------------------------------------------------------')
print() #换行

@ddt #数据驱动
class Test_case(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning) #此方法治标不治本，只是隐藏了‘警告信息’

    @data(*testData) #@data把列表testData中每一行字典数据分离开来
    def test_case_e_assessment_package(self,data):#传入data数据
        logging.info('--------------test_case_e_assessment_package_'+str(data['id'])+'--------------')

        #读取文件
        with open('./dingding_json_data/dingding_json_data.json', 'r',encoding='utf-8') as r_json:
            json_data=json.load(r_json) #读取上个接口响应的数据

        #写入文件
        def write_function(public_methods):
            #把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
            with open('./dingding_json_data/dingding_json_data.json', 'w') as w_json:
                json.dump(public_methods, w_json)

        time.sleep(0.5) #等待0.5秒（防止请求速度过快，导致响应不及时，从而报异常）

        #【注意：数据初始化（钉钉版绩效，无法进行了，目前先这样吧】
        global assessment_group_total,now_month,now_month1,now_day,now_day1,result2,l,review_package_data,ids  #全局变量

        res = Request().send_request(data,json_data)  #发送请求，并返回响应的结果
        result = res.json()  #转化为json格式
        print('excel接口响应返回数据-result：', result)

        if int(data['api_num1']) == 1:
            if int(data['api_num2']) == 1:
                assessment_group_total = result['data']['total']  #获取考评组列表总数
                if int(now_month1)<=9:now_month1 = '0' + str(now_month1) #月
                if int(now_day1)<=9: now_day1 = '0' + str(now_day1) #日
                data_format = str(now_year1) + str(now_month1) + str(now_day1)  #拼接符合接口参数中的日期格式要求(20200618)

                #找到周期类型-天（"cycle_type": 1）且存在被考核人的‘考核表’
                for ids in range(0, assessment_group_total):
                    if result['data']['list'][(assessment_group_total-1)-ids]['cycle_type'] == 1 and result['data']['list'][(assessment_group_total-1)-ids]['employee_num'] != 0:  #判断周期类型-天，被考核人-存在
                        the_inspection_package_data={"group_ids["+str((assessment_group_total-1)-ids)+"]":result['data']['list'][(assessment_group_total-1)-ids]['id'],"cycle_type": 1,"date":str(data_format),"config":{"config.assessment": {"config.assessment.feedback": 1,"config.assessment.point_scope": {"config.assessment.point_scope.employee": 2,"config.assessment.point_scope.manager": 2,"config.assessment.point_scope.special": 2,"config.assessment.point_scope.same_level": 2,"config.assessment.point_scope.reviewer": 2},"config.assessment.point_comment": {"config.assessment.point_comment.employee": 2,"config.assessment.point_comment.manager": 2,"config.assessment.point_comment.manager.special": 2,"config.assessment.point_comment.same_level": 2,"config.assessment.point_comment.reviewer": 2},"config.assessment.result_distribution": 1},"config.manager_adjustment": 0}} #拼接考核包数据

                        # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                        write_function(the_inspection_package_data)

                        # box_excel.write_excel(int(data['id']) + 2, 9,str(review_package_data)) #给下一行写入数据(覆盖)
                        break #结束此次循环

            if int(data['api_num2'])==2:
                res1 = requests.session().request(url=data['host_url'] + '/api/per/evaluation/all_group', headers=eval(data['headers']),method='GET',verify=False)
                result1 = res1.json() #响应结果

                if int(result['code'])==0 and result['msg']=='同周期考核表的考核包已存在':
                    print('请注意：同周期考核表的考核包已存在！')
                    for k in range(now_year, sys.maxsize):  #年，sys.maxsize，几乎无限获取数据
                        for i in range(now_month, 13):  #当前月份~12月份(一年共有12个月)
                            day_num_list1 = list(calendar.monthrange(k, i)) #(2022,2)
                            # if i == int(now_month):  #月 2
                            for j in range(now_day, day_num_list1[1] + 1):  #天 23

                                time.sleep(0.5) #每轮循环，等待0.5秒（主要是我不想让程序跑辣么快）

                                if int(i) <= 9:i = '0' + str(i)
                                if j <= 9:j = '0' + str(j)

                                data_format=str(k) + str(i) + str(j) #拼接符合接口参数中的日期格式要求(20200618)
                                review_package_data = {"group_ids[" + str((assessment_group_total-1)-ids) + "]":result1['data']['list'][(assessment_group_total-1)-ids]['id'], "cycle_type": 1,"date": str(data_format), "config": {"config.assessment": {"config.assessment.feedback": 1,"config.assessment.point_scope": {"config.assessment.point_scope.employee": 2,"config.assessment.point_scope.manager": 2,"config.assessment.point_scope.special": 2,"config.assessment.point_scope.same_level": 2,"config.assessment.point_scope.reviewer": 2},"config.assessment.point_comment": {"config.assessment.point_comment.employee": 2,"config.assessment.point_comment.manager": 2,"config.assessment.point_comment.manager.special": 2,"config.assessment.point_comment.same_level": 2,"config.assessment.point_comment.reviewer": 2},"config.assessment.result_distribution": 1},"config.manager_adjustment": 0}}  #拼接考核包数据
                                res2 = requests.session().request(url=data['host_url'] + data['request_url'],headers=eval(data['headers']), method=data['method'],data=review_package_data,verify=False)
                                result2 = res2.json()
                                if result2['code'] == 1 and result2['msg'] == '提交成功':
                                    print('发起考核成功了！')
                                    break
                                i = int(i)
                                # if int(j) <= int(day_num_list1[1]):
                                now_day = 1
                            # if int(i) <= 12:
                                now_month = 1
                            else:continue
                            break
                        else:continue
                        break
                else:
                    data['api_num2']=str(22) #（若一开始‘发起考核’就能创建成功后，就给data['api_num2']重新赋值）

        if int(data['api_num1'])==2:
            if int(data['api_num2'])==1:
              the_inspection_package_data={"package_id":result['data']['list'][0]['id'], "employee_ids_code":'["22"]'}  #往考核包添加用户（莫仕钊,id=22）数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 2, 9, str(review_package_data1))  # 给下一行写入数据(覆盖)

            if int(data['api_num2'])==3:
              the_inspection_package_data={"package_id":result['data']['list'][0]['id'],"doing_id":0,"page":1,"page_size":100}  #考核包详情v3(优先使用)数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 3, 8, str(review_package_data2))  #给下二行写入数据(覆盖)

        if int(data['api_num1'])==3:
            if int(data['api_num2'])==1:
              the_inspection_package_data = {"package_id": result['data']['list'][0]['id'],"employee_ids_code": '["22"]'}  #往考核包删除用户（莫仕钊,id=22）数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 2, 9, str(review_package_data1))  # 给下一行写入数据(覆盖)
            if int(data['api_num2'])==3:
              the_inspection_package_data = {"package_id": result['data']['list'][0]['id'], "doing_id": 0, "page": 1,"page_size": 100}  #考核包详情v3(优先使用)数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 3, 8, str(review_package_data2))  #给下二行写入数据(覆盖)

        if int(data['api_num1'])==4:
            if int(data['api_num2'])==1:
              the_inspection_package_data = {"package_id": result['data']['list'][0]['id']}  #可以往考核包加的用户列表-数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 2, 8, str(review_package_data1))  #给下一行写入数据(覆盖)

        if int(data['api_num1'])==7:
            if int(data['api_num2'])==1:
              the_inspection_package_data = {"package_id": result['data']['list'][0]['id']}  #获取指定考核包的考评组列表-数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 2, 8, str(review_package_data1))  #给下一行写入数据(覆盖)

            if int(data['api_num2'])==3:
              the_inspection_package_data = {"package_id": result['data']['list'][0]['id']}  # 获取指定考核包的考评组列表-数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 3, 8, str(review_package_data1))  #给下二行写入数据(覆盖)

        if int(data['api_num1'])==8:
            if int(data['api_num1'])==1:
                the_inspection_package_data={"package_id":result['data']['list'][0]['id']} #员工考核记录信息列表数据

                # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
                write_function(the_inspection_package_data)

        if int(data['api_num1'])==9:
            if int(data['api_num2'])==1:
              the_inspection_package_data = {"id": result['data']['list'][0]['id'],"publicity":'{"publicity": [26],"concealment":[34]}'}  #编辑绩效包公示配置-数据

              # 把此接口的响应相关数据，加入到准备数据之中，给下个接口提供数据
              write_function(the_inspection_package_data)

              # box_excel.write_excel(int(data['id']) + 2, 9, str(review_package_data1))  #给下一行写入数据(覆盖)


        if int(data['api_num1'])==1 and int(data['api_num2'])==2:
            box_excel.write_excel(int(data['id']) + 1, 12, str(result2))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
            box_excel.write_excel(int(data['id']) + 1, 13,str(result2['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
        else:
            box_excel.write_excel(int(data['id'])+1,12,str(result))  #把响应返回的全部结果，逐一写入到excel表中‘response_result’
            box_excel.write_excel(int(data['id'])+1,13,str(result['code']))  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’


        #对断言进行异常捕获，断言正常的回写用例已通过，断言异常的回写用例未通过
        try:
            if int(data['api_num1']) == 1 and int(data['api_num2']) == 2:
                self.assertEqual(int(result2['code']), int(data['expected_result']))
            else:
                self.assertEqual(int(result['code']),int(data['expected_result']))

            #把响应结果数据写入指定位置
            if int(data['api_num1'])==1:
                if int(data['api_num2'])==1:
                    #找到周期类型-天（"cycle_type": 1）且存在被考核人的‘考核表’
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"id:"+str(result['data']['list'][(assessment_group_total-1)-ids]['id']),"name:"+str(result['data']['list'][(assessment_group_total-1)-ids]['name']),"employee_num:"+str(result['data']['list'][(assessment_group_total-1)-ids]['employee_num'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result2['code']),"msg:" + str(result2['msg']),"name:" + str(result2['data']['name'])}))
            if int(data['api_num1'])==2:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==4:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
            if int(data['api_num1'])==3:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==4:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg']),"total:" + str(result['data']['total'])}))
            if int(data['api_num1'])==4:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg'])}))
            if int(data['api_num1'])==5:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg'])}))
            if int(data['api_num1'])==6:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg'])}))
            if int(data['api_num1'])==7:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg']),"id:" + str(result['data'][0]['id']),"name:" + str(result['data'][0]['name'])}))
                if int(data['api_num2'])==3:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==4:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg'])}))
            if int(data['api_num1'])==8:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']),"msg:" + str(result['msg']),"id:" + str(result['data']['list'][0]['id']),"employee_name:" + str(result['data']['list'][0]['employee_name'])}))
            if int(data['api_num1'])==9:
                if int(data['api_num2'])==1:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:"+str(result['code']),"msg:"+str(result['msg']),"total:"+str(result['data']['total'])}))
                if int(data['api_num2'])==2:
                    box_excel.write_excel(int(data['id']) + 1, 11, str({"code:" + str(result['code']), "msg:" + str(result['msg'])}))


        except AssertionError as f: #断言异常
            box_excel.write_excel(int(data['id']) + 1, 13, 0)  #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
            box_excel.write_excel(int(data['id'])+1,15,'用例未通过') #注意：写入的文件，必须是处于关闭状态，否则程序无法写入
            raise f #当断言时，会显示出失败的、成功的数量

        else: #否则，断言是正常的
            box_excel.write_excel(int(data['id']) + 1, 13,1) #提取响应返回结果中的一部分，逐一写入到excel表中‘check’，用于‘断言’
            box_excel.write_excel(int(data['id'])+1,15,'用例已通过')

#调试运行
if __name__ == '__main__':
    unittest.main()

#在Excel中的数据
#运行前（真正运行,编辑时的数据）：{'cate_id': 16, 'name': '修改指标分类名称1644919283'}
#运行后（重新写入的最新数据，提供下次运行使用）：{'cate_id': 16+1, 'name': '修改指标分类名称1644919453'}
#列表-用中括号[]，嵌套时，需要单引号
#字典(json)-用大括号{}，嵌套时，无需单引号














































