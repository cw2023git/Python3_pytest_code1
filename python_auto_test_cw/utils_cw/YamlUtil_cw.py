
#-----------------------------------封装读取yaml工具类-----------------------------------
import os
import yaml

class YamlReader:
    #初始化
    def __init__(self,yamlf):
        if os.path.exists(yamlf): #判断文件是否存在
            self.yamlf=yamlf
        else:
            raise FileExistsError("文件不存在！")
        self._data=None #私有的，通过此变量，确认是否读取
        self._data_all=None #私有的，通过此变量，确认是否读取

    #yaml读取（单个文档读取）
    def data_red(self):
        #第一次调用_data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data: #判断_data是否存在，如果不存在，就读取，如果已存在，直接返回
            with open(self.yamlf,'rb') as f:
                self._data=yaml.safe_load(f)
        return self._data #返回

    #yaml读取（多个文档读取）
    def data_red_all(self):
        #第一次调用_data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data_all:
            with open(self._data_all,'rb') as f:
                self._data_all=yaml.safe_load_all(f)
        return self._data_all #返回












































