import os
from utils.yamlutil import YamlReader

#1、获取项目基本目录
#获取当前项目的绝对路径
current=os.path.abspath(__file__)
print(current)
base_dir=os.path.dirname(os.path.dirname(current))
print(base_dir)
#定义config目录的路径
_config_path=base_dir+os.sep+"config"

#定义data目录的路径
_data_path=base_dir+os.sep+"data"

#定义config.yaml文件的路径
_config_file=_config_path+os.sep+"config.yaml"

#定义db_conf.yaml文件的路径
_db_config_file=_config_path+os.sep+"db_conf.yaml"

#定义log文件路径
_log_path=base_dir+os.sep+"logs"

#定义report目录的路径
_report_path=base_dir+os.sep+"report"

def get_report_path():
    """
    获取report绝对路径
    :return:
    """
    return _report_path

def get_data_path():
    return _data_path

def get_db_config_file():
    return _db_config_file

def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

def get_log_path():
    """
    获取log文件路径
    :return
    """
    return _log_path

#2、读取配置文件
class ConfigYaml: #创建类
   def __init__(self):  #初始yaml读取配置文件
       self.config=YamlReader(get_config_file()).data_red() #读取yaml文件内容，并返回、赋值
       self.db_config=YamlReader(get_db_config_file()).data_red()

   #定义方法获取需要信息
   def get_excel_file(self):
       """
       获取测试用例excel名称
       :return:
       """
       return self.config["base"]["test"]["case_file"] #读取yaml文件中对应的值，并返回

   def get_excel_sheet(self):
       """
       获取测试用例sheet名称
       :return:
       """
       return self.config["base"]["test"]["case_sheet"] #读取yaml文件中对应的值，并返回

   def get_config_url(self):
       return self.config["base"]["test"]["url"]

   def get_conf_log(self):
       """
       获取日志级别
       :return:
       """
       return self.config['base']['log_level']

   def get_conf_log_extension(self):
       """
       获取文件扩展名
       :return:
       """
       return self.config['base']['log_extension']

   def get_db_conf_info(self,db_alias):
       """
       根据db_alias获取该名称下的数据库信息
       :param db_alias:
       :return:
       """
       return self.db_config[db_alias]

   def get_email_info(self):
       """
       获取邮件配置相关信息
       :return:
       """
       return self.config['email']

if __name__ == '__main__':
    conf_read=ConfigYaml()
    # print(conf_read.get_config_url())
    # print(conf_read.get_conf_log())
    # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_conf_info("db_1")) #连接，访问数据库1

    #问题：如果说我们测试的系统是’分布式‘的，需要验证、访问多个不同的数据库，此时该如何办？
    #解决如下（我丢，我还以为有什么高见呢）：
    # print(conf_read.get_db_conf_info("db_1")) #连接，访问数据库1
    # print(conf_read.get_db_conf_info("db_2")) #连接，访问数据库2
    # print(conf_read.get_db_conf_info("db_3")) #连接，访问数据库3

    # print(conf_read.get_excel_file()) #获取excel名称
    # print(conf_read.get_excel_sheet()) #获取sheet名称
    print(conf_read.get_email_info()) #获取邮件配置信息






















