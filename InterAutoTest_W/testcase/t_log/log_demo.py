
import logging #1、导入logging包
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s') #2、设置配置信息
logger=logging.getLogger('log_demo') #3、定义日志名称getlogg
logger.info("info") #4、info、debug(日志等级)
logger.debug("debug")
logger.warning("warning")
















































