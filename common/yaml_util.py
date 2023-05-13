
import os,yaml

#读取、写入、清空等，都是固定写法

#读取
def read_yaml(key):
    with open(os.getcwd()+'./yaml_file.yaml',mode='r',encoding='utf-8') as f:
         value=yaml.load(stream=f,Loader=yaml.FullLoader)
         return value[key]


#写入
def write_yaml(data):
    with open(os.getcwd()+'./yaml_file.yaml',mode='a',encoding='utf-8') as f:
         yaml.dump(data,stream=f,allow_unicode=True)

#清空
def clear_yaml():
    with open(os.getcwd()+'./yaml_file.yaml',mode='w',encoding='utf-8') as f:
         f.truncate()

#读取测试用例
def read_testcase(yaml_name):
    with open(os.getcwd()+'/testcase/'+yaml_name,mode='r',encoding='utf-8') as f:
         value=yaml.load(stream=f,Loader=yaml.FullLoader)
         return value

'''
f：表示文件对象，把打开的文件保存到‘f’

'''































