
#--------------------------------读取&写入Excel--------------------------------
#读取excel表中的数据，使用xlrd模块
#写入excel表中的数据，使用openpyxl模块
import xlrd      #用于读取
import openpyxl  #用于写入
import os        #用于检查
import sys       #用于退出测试程序

#定义一个类
class Xlrd_Write_Excel():
    def __init__(self,excel_name,sheet_name):
        self.excel_name=excel_name
        self.sheet_name=sheet_name

    #定义读取excel表数据的方法
    def read_excel(self):
        excel_path=os.path.join(os.getcwd(),self.excel_name)#获取当前路径下的excel表文件
        if not os.path.exists(excel_path):
            print('Excel表文件不存在！！！')
            sys.exit() #找不到指定的文件，就会退出测试程序
        file=xlrd.open_workbook(self.excel_name)  #打开指定的excel表文件
        table=file.sheet_by_name(self.sheet_name) #获取excel表中指定的sheet名称

        nrows=table.nrows #获取总行数
        ncols=table.ncols #获取总列数

        if nrows >1: #判断sheet页中是否有数据
            keys=table.row_values(0)#表示获取sheet表中第一行数据(即:sheet表中自己设计的表头样式)
            list_data=[] #定义一个空列表
            for i in range(1,nrows):
                values=table.row_values(i) #获取除表头以外的sheet表中的每一行数据
                dict_data=dict(zip(keys,values))#把keys和values这两个列表进行一一对应组成字典
                list_data.append(dict_data) #把组成每一行的字典存放到列表list_data中
            return list_data #最后，返回这个存储了整个excel表格中的每一行字典格式数据的列表list_data
        else:
            print('指定的sheet表未填写数据')
            return None

    #写入excel表前，打开excel表，选择表单
    def open(self):
        self.excel=openpyxl.load_workbook(self.excel_name)#加载excel表文件
        self.sheet=self.excel[self.sheet_name]            #打开sheet页

    #写入excel表后，关闭excel表，释放内容
    def close(self):
        self.excel.close()

    #定义写入excel表数据的方法
    # row-行数、column-列数、value-要写入的内容（注意:行数、列数这里都是指数字，不是下标）
    def write_excel(self,rows,cols,values):
        self.open() #调用open()方法，加载、打开excel表
        self.sheet.cell(row=rows,column=cols,value=values) #写入指定表格、指定的数据
        self.excel.save(self.excel_name) #保存excel表文件
        self.close() #调用close()方法，关闭excel表

#调试运行
if __name__ == '__main__':
    box1=Xlrd_Write_Excel('./ddt_data_指标.xlsx','指标库接口') #此模块和Excel文件在同一个文件夹下
    read1=box1.read_excel()
    print('read1:',read1[0])

    # box1.write_excel(10,2,'国家机密')


















































