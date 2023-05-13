
from config.config import ConfigYaml
from utils.MysqlUtil import Mysql
import json
import re #正则
from utils.AssertUtil import AssertUtil
from utils.LogUtils import my_log
import subprocess
from utils.EmailUtil import SendEmail

p_data='\${(.*)}\$' #定义好正则表达式
log=my_log()


#1、初始化数据库信息，在‘common’中创建Base.py文件

#2、接口用例返回结果内容进行数据库验证
#1、定义init_db
def init_db(db_alias):

  #2、初始化数据库信息，通过配置文件
  db_info=ConfigYaml().get_db_conf_info(db_alias)
  host=db_info["db_host"]
  user=db_info["db_user"]
  password=db_info["db_password"]
  db_name=db_info["db_name"]
  charset=db_info["db_charset"]
  port=int(db_info["db_port"])

  #3、初始化mysql对象
  conn=Mysql(host,user,password,db_name,charset,port)
  print(conn)
  return conn

def assert_db(db_name,result,db_verify):
    assert_util=AssertUtil()

    #1、初始化数据库
    # sql = init_db("db_1")
    sql = init_db(db_name)

    #2、查询sql、excel定义好的
    db_res = sql.fetchone(db_verify)
    # log.debug("数据库查询结果:{}".format(str(db_res)))  # format-

    #3、数据库的结果与接口返回的结果验证
    #（1）获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    #（2）根据key，获取数据库结果，接口结果
    for line in verify_list:
        # res_line = res["body"][line]  # 获取接口的结果
        res_line = result[line]  #获取接口的结果

        res_db_line = dict(db_res)[line]  # 获取数据库的结果

        #（3）验证
        assert_util.assert_body(res_line, res_db_line)

def json_pars(data):
  """
  格式化字符，转换json
  :param data:
  :return:
  """
  # if data:
  #   header = json.loads(data)
  # else:
  #   header = data

  #可使用列表推导方式
  return json.loads(data) if data else data

#动态关联：1、定义查询的公共方法
def res_find(data,pattern_data=p_data):
    """
    查询
    :param data:
    :param pattern_data:
    :return:
    """
    # pattern=re.compile('\${(.*)}\$')
    pattern=re.compile(pattern_data)
    re_res=pattern.findall(data)
    return re_res

#动态关联：2、定义替换的公共方法
def res_sub(data,replace,pattern_data=p_data):
  """
  替换
  :param data:
  :param replace:
  :param pattern_data:
  :return:
  """
  pattern = re.compile(pattern_data)
  re_res = pattern.findall(data)
  if re_res:#判断存在
    return re.sub(pattern_data,replace,data)
  return re_res


#动态关联：3、定义验证请求中是否有‘${}$’，返回${}$中的内容的公共方法
def params_find(headers,cookies):
  """
  #验证请求中是否有${}$需要结果关联
  :param headers:
  :param cookies:
  :return:
  """
  if "${" in headers: #判断headers存在
    headers=res_find(headers) #查找出来

  if "${" in cookies: #判断cookies存在
    cookies=res_find(cookies) #查找出来
  return headers,cookies

#Allure报告，subprocess
def allure_report(report_path,report_html):
    """
    生成allure报告
    :param report_path:
    :param report_html:
    :return:
    """
    #1、执行命令 allure generate
    # allure_cmd="allure generate report/result -o report/html --clean"
    allure_cmd="allure generate %s -o %s --clean"%(report_path,report_html)
    #2、subprocess.call()
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("执行用例失败，请检查以下测试环境相关配置")
        raise

#定义发送邮件公共方法
def send_email(report_html_path="",content="",title="测试"):
    """
    发送邮件
    :param report_html_path:
    :param content:
    :param title:
    :return:
    """
    #初始化类（smtp_adder,username,password,recv,title,content=None,file=None）
    email_info = ConfigYaml().get_email_info()
    smtp_adder = email_info['smtpserver']
    username = email_info['username']
    password = email_info['password']
    recv = email_info['receiver']

    email = SendEmail(smtp_adder=smtp_adder,
                      username=username,
                      password=password,
                      recv=recv,
                      title=title,
                      content=content,
                      file=report_html_path)  #初始化类

    email.send_mail()  #发送邮件



if __name__ == '__main__':
    # init_db("db_1")
    res_find_output=res_find('{"Authorization":"JWT ${token}$"}')
    print('输出结果：',res_find_output) #输出结果： ['token']

    res_sub_output=res_sub('{"Authorization":"JWT ${token}$"}',"123") #替换
    print('输出结果：',res_sub_output)





































