import os
import yaml


#1、创建类
#2、初始化，文件是否存在
#3、yaml读取

class YamlReader:
    def __init__(self,yamlf):
        if os.path.exists(yamlf): #判断获取的yaml文件是否存在
            self.yamlf=yamlf
        else:
            raise FileExistsError("文件不存在")
        self._data=None #通过这个变量，来确认是否读取过
        self._data_all=None

    #yaml读取(单个文档读取)
    def data_red(self):
        #第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data=yaml.safe_load(f)
        return self._data

    #yaml读取(多个文档读取)
    def data_red_all(self):
        # 第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data_all:
            with open(self.yamlf, "rb") as f:
                self._data_all = yaml.safe_load_all(f)
        return self._data_all




































