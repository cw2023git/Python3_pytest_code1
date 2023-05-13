
import os
import xlrd

#把读取Excel数据方法进行封装
#目的：是为了参数化，要知道'pytest'框架的数据格式是‘list’列表，需要返回给我的是list格式数据

#自定义异常
class SheetTypeError:
    pass

#1、验证文件是否存在，存在读取，不存在报错
class ExcelReader:
    def __init__(self,excel_file,sheet_by):
        if os.path.exists(excel_file):
            self.excel_file=excel_file
            self.sheet_by=sheet_by
            self._data=list() #定义一个空列表
        else: #判断不存在，则抛出异常
            raise FileNotFoundError("excel文件不存在！")

    #2、读取sheet方式，名称，索引
    def data(self):
        global sheet
        #存在则不读取，不存在则需读取
        if not self._data: #判断‘self._data’不存在的情况，需读取
            workbook=xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str,int]: #判断sheet对象是否是str类型、int类型
                raise SheetTypeError("请输入int或str")
            elif type(self.sheet_by)==int:
                sheet=workbook.sheet_by_index(self.sheet_by) #根据索引，获取sheet对象
            elif type(self.sheet_by)==str:
                sheet=workbook.sheet_by_name(self.sheet_by)  #根据名称，获取sheet对象

        #3、读取sheet内容
            #返回list，元素：字典
            #格式[{"a":"a1","b":"b1"},{"a":"a2","b":"b2"}]
            #1、获取首行的信息
            title=sheet.row_values(0)

            #2、遍历测试行与首行组成dict(字典)，放在list(列表)
            #1、循环，过滤首行，从1开始
            for col in range(1,sheet.nrows):
                col_valus=sheet.row_values(col)
                #2、与首行组成字典，放在list
                self._data.append(dict(zip(title, col_valus)))

        #4、结果返回
        return self._data

"""
#举例：
header=["a","b"]
values1=["a1","b1"]
values2=["a2","b2"]

print(dict(zip(header,values1))) #输出结果：{'a': 'a1', 'b': 'b1'}
print(dict(zip(header,values2))) #输出结果：{'a': 'a2', 'b': 'b2'}

data_list=list() #定义一个空列表
data_list.append(dict(zip(header,values1)))
data_list.append(dict(zip(header,values2)))
print('data_list：',data_list) #输出结果：[{'a': 'a1', 'b': 'b1'}, {'a': 'a2', 'b': 'b2'}]
"""

if __name__ == '__main__':
    reader=ExcelReader("../data/testdata.xlsx","美多商城接口测试用例")
    print(reader.data())

























