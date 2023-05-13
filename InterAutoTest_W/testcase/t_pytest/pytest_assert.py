# coding=UTF-8

import pytest

# 常用断言：
# 判断xx为真  assert xx
#1、定义方法进行assert
def test_1():
    a=True
    assert a

# 判断xx不为真 assert not xx
def test_2():
    a=False
    assert a

# 判断b包含a assert a in b
def test_3():
    a='hello'
    b='hello world'
    assert a in b

# 判断a等于b assert a==b
def test_4():
    a=b='hello'
    assert a == b

# 判断a不等于b assert a!=b
def test_5():
    a='hello'
    b='hello world'
    assert a != b

#2、运行查看结果
if __name__ == '__main__':
    pytest.main()





























