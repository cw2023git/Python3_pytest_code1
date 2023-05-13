
import os
import pytest

if __name__ == '__main__':
    # pytest.main(['-vs','./testcase'])
    # pytest.main(['-vs','./testcase/test_day1.py']) #指定模块
    # pytest.main(['-vs','./testcase/test_day1.py::Test1::test_1']) #使用nodeid制定类名、函数名
    # pytest.main(['-vs','./testcase/test_day1.py','--reruns=2']) #失败，重跑
    # pytest.main(['-vs','./testcase/test_day1.py','--html=./report/report.html']) #生成html报告
    pytest.main() #使用pytest.ini配置文件（会去读取此配置文件中的各个参数）
    os.system('allure generate ./report_tepm -o ./report_allure --clean')











































