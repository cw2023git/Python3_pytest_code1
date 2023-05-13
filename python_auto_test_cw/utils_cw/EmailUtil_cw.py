
#-----------------------------------封装邮件配置工具类-----------------------------------


from email.mime.multipart import MIMEMultipart #导入邮件-MIMEMultipart库
from email.mime.text import MIMEText #导入邮件-MIMEText库
import smtplib #导入

#数据初始化
#1、smtp地址、用户名、密码、接收邮件者、邮件标题、邮件内容、邮件附件
class SendEmail:
    #初始化方法
    def __init__(self,smtp_adder,username,password,recv,title,content=None,file=None):
        self.smtp_adder=smtp_adder #smtp地址
        self.username=username #用户名
        self.password=password #密码
        self.recv=recv #接收邮件者
        self.title=title #邮件标题
        self.content=content #邮件内容
        self.file=file #邮件附件

    #定义发送邮件方法
    def send_mail(self):
        #MIMEMultipart，需导入此库
        msg=MIMEMultipart()

        #1、初始化邮件信息
        msg.attach(MIMEText(self.content,_charset='utf-8'))
        msg['subject']=self.title #邮件标题
        msg['From']=self.username #邮件发送者
        msg['To']=self.recv #邮件接收者

        #邮件附件
        #判断是否有附件
        if self.file:
           att=MIMEText(open(self.file).read()) #MIMEText读取文件
           att['Content-Type']='application/octet-stream' #设置内容类型
           att['Content-Disposition']='attachment;filename="%s"'%self.file #设置附件头
           msg.attach(att) #将内容附加到邮件主体中

        #2、登录邮件服务器
        self.smtp=smtplib.SMTP(self.smtp_adder,port=25) #创建smtp对象（port默认是25）
        self.smtp.login(self.username,self.password) #登录邮件服务器

        #3、发送邮件
        self.smtp.sendmail(self.username,self.recv,msg.as_string())

if __name__ == '__main__':
    #初始化类（smtp_adder,username,password,recv,title,content=None,file=None）
    from config.config import ConfigYaml
    email_info=ConfigYaml().get_email_info()
    smtp_adder=email_info['smtpserver']
    username=email_info['username']
    password=email_info['password']
    recv=email_info['receiver']

    email=SendEmail(smtp_adder,username,password,recv,'测试') #初始化类
    email.send_mail() #发送邮件

    #2-11-3 邮件配置-邮件配置之运行
    #1、封装公共方法
    #2、应用测试发送





