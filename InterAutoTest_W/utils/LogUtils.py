
import logging
from config import config #导入logs目录
import datetime #导入当前时间
from config.config import ConfigYaml #导入扩展名
import os

#定义日志级别的映射
log_l={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR,
}

#封装log工具类
class Logger: #1、创建类
#2、定义参数
   def __init__(self,log_file,log_name,log_level):
       self.log_file=log_file #扩展名 配置文件
       self.log_name=log_name #参数
       self.log_level=log_level
#3、输出控制台或文件
       self.logger = logging.getLogger(self.log_name)  #1、设置logger名称
       self.logger.setLevel(log_l[self.log_level])  #2、设置log级别

       #判断handlers是否存在
       if not self.logger.handlers:
           fh_stream = logging.StreamHandler()  #3、输出控制台
           fh_stream.setLevel(log_l[self.log_level])  #4、设置日志级别
           formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')  #5、定义输出格式
           fh_stream.setFormatter(formatter)

           #写入文件
           fh_file = logging.FileHandler(self.log_file)
           fh_file.setLevel(log_l[self.log_level])
           fh_file.setFormatter(formatter)

           self.logger.addHandler(fh_stream)  # 6、添加handler
           self.logger.addHandler(fh_file)


# 2、重构配置文件-[以重构了，相当于修改了]
#
# 3、日志工具类应用
#(1)、初始化参数数据（日志文件名称、日志文件级别）
#日志文件名称=logs目录+当前时间+扩展名
log_path=config.get_log_path() #获取logs目录
current_time=datetime.datetime.now().strftime("%Y-%m-%d") #当前时间
log_extension=ConfigYaml().get_conf_log_extension() #扩展名
logfile=os.path.join(log_path,current_time+log_extension)
print('查看结果1：',logfile)

#日志文件级别
loglevel=ConfigYaml().get_conf_log()
print('查看结果2：',loglevel)

#(2)、对外方法，初始log工具类，提供其它类使用
def my_log(log_name=__file__):#__file__，传入的是默认为当前文件名称，或者指定文件的路径或不写
    return Logger(log_file=logfile,log_name=log_name,log_level=loglevel).logger

if __name__ == '__main__':
    my_log().debug('这是一个debug的测试')











































