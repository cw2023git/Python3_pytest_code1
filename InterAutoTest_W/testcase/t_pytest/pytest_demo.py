
import pytest

#1、创建简单测试方法
"""
1、创建普通方法
2、使用pytest断言的方法
"""
#1、创建普通方法
def func(x):
    return x+1

#2、使用pytest断言的方法
def test_a(): #注意使用pytest方法，方法名必须是以‘test’为开头的
    print("----test_a----")
    assert func(3) == 5 #断言失败

@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_c():
    print("----test_c----")
    assert func(3) == 5 #断言失败

def test_b(): #注意使用pytest方法，方法名必须是以‘test’为开头的
    print("----test_b----")
    assert 1 #断言成功

#2、pytest运行
"""
1、pycharm代码直接执行
2、命令行执行
"""
#代码直接执行
if __name__ == '__main__':
    pytest.main()
    # pytest.main(['pytest_demo.py']) #老师的写法，可能对方版本太低了，4.5.0









































