
#-----------------------------------封装日志工具类-----------------------------------

import logging #导入日志模块
from config_cw import Config_cw #导入logs目录
import datetime #导入当前时间
from config_cw.Config_cw import ConfigYaml #导入扩展名
import os

#定义存储日志级别的映射的变量
log_level_map={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR
}

#创建类
class Logger:
    #初始化
    def __init__(self,log_file,log_name,log_level):
        self.log_file=log_file #日志文件（扩展名、配置文件）
        self.log_name=log_name #日志名称
        self.log_level=log_level #日志等级

    #输出控制台或文件
        self.logger=logging.getLogger(self.log_name) #设置logger名称
        self.logger.setLevel(log_level_map[self.log_level]) #设置log级别

        #判断handlers是否存在
        if not self.logger.handlers:
            fh_stream=logging.StreamHandler() #输出控制台
            fh_stream.setLevel(log_level_map[self.log_level]) #设置日志级别

            formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s') #定义输出格式

            #写入文件
            fh_file=logging.FileHandler(self.log_file)
            fh_file.setLevel(log_level_map[self.log_level])
            fh_file.setFormatter(formatter)

            #添加handlers
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)

#初始化参数数据（日志文件名称、日志文件级别）
log_path=Config_cw.get_log_path() #获取logs目录
current_time=datetime.datetime.now().strftime("%Y-%m-%d") #获取当前时间
log_extension=ConfigYaml().get_log_extension() #获取扩展名
logfile=os.path.join(log_path,current_time+log_extension) #log文件，拼接文件名称
loglevel=ConfigYaml().get_log_level() #日志文件级别

#定义使用日志的方法
def my_log(log_name=__file__): #__file__，传入的是默认为当前文件名称或者指定文件的路径或不写
    return Logger(log_file=logfile,log_name=log_name,log_level=loglevel).logger

if __name__ == '__main__':
    my_log().debug('这是一个debug的测试')














































