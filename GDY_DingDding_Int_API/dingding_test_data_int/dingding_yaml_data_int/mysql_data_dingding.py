
#=========数据初始化=========
# from pymysql import connect #导入pymysql模块 使用mysql数据库
import pymssql
import yaml    #导入yaml模块
import logging

#连接数据库的基本配置信息
host='127.0.0.1'    #数据库服务器地址
user='sa'           #数据库账户
password='123'          #数据库密码
database='ccc'         #数据库名
chart='UTF-8'        #编码格式（全大写）

class DB():#定义一个DB类
    def __init__(self):
        self.conne=pymssql.connect(host=host,      #数据库服务器地址
                                   user=user,      #数据库账户
                                   password=password,  #数据库密码
                                   database=database,  #数据库名
                                   charset=chart)     #编码格式

        self.cursor=self.conne.cursor() #创建游标对象

    #定义清除数据的方法
    def clear(self,table):
        logging.info('开始清除数据......')
        sql='truncate table '+table
        self.cursor.execute(sql)
        self.conne.commit()#提交
        logging.info('结束清除数据......')

    #定义插入数据的方法

    def insert(self,table,data1):
        # print('开始插入数据......')
        #首先需要构造sql插入语句
        for i in data1:
            data1[i]="'"+str(data1[i])+"'" #把字典中的每个值，先转化为字符类型
        key=','.join(data1.keys()) #获取字典data1中的每个键,使用,分隔，而join会把字典中每个键加载到key
        value=','.join(data1.values())#获取字典data1中的每个值
        # print(key)
        # print(value)

        #开始构造插入的sql语句
        sql='insert into '+table+'('+key+')'+' values'+'('+value+')'
        self.cursor.execute(sql)#把构造好的sql语句，传入到游标执行对象中
        self.conne.commit()#提交sql语句
        # print('结束插入数据......')

    #定义关闭数据库方法
    def close(self):
        logging.info('开始关闭数据库......')
        self.cursor.close()#关闭游标
        self.conne.close() #关闭数据库
        logging.info('结束关闭数据库......')

    #定义初始化数据方法
    def init_data(self,data2):#传入yaml数据，里面包含了数据表和数据
        logging.info('开始初始化数据......')

        #1、把数据表和数据分离开来
        for table,data3 in data2.items():#data2.items()方法，可以把字典中键和值分离开
            self.clear(table)#调用清除数据的方法
            logging.info('开始插入数据......')
            for j in data3:#2、获取分离开的剩余字典data3中每队键值对
                self.insert(table,j) #调用插入数据的方法
            logging.info('结束插入数据......')

        #3、最后，调用关闭数据库的方法
        self.close()

        logging.info('结束初始化数据......')

if __name__ == '__main__':
    db=DB() #实例化类，生成对象db
    # data1={'id':4,'username':'sql4','password':123}
    # db.insert('python3',data1)
    ddd=open('data.yaml','r',encoding='UTF-8') #因为yaml数据文件和代码在同一路径下
    data2=yaml.load(ddd)#把yaml数据格式转化为python数据格式

    db.init_data(data2)#调用初始化数据的init_data()方法


