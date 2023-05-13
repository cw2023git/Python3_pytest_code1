
#-----------------------------------封装excel列属性方法-----------------------------------

#封装类（注意：此处可优化为自动获取excel各列属性名）
class DataConfig:
    #定义各列属性
    case_id='用例ID'
    case_model='模块'
    case_name='接口名称'
    url='请求URL'
    pre_exec='前置条件'
    # obtain_content='获取内容' #获取前置用例中指定的内容，用于替换
    method='请求类型'
    params_type='请求参数类型'
    params='请求参数' #（不管是post对应‘data’，还是get对应‘params’）
    expect_result='预期结果'
    actual_result='实际结果'
    is_run='是否运行'
    headers='headers'
    cookies='cookies'
    code='status_code'
    db_verify='数据库验证'






























