
#-----------------------------------主程序-----------------------------------

import os
import pytest
from config_cw import Config_cw #导入整个配置文件
from common_cw import Base_cw #导入基本方法
import logging.config

log_conf='./logs_cw/logs_cw.conf' #日志配置表的路径
logging.config.fileConfig(log_conf) #加载日志配置表
logging=logging.getLogger() #log采集对象，生成log

if __name__ == '__main__':
    print('你好，世界')
    logging.info('---------开始执行钉钉-积分系统-API自动化测试---------')
    #运行方法2：
    report_path = Config_cw.get_report_path() + os.sep + 'result' #拼接目录名称，存放测试结果
    report_html_path = Config_cw.get_report_path() + os.sep + 'html' #拼接目录名称，存放测试报告文件

    pytest.main(['-s', '--alluredir', report_path]) #运行

    #会在jenkins中进行配置，此处无需编写了
    Base_cw.allure_report(report_path,report_html_path) #自动成成测试报告(不过，我在这边直接用)
    logging.info('---------结束执行钉钉-积分系统-API自动化测试---------')




























