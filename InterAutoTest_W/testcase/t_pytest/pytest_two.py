
import pytest

"""
1、创建类型和测试方法
2、创建数据
3、创建参数化
4、运行
"""
# 1、创建类型和测试方法
class TestDemo:
    # 2、创建数据
    data_list=[('xiaoming','123456'),('xiaohong','456789')]

    # 3、创建参数化
    @pytest.mark.parametrize(("name","password"),data_list)
    def test_a(self,name,password):
        print('test_a')
        print(name,password)
        assert 1


# 4、运行
if __name__ == '__main__':
    pytest.main()
























