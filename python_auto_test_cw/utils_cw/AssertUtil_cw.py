
#-----------------------------------封装断言工具类-----------------------------------

from utils_cw.LogUtil_cw import my_log #导入日志
import json
import pymysql

#封装断言类
class AssertUtil:
    #初始化方法、日志
    def __init__(self):
        self.log=my_log("AssertUtil")

    #封装code相等的断言方法
    def assert_code(self,code,expected_code):#code-实际,expected_code-预期
        try:
            assert int(code)==int(expected_code) #断言
            return True
        except:
            self.log.error('状态码错误，实际状态码：%s，预期状态码：%s'%(code,expected_code))
            raise #抛出异常

    #封装body相等的断言方法
    def assert_body(self,body,expected_body):#body-实际,expected_body-预期
        try:
            assert body==expected_body #断言
            return True
        except:
            self.log.error('body错误，实际body：%s，预期body：%s'%(body,expected_body))
            raise #抛出异常

    #封装body包含的断言方法
    def assert_in_body(self,in_body,expected_in_body):#in_body-实际,expected_in_body-预期
        try:
            # in_body=json.dumps(in_body) #转成json格式数据（此处注释掉，就能正常断言了）
            assert expected_in_body in in_body #断言（in_body是否包含expected_in_body）
            return True
        except:
            self.log.error('不包含或者body错误，实际body：%s，预期body：%s'%(in_body,expected_in_body))
            raise #抛出异常

























































