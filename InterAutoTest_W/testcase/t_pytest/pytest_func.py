
import pytest

"""
1、定义类
2、创建测试方法（注意：以test开头）
3、创建setup和teardown
4、运行查看结果
"""
# 1、定义类
class TestFunc:
    # 3、创建setup和teardown
    def setup(self):#此方法名固定的
        print('---setup---')
    def teardown(self):#此方法名固定的
        print('---teardown---')

    # 2、创建测试方法（注意：以test开头）
    def test_a(self):
        print('test_a')
    def test_b(self):
        print('test_b')

# 4、运行查看结果
if __name__ == '__main__':
    pytest.main()






















