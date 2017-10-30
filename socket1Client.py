#coding=utf-8;

from socket import  *
from  time import ctime

HOST = "127.0.0.1";
PORT = 21567;
BUFSIZE = 1024;
ADDR = (HOST,PORT);

# 建立一个tcp socket
tcpCliSocket = socket(AF_INET,SOCK_STREAM);
tcpCliSocket.connect(ADDR);

# 循环
while True:
    data = input('>>');
    if not data:
        break;
    # 如果用户输入数据 就进行发送到server
    data = data.encode('utf-8');
    tcpCliSocket.send(data);
    data = tcpCliSocket.recv(BUFSIZE);
    if not  data:
        break;
    print (data.decode('utf-8'));
    # 接受到数据就关闭的话，那么程序 不管是客户端还是服务端，只能执行一次，所以注释掉关闭的代码 就可以持续通信
#tcpCliSocket.close();


