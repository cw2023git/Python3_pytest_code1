
#-----------------------------------封装读取Excel数据工具类-----------------------------------
import os
import xlrd

#把读取Excel数据方法进行封装
#目的：是为了参数化，要知道'pytest'框架的数据格式是‘list’列表，需要返回给我的是list格式数据

#自定义异常（疑问？）
class SheetTypeError:
    pass

#封装类
class ExcelReader():
    #初始化方法
    def __init__(self,excel_file,sheet_by):
        if os.path.exists(excel_file): #判断excel文件是否存在
            self.excel_file=excel_file
            self.sheet_by=sheet_by

            self._data=list() #定义私有的空列表
        else:
            raise FileNotFoundError('excel文件不存在！') #判断excel文件不存在，则抛出异常

    #定义读取sheet方式、名称、索引的方法
    def data(self):
        global sheet #全局变量

        #已存在则不读取，不存在则需读取
        if not self._data: #判断‘self._data’不存在的情况，需读取
            workbook=xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in[str,int]: #判断sheet对象是否是str类型、int类型
                raise SheetTypeError('请输入int类或str类型') #此现象，讲师写的一样如此
            elif type(self.sheet_by)==int:
                sheet=workbook.sheet_by_index(self.sheet_by) #根据索引，获取sheet对象
            elif type(self.sheet_by)==str:
                sheet=workbook.sheet_by_name(self.sheet_by) #根据名称，获取sheet对象
            else:
                print('既不是int类型也不是str类型！')

            #获取sheet内容
            title=sheet.row_values(0) #获取首行的信息

            #遍历测试行与首行组成dict(字典)，放在list(列表)
            #1、循环、过滤首行，从1开始
            for col in range(1,sheet.nrows):
                col_values=sheet.row_values(col) #获取每一行内容
                self._data.append(dict(zip(title,col_values))) #每一行内容和首行组成字典，存放在list

        return self._data #返回

if __name__ == '__main__':
    reader=ExcelReader("../data_cw/testdata_cw.xls","功道云-7.0-积分系统") #实例化类（或初始化类）
    print('输出结果：',reader.data())









































