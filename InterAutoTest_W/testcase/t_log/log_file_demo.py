
import logging

#输出控制台

logger=logging.getLogger("log_file_demo")#1、设置logger名称
logger.setLevel(logging.INFO) #2、设置log级别
fh_stream=logging.StreamHandler()#3、创建handler

#写入文件
fh_file=logging.FileHandler('./test.log')

fh_stream.setLevel(logging.INFO)#4、设置日志级别
fh_file.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')#5、定义输出格式
fh_file.setFormatter(formatter)
fh_stream.setFormatter(formatter)

logger.addHandler(fh_stream)#6、添加handler
logger.addHandler(fh_file)
logger.info('这是一个日志级别')#7、运行输出
logger.debug('这是一个debug')













































