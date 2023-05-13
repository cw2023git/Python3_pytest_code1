
#封装成一个py文件，可以给所有用例文件提供使用

import pytest

@pytest.fixture(scope='function')

# def my_user(request):
def my_user():
    print('my_user的前置方法')
    # yield request.param  #显示如下：test_day1.py::Test1::test_1[cl] 前置方法
    yield
    print('my_user的后置方法')











































