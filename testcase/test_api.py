
import requests
from common.yaml_util import *

# requests.get()

def test_yaml1():
    aaa=res.json()
    write_yaml("键":aaa) #把接口返回的数据写入yaml文件


def test_yaml2():
    bbb=res.json()
    read_yaml('键') #传入‘键’读取对应的值




























