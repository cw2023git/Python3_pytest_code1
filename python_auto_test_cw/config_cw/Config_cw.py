
#-----------------------------------封装配置方法-----------------------------------

import os
from utils_cw.YamlUtil_cw import YamlReader #导入不了
# from utils.yamlutil import YamlReader #先导入另外一个库（这是为啥？）

#1、获取项目基本目录

#获取当前项目的绝对路径
current=os.path.abspath(__file__) #获取当前文件的绝对路径
print('获取当前文件的绝对路径：',current)

base_dir=os.path.dirname(os.path.dirname(current)) #获取当前项目的绝对路径
print('获取当前项目的绝对路径',base_dir)

#定义config_cw目录的路径
_config_path=base_dir+os.sep+"config_cw" #私有变量,基础路径拼接而成
print('定义config_cw目录的路径：',_config_path)

#定义config_cw.yaml文件的路径
_config_file=_config_path+os.sep+"config_cw.yaml"

#定义db_confile_cw.yaml文件的路径
_db_confile_file=_config_path+os.sep+"db_config_cw.yaml"

#定义data目录的路径
_data_path=base_dir+os.sep+"data_cw"

#定义log目录路径
_log_path=base_dir+os.sep+"logs_cw"

#定义report目录路径
_report_path=base_dir+os.sep+"report_cw"
print('定义report目录路径:',_report_path)

#定义各方法，访问对应的路径
def get_config_path():
    return _config_path #调用、返回Config目录的路径

def get_config_file():
    return _config_file #调用、返回config.yaml文件的路径

def get_data_path():
    return _data_path #调用、返回data目录的路径

def get_db_confile_file():
    return _db_confile_file #调用、返回db_confile.yaml文件的路径

def get_log_path():
    return _log_path #调用、返回log目录路径

def get_report_path():
    return _report_path #调用、返回report目录路径


#2、读取配置文件
class ConfigYaml:#创建类
    #初始化方法-初始yaml读取配置文件
    def __init__(self):
        self.config=YamlReader(get_config_file()).data_red() #读取yaml配置文件-存储日志等级、url、excel、sheet
        self.db_config=YamlReader(get_db_confile_file()).data_red() #读取yaml配置文件-存储数据库连接信息

    #定义各方法获取需要的信息
    def get_excel_file(self): #获取excel文件名称
        return self.config['Base']['test']['case_file']

    def get_excel_sheet(self): #获取测试用例sheet名称
        return self.config['Base']['test']['case_sheet']

    def get_config_url(self): #获取url地址
        return self.config['Base']['test']['url']

    def get_log_level(self): #获取日志级别
        return self.config['Base']['log_level']

    def get_log_extension(self): #获取log文件扩展名
        return self.config['Base']['log_extension']

    def get_db_conf_info(self,db_alias): #获取数据库信息，传入一个参数，指定要连接的数据库
        return self.db_config[db_alias]

    def get_email_info(self): #获取邮件配置相关信息
        return self.config['Email']

if __name__ == '__main__':
    conf_read=ConfigYaml() #初始化类

    print(conf_read.get_excel_file())  #获取excel名称
    print(conf_read.get_excel_sheet())  #获取sheet名称




























































