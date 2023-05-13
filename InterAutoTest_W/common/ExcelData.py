
from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig
"""
#1、使用excel工具类，获取结果list 【注意：以下代码是无法直接使用的，需要进行修改】
reader=ExcelReader("../data/testdata.xlsx","美多商城接口测试用例")
# print(reader.data())


#2、列是否运行内容，y
run_list=list() #定义一个空列表

for line in reader.data():
    if line['是否运行']=='y':
        # print(line)

        #3、保存要执行的结果，放到新的列表
        run_list.append(line)

print(run_list)
"""
#修改如下：

class Data:
    def __init__(self,testcase_file,sheet_name):
        #1、使用excel工具类，获取结果list
        # self.reader=ExcelReader("../data/testdata.xlsx","美多商城接口测试用例")
        self.reader=ExcelReader(testcase_file,sheet_name) #调用、初始化类
        # print(reader.data())

    #2、列是否运行内容，y
    def get_run_data(self):
        """
        根据是否运行列==y，获取执行测试用例
        :return:
        """
        run_list=list() #定义一个空列表

        for line in self.reader.data():#此时在self.reader.data()中，获取到测试用例中全部已组合为列表的数据
            if str(line[DataConfig().is_run]).lower()=='y': #不管y是大小写，都转为小写、字符串
                # print(line)
                #3、保存要执行的结果，放到新的列表
                run_list.append(line) #放进去的数据，表示要执行的
        print(run_list)
        return run_list #返回的要么为空-不用执行（是否运行==n）、要么是有数据-需要执行（是否运行==y）

    #获取所有的测试用例
    def get_case_list(self):
        """
        获取全部测试用例
        :return:
        """
        run_list=list() #空列表
        for line in self.reader.data():
            run_list.append(line)

        #可使用另一种方法-列表推导式
        # run_list=[line for line in self.reader.data()]
        return run_list #返回全部测试用例

    #获取执行用例方法
    def get_case_pre(self,pre):
        #1、获取全部测试用例
        run_list=self.get_case_list()
        #2、list判断，执行，获取
        """
        根据前置条件：从全部测试用例取到测试用例
        :param pre:
        :return:
        """
        for line in run_list:
            if pre in dict(line).values(): #判断、匹配‘前置条件’在全部测试用例中的哪一条
                return line #找到、并返回‘前置条件’所对应的那条用例
        return None #返回为空的，表示没找到
















































