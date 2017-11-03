#coding=utf-8;

# 发送邮件和生成邮件使用的类库
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 设置发件的服务器地址
SMTPSVR = "smtp.163.com";
# 设置发送者的邮件地址
From = "yeshengke@163.com";
# 设置接收者的邮件地址
To = "1023954998@qq.com";
# 发送者的密码
PASSWORD = "";



# 1 生成一个多部分邮件信息 参数是邮件的名字
def make_mpa_msg():
    # 两部分 一部分是纯文本 一部分是附件内容
    # alternative 参数来实例化这个类
    email = MIMEMultipart('alternative');
    # 传入参数plain
    text = MIMEText('Hello handsome man!!!','plain');
    email.attach(text);
    # HTML 内容  和  text 是等价的 ，基于web 的显示HTML 内容
    # 基于命令行的话显示的是纯文本内容 传入参数 是html
    html = MIMEText('<html><body><h4>Hello handsome man!!!</h4></body></html>','html');
    email.attach(html);
    return email;


# 2 发送操作
# 传入参数 来自谁  发送给谁 消息
def send_msg(fr,to,msg):
    # qq 邮箱的端口号 587 或者 465
    s = smtplib.SMTP(SMTPSVR)

    # 登录操作
    s.login(From,PASSWORD);
    errs = s.sendmail(fr,to,msg);
    print ("send mail successfully");
    s.quit();


if __name__ == '__main__':
    print ("will send alternative mail");
    msg = make_mpa_msg();
    msg["From"] = From;
    msg["To"] = To;
    msg["Subject"] = 'QQYE';

    send_msg(From,To,msg.as_string());









