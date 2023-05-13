
#封装成一个py文件，可以给所有用例文件提供使用

import pytest
from common.yaml_util import *

@pytest.fixture(scope='function')

# def my_all(request):
def my_all():
    print('my_all的前置方法')
    # yield request.param  #显示如下：test_day1.py::Test1::test_1[cl] 前置方法
    yield
    print('my_all的后置方法')


#在所有的接口请求之前执行
@pytest.fixture(scope='session',autouse=True)
def my_all():
    clear_yaml()






































