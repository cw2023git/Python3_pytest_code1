
#-----------------------------------封装获取excel数据方法-----------------------------------

from utils_cw.ExcelUtil_cw import ExcelReader #导入读取Excel数据工具类
from common_cw.ExcelConfig_cw import DataConfig #导入excel列属性方法

#封装类
class Data:
    #初始化方法
    def __init__(self,testcase_file,sheet_name):
        self.reader=ExcelReader(testcase_file,sheet_name) #调用ExcelUtil.py，进行初始化类

    #定义、获取用例，判断是否‘执行’的方法
    def get_run_data(self):
        run_list=list() #定义一个空列表
        for line in self.reader.data():
            #根据是否运行列==y，获取执行测试用例
            if str(line[DataConfig().is_run]).lower()=='y': #不管y是大小写，都转为小写、字符串
                run_list.append(line) #装载进列表
        # print('打印出y的用例：',run_list)
        # print(run_list)
        return run_list #返回

    #定义获取所有测试用例的方法
    def get_case_list(self):
        run_list=list() #空列表
        for line in self.reader.data(): #此处可使用‘列表推导式’
            run_list.append(line) #装载进列表（返回的不都是装载好了吗？、此处为什么还要装载一次？）

        return run_list #返回

    #定义获取执行用例方法【前置用例】
    def get_case_pre(self,pre): #传入前置用例名称
        run_list=self.get_case_list() #获取全部测试用例

        #list判断、执行、获取
        for line in run_list: #循环获取每一条用例信息
            if pre in dict(line).values(): #前置用例是否在全部用例（'dict(line).values()'）之中
                return line
        return None #返回为空的，表示没找到































































