
#简单使用，连接数据库
"""
import pymysql

#1、导入pymysql包
#2、连接database（使用‘navicat’客户端，连接mysql数据库）
conn=pymysql.connect(
    host='211.103.136.242',
    user='test',
    password='test123456',
    database='meiduo',
    # charset='utf-8',
    port=7090 #注意：若是使用默认端口（8090），则无需定义
)

#3、获取执行sql的光标对象
cursor=conn.cursor()

#4、执行sql
sql="select username,password from tb_users" #编写sql语句
# cursor.execute(sql) #执行sql语句（没打印出结果）

res=cursor.execute(sql) #执行sql语句
cursor.fetchone() #查询，是查询单条信息还是多条信息，如果是查询多条信息，使用fetchone()方法
print('输出查询数据库结果：',res)

#5、关闭对象
cursor.close() #关闭光标对象
conn.close() #关闭数据库对象
"""

#-----------------------------------------------

# 工具类封装及使用：
# 1、PyMysql工具类封装
import pymysql
from utils.LogUtils import my_log

#1、创建封装类
class Mysql:
    # 2、初始化数据，连接数据库，创造光标对象
    def __init__(self,host,user,password,database,charset='utf-8',port=3306):
        self.log=my_log()
        self.conn=pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port  #注意：若是使用默认端口（8090），则无需定义
        )
        #cursor=pymysql.cursors.DictCursor，是为了处理结果是’元组‘的情况，如此返回的数据就是个’字典‘格式了
        self.cursor=self.conn.cursor(cursor=pymysql.cursors.DictCursor) #创造光标对象（获取执行sql的光标对象）

#3、创建查询、执行方法
    def fetchone(self,sql): #定义的是查询一个数据的方法
        """
        单个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql) #执行sql语句
        return self.cursor.fetchone() #返回所查询的数据，查询一个

    def fetchall(self,sql): #定义的是查询多个数据的方法
        """
        多个查询
        :param sql:
        :return:
        """
        self.cursor.execute(sql) #执行sql语句
        return self.cursor.fetchall() #查询数据，查询多个

    #定义个执行方法【用于更新mysql的数据】
    def exec(self,sql):
        """
        执行
        :return:
        """
        #问题：如果数据或光标没有进行初始化操作，是不是会报错呀
        #解决如下：
        try:#如果执行数据库报错的话，我们需要回滚
            if self.conn and self.cursor: #判断这两个都有了（即：都进行了初始化）
                self.cursor.execute(sql) #执行sql语句
                self.conn.commit() #提交
        except Exception as ex:
            self.conn.rollback() #若报错，直接回滚
            self.log.error('Mysql 执行失败')
            self.log.error(ex)
            return False #失败，返回
        return True #成功，返回


#4、关闭对象（光标对象、连接数据库对象）
    def __del__(self): #当完成以后，会自动关闭对象
        #1、关闭光标对象
        if self.cursor is not None: #判断光标对象不为空时，才去关闭
            self.cursor.close()

        #2、关闭连接对象
        if self.conn is not None: #判断连接对象不为空时，才去关闭
            self.conn.close()

if __name__ == '__main__':
    mysql=Mysql("211.103.136.242", #初始化类
                "test",
                "test123456",
                "meiduo",
                charset="utf-8",
                port=7090
                )
    # sql = "select username,password from tb_users"  # 编写sql语句
    # res=mysql.fetchone("select username,password from tb_users") #查询单条数据
    # res=mysql.fetchall("select username,password from tb_users") #查询多条数据

    #此语句‘慎用’
    res=mysql.exec('update tb_users set first_name="python" where username="python"') #更新sql数据
    print(res)

    """
    如果写很多测试用例，需要验证结果的时候，为了方便管理、不易出错，
    我们可以把以上固定的信息，提取出来，放在‘配置文件’当中，来进行读取
    """
    #1、创建新的db_conf.yaml，db1，db2
    #2、编写数据库基本信息
    #3、重构Conf.py
    #4、执行









































