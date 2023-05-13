
from config import config
import os
from utils.yamlutil import YamlReader
import pytest
from config.config import ConfigYaml
from utils.RequestsUtil import Request

#1、获取测试用例内容
#获取testlogin.yaml文件路径
test_file=os.path.join(config.get_data_path(),"testlogin.yaml")
# print('输出路径：',test_file)

#使用工具类来读取多个文档内容
data_list=YamlReader(test_file).data_red_all()
print(data_list)

@pytest.mark.parametrize("login",data_list)
#2、参数化，执行测试用例
def test_yaml(login):
    #初始化url，data
    url=ConfigYaml().get_config_url()+login['url']
    print('输出url:',url)

    data=login["data"]
    print('输出data：',data)

    #post请求
    request=Request() #初始化类
    res=request.post(url,json=data)
    print('输出res：',res)

    #打印结果


if __name__ == '__main__':
    pytest.main()

    #运行的结果，并未断言、验证















































