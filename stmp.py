#coding=utf-8;

from smtplib import SMTP
from poplib import POP3
from time import  sleep
"""
    SMTP 的使用过程
    1>连接到服务器
    2>登录（可选）
    3>发出服务请求
    4>退出

    SMTP 是发送邮件使用的
"""

"""
    下载邮件的协议 邮局协议 POP
    1>连接到服务器
    2>登录（可选）
    3>发出服务请求
    4>退出

"""

SMTPSVR = 'smtp.163.com';
POP3SVR = 'pop.163.com';

# 发送目的地
who = 'yeshengke@163.com';
# 这里写你的密码
password = '';
# 主题和正文之间要回车以下，要不发布出去
origMsg = '''\
From:%(who)s
TO:%(who)s
Subject: hello alexander

Hello Such a handsome man!
'''%{'who':who};
# 当然 如果邮件中有
# 中文的话 要进行utf-8 转码
#origMsg = origMsg.encode("utf-8");
# 以下代码是使用SMTP 完成邮件的发送
# 实例化一个SMTP 对象
sendSvr = SMTP(SMTPSVR);
# 进行登录操作
sendSvr.login(who,password)
# 进行发送 第一个参数是 from 来自谁  第二个参数是to 发送给谁，可以是列表
# origmsg 代表邮件整体
errs = sendSvr.sendmail(who,[who],origMsg);
sendSvr.quit();
# 断言 如果有错误，则会触发错误发生
assert len(errs) == 0,errs
print ("send mail successfully");
# 睡一会，等待邮件进行投递
sleep(10);


# 以下代码是用POP3 拉取邮件
# 实例化
receiveSvr = POP3(POP3SVR);
# 用户名 和 密码
receiveSvr.user(who);
receiveSvr.pass_(password);
# 获取邮件列表
mail_list = receiveSvr.stat();
# 进行下载第一个邮件 就是最新的邮件
# retr 方法 从服务器中获取消息，并且设置为已读的状态，返回一个长度为3 的元组
# 分别是服务器的响应 消息的所有行 消息的字节数
rsp,msg,siz = receiveSvr.retr(mail_list[0]);
# 邮件头和 正文使用空白符 分隔
#sep = msg[-1];
# # 获取正文
receiveBody = msg[-1];
print (receiveBody);


# 以下是国内其他邮件服务商

'''
gmail(google.com)
POP3服务器地址:pop.gmail.com（SSL启用 端口：995）
SMTP服务器地址:smtp.gmail.com（SSL启用 端口：587）

21cn.com:
POP3服务器地址:pop.21cn.com（端口：110）
SMTP服务器地址:smtp.21cn.com（端口：25）

sina.com:
POP3服务器地址:pop3.sina.com.cn（端口：110）
SMTP服务器地址:smtp.sina.com.cn（端口：25）

tom.com:
POP3服务器地址:pop.tom.com（端口：110）
SMTP服务器地址:smtp.tom.com（端口：25）

163.com:
POP3服务器地址:pop.163.com（端口：110）
SMTP服务器地址:smtp.163.com（端口：25）

263.net:
POP3服务器地址:pop3.263.net（端口：110）
SMTP服务器地址:smtp.263.net（端口：25）

yahoo.com:
POP3服务器地址:pop.mail.yahoo.com
SMTP服务器地址:smtp.mail.yahoo.com

263.net.cn:
POP3服务器地址:pop.263.net.cn（端口：110）
SMTP服务器地址:smtp.263.net.cn（端口：25）

Foxmail：
POP3服务器地址:POP.foxmail.com（端口：110）
SMTP服务器地址:SMTP.foxmail.com（端口：25）

sinaVIP
POP3服务器:pop3.vip.sina.com （端口：110）
SMTP服务器:smtp.vip.sina.com （端口：25）

sohu.com:
POP3服务器地址:pop3.sohu.com（端口：110）
SMTP服务器地址:smtp.sohu.com（端口：25）

etang.com:
POP3服务器地址:pop.etang.com
SMTP服务器地址:smtp.etang.com

x263.net:
POP3服务器地址:pop.x263.net（端口：110）
SMTP服务器地址:smtp.x263.net（端口：25）

yahoo.com.cn:
POP3服务器地址:pop.mail.yahoo.com.cn（端口：995）
SMTP服务器地址:smtp.mail.yahoo.com.cn（端口：587）
雅虎邮箱POP3的SSL不启用端口为110，POP3的SSL启用端口995；SMTP的SSL不启用端口为25，SMTP的SSL启用端口为465

QQ邮箱 QQ企业邮箱
POP3服务器地址：pop.qq.com（端口：110） POP3服务器地址：pop.exmail.qq.com （SSL启用 端口：995）
SMTP服务器地址：smtp.qq.com （端口：25） SMTP服务器地址：smtp.exmail.qq.com（SSL启用 端口：587/465）
SMTP服务器需要身份验证

126邮箱 HotMail
POP3服务器地址:pop.126.com（端口：110） POP3服务器地址：pop.live.com （端口：995）
SMTP服务器地址:smtp.126.com（端口：25） SMTP服务器地址：smtp.live.com （端口：587）

china.com: 139邮箱
POP3服务器地址:pop.china.com（端口：110） POP3服务器地址：POP.139.com（端口：110）
SMTP服务器地址:smtp.china.com（端口：25） SMTP服务器地址：SMTP.139.com(端口：25)

'''






