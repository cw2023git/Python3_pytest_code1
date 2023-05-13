
import yaml

"""
1、创建yaml格式文件
2、读取这个文件
3、输出这个文件
"""


#读取单个文件：
#1、导入yaml包
# with open("./data.yaml","r",encoding="utf-8") as f: #2、打开文件，使用encoding="utf-8"解决编码问题
#      r=yaml.safe_load(f) #3、使用yaml读取文件
#      print(r) #4、输出文件内容

#读取多个文件
#1、编辑或修改data.yaml
#2、yaml读取方法，all
#3、循环打印
# with open("./data.yaml","r",encoding="utf-8") as f: #2、打开文件，使用encoding="utf-8"解决编码问题
#      r=yaml.safe_load_all(f) #3、使用yaml读取文件
#      for i in r:
#         print(i) #4、输出文件内容

from utils.yamlutil import YamlReader
#调用yaml读取这一封装的方法
# res=YamlReader("./data.yaml").data_red() #读取单个文件
res=YamlReader("./data.yaml").data_red_all() #读取多个文件
print(res)




















