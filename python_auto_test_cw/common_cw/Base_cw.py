
#-----------------------------------封装基本方法-----------------------------------

from config_cw.Config_cw import ConfigYaml #导入配置文件库
from utils_cw.MysqlUtil_cw import Mysql #数据库连接、断言工具
import json
import re #导入正则
from utils_cw.AssertUtil_cw import AssertUtil #导入断言工具
from utils_cw.LogUtil_cw import my_log #导入日志
import subprocess #导入allure报告中的一种内置方法
from utils_cw.EmailUtil_cw import SendEmail #导入邮件配置


p_data='\${(.*)}\$' #定义‘正则表达式’1
s_data='\&{(.*)}\&' #定义‘正则表达式’2
log=my_log() #日志


#接口用例返回结果内容进行数据库验证
#定义初始化方法
def init_db(db_alias):
    #初始化数据信息，通过配置文件
    db_info=ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])

    #初始化mysql对象
    conn=Mysql(host,user,password,db_name,charset,port)
    print('获取数据库基本信息',conn)
    return conn

#定义数据库断言的方法
def assert_db(db_name,result,db_verify):
    assert_util=AssertUtil() #调用‘断言工具类’

    sql=init_db(db_name) #调用‘初始化方法’

    db_res=sql.fetchone(db_verify) #查询sql、excel文件中各内容

    #数据库的结果与接口返回的结果进行验证
    verify_list=list(dict(db_res).keys()) #获取数据库结果的key

    #根据key，分别获取数据框结果、接口结果
    for line in verify_list:
        res_line=result[line] #获取接口返回结果
        res_db_line=dict(db_res)[line] #获取数据库结果
        assert_util.assert_body(res_line,res_db_line) #验证（两种结果进行验证、断言）

#定义数据转换为json格式方法
def json_pars(data): #传入数据参数-data
    if data: #判断参数-data是否为空
        header=json.loads(data) #转换为json格式
    else:
        header=data #不做转换
    return header #返回

    #return json.loads(data) if data else data #可使用’列表推导‘方式

#动态关联：1、定义’查询‘公共方法
def res_find(data,pattern_data=p_data): #pattern_data=p_data，如果不传参，可以给个默认值-p_data
    pattern=re.compile(pattern_data) #定义‘正则表达式’
    re_res=pattern.findall(data) #根据正则表达式，查找内容（即：查找${rule_id}$中的内容-rule_id）
    return re_res #返回

#静态关联：1、定义’查询‘公共方法
def static_find(data,pattern_data=s_data): #pattern_data=p_data，如果不传参，可以给个默认值-p_data
    pattern=re.compile(pattern_data) #定义‘正则表达式’
    re_res=pattern.findall(data) #根据正则表达式，查找内容（即：查找${rule_id}$中的内容-rule_id）
    return re_res #返回

#动态关联：2、定义’替换‘公共方法
def res_sub(data,replace,pattern_data=p_data):#同样，如果不传参，可以给个默认值-p_data
    pattern=re.compile(pattern_data) #同样，需 定义‘正则表达式’
    re_res=pattern.findall(data) #同样，需根据正则表达式，查找内容
    if re_res: #判断是否存在，存在，才去替换
        return re.sub(pattern_data,replace,data) #替换，pattern_data-格式（即：正则表达式）,
                                                     # replace-你要替换的内容,
                                                     # data-原来的参数
    return re_res #无需替换，返回查询的内容

#静态关联：2、定义’替换‘公共方法
def static_sub(data,replace,pattern_data=s_data):#同样，如果不传参，可以给个默认值-p_data
    pattern=re.compile(pattern_data) #同样，需 定义‘正则表达式’
    re_res=pattern.findall(data) #同样，需根据正则表达式，查找内容
    if re_res: #判断是否存在，存在，才去替换
        return re.sub(pattern_data,replace,data) #替换，pattern_data-格式（即：正则表达式）,
                                                     # replace-你要替换的内容,
                                                     # data-原来的参数
    return re_res #无需替换，返回查询的内容

#动态关联：3、定义’验证‘方法（验证请求中是否有‘${}$’，并返回${}$中的内容）
# def params_find(headers,cookies):
def params_find(params):
    if "${" in params: #判断headers是否存在
        print()
        params=res_find(params) #查找出来

    # if "${" in cookies: #判断cookies是否存在
    #     cookies=res_find(cookies) #查找出来
    # return headers,cookies #返回（同时返回）
    return params #返回（同时返回）

#静态关联：3、定义’验证‘方法（验证请求中是否有‘&{}&’，并返回&{}&中的内容）
def static_params_find(params):
    if "&{" in params: #判断headers是否存在
        print()
        params=static_find(params) #查找出来
    return params #返回（同时返回）

#定义’allure报告‘方法
def allure_report(report_path,report_html):
    allure_cmd="allure generate %s -o %s --clean"%(report_path,report_html) #执行命令
    print('执行命令:',allure_cmd)
    log.info('报告地址')
    try:
        subprocess.call(allure_cmd,shell=True) #allure报告中一种命令
    except:
        log.error("执行用例失败，请检查以下测试环境相关配置")
        raise #抛出异常

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































