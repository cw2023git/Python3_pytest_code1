
#-----------------------------执行用例并生成测试报告功能的封装-----------------------------
import time
import unittest
import logging.config
from BeautifulReport import BeautifulReport
# from test_data.yaml_data.mysql_data import * #暂时用不上
# import yaml

test_dir='./dingding_test_case'     #测试用例模块的路径
report_dir='./dingding_reports' #存放生成的测试报告文件

log_conf='./dingding_log/log_dingding.conf' #日志配置表的路径
logging.config.fileConfig(log_conf) #加载日志配置表
logging=logging.getLogger() #log采集对象，生成log

"""
#目前暂时用不上

#数据初始化
db=DB() #实例化类，生成对象
yaml_data=open('./test_data/yaml_data/data.yaml','r',encoding='UTF-8') #打开yaml文件
data=yaml.load(yaml_data) #把yaml数据格式转化为python数据格式
db.init_data(data) #调用init_data()方法，开始进行初始化数据
"""

logging.info('--------------------------------------开始执行钉钉功道云绩效API自动化测试--------------------------------------')
time.sleep(1) #延迟1秒，效果更好
print() #换行

#加载测试用例模块
# discover=unittest.defaultTestLoader.discover(test_dir,'test_case_c_*.py') #运行单个文件
discover=unittest.defaultTestLoader.discover(test_dir,'test_case_*.py') #运行全部文件

#构造生成测试报告的名称
now_time=time.strftime('%Y-%m-%d %H-%M-%S ') #获取当前系统时间
# report_name=report_dir+'/'+now_time+'dingding_api_report（测试环境）.html' #完整的测试报告名称-测试环境
report_name=report_dir+'/'+now_time+'-dingding_api_report（正式环境）.html' #完整的测试报告名称-正式环境

#运行测试用例模块，并生成漂亮的测试报告
# BeautifulReport(discover).report(filename=report_name,description='钉钉功道云绩效API自动化测试报告（测试环境）') #测试环境
BeautifulReport(discover).report(filename=report_name,description='钉钉功道云绩效API自动化测试报告（正式环境）') #正式环境

print() #换行

logging.info('--------------------------------------钉钉功道云绩效API自动化测试已执行完毕，请查看测试报告--------------------------------------')

