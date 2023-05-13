import pytest
from common.yaml_util import *

class Test11:
    #使用数据驱动
    # @pytest.mark.parametrize("参数名","参数值")
    @pytest.mark.parametrize("args_name",read_testcase("get_token.yaml"))

    def test_22(self,args_name):
        print('数据驱动，打印此参数：',args_name)
        #经验证，args_name中的数据是个‘字典’数据，，，因此请求接口所需的数据，可获取改参数中的各个数据
        url=args_name['requests']['url']
        data=args_name['requests']['data']

        #断言
        if "access_token" in res.text:
            write_yaml({"access_token":res.json()["access_token"]})




        print('这是此模块中的冒烟用例22')

    # @pytest.mark.skip   #跳过，无条件跳过
    def test_33(self):
        print('这是此个要跳过的测试用例33')

    # @pytest.mark.skipif(age>=18,'已成年') #跳过，有条件跳过
    def test_44(self):
        print('这是此模块中的冒烟用例44')
        # raise Exception('自定义异常')


if __name__ == '__main__':
    pytest.main()




























