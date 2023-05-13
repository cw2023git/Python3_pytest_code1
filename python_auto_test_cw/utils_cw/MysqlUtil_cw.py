
#-----------------------------------封装数据库连接、断言工具类-----------------------------------

import pymysql
from utils_cw.LogUtil_cw import my_log #导入日志库

#封装类
class Mysql:
    #初始化方法、连接数据库、创造光标对象
    def __init__(self,host,user,password,database,charset='utf-8',port=3306):
       self.log=my_log()
       self.conn=pymysql.connect(
           host=host,
           user=user,
           password=password,
           database=database,
           charset=charset,
           port=port #注意：若是使用默认端口（8090），则无需定义
       )

       #创造光标对象（获取执行sql的光标对象）
       #cursor=pymysql.cursors.DictCursor，是为了处理结果是’元组‘的情况，如此返回的数据就是个’字典‘格式了
       self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    #定义查询的方法
    def fetchone(self,sql): #定义的是查询一个数据的方法
       self.cursor.execute(sql) #执行sql语句
       return self.cursor.fetchone() #返回查询的数据

    def fetchall(self,sql): #定义的是查询多个数据的方法
       self.cursor.execute(sql) #执行sql语句
       return self.cursor.fetchall() #返回查询的数据

    #定义执行的方法
    def exec(self,sql):
        try:
            if self.conn and self.cursor: #判断这两个都有了（即：都进行了初始化）
               self.cursor.execute(sql) #执行sql语句
               self.conn.commit() #提交
        except Exception as ex:
            self.log.error('mysql执行失败！')
            self.log.error(ex)
            return False #失败，返回
        return True #成功，返回

    #定义关闭的方法(关闭光标对象、关闭连接数据库对象）)
    def __del__(self): #当完成以后，会自动关闭对象
       #1、关闭光标对象
       if self.cursor is not None: #判断光标对象不为空时，才去关闭
           self.cursor.close() #关闭光标

       #2、关闭连接数据库对象
       if self.conn is not None: #判断连接对象不为空时，才去关闭
           self.conn.close() #光标连接


if __name__ == '__main__':
    mysql = Mysql("211.103.136.242",  # 初始化类
                  "test",
                  "test123456",
                  "meiduo",
                  charset="utf-8",
                  port=7090
                  )

    #此语句‘慎用’
    res = mysql.exec('update tb_users set first_name="python" where username="python"')  #更新sql数据
    print(res)





































































