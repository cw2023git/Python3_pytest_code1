
from utils.LogUtils import my_log
import json,pymysql

#1、定义封装类
class AssertUtil:
    #2、初始化数据，日志
    def __init__(self):
        self.log=my_log('AssertUtil')

    #3、code相等的方法
    def assert_code(self,code,expected_code):
        """
        验证码返回状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int(code)==int(expected_code)
            return True
        except:
            self.log.error('状态码错误，实际状态码：%s,预期状态码：%s'%(code,expected_code))
            raise #抛出异常

    #4、body相等的方法【数据库结果验证时，调用的方法】
    def assert_body(self,body,expected_body):
        """
        验证返回结果内容相等
        :param body:
        :param expected_body:
        :return:
        """
        try:
           assert body==expected_body
           return True
        except:
            self.log.error('body错误，实际body：%s,预期body：%s'%(body,expected_body))
            raise #抛出异常

    #5、body包含的方法
    def assert_in_body(self,in_body,expected_in_body):
        """
        验证返回结果是否包含期望的结果
        :param in_body:
        :param expected_in_body:
        :return:
        """
        try:
            in_body=json.dumps(in_body) #转成json格式
            assert expected_in_body in in_body
            return True
        except:
            self.log.error('不包含或者body是错误，实际body：%s，期望body：%s'%(in_body,expected_in_body))
            raise #抛出异常
















































