
#封装成一个py文件，可以给所有用例文件提供使用

import pytest

@pytest.fixture(scope='function')

# def my_product(request):
def my_product():
    print('my_product的前置方法')
    # yield request.param  #显示如下：test_day1.py::Test1::test_1[cl] 前置方法
    yield
    print('my_product的后置方法')











































