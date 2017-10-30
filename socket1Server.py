#coding=utf-8;

from socket import  *
from time import  ctime

# 1设置端口号 地址 和 缓存内存
HOST = '';
PORT = 21567;
BUFSIZE = 1024;
ADDR = (HOST,PORT);

#2 创建tcp socket 链接
tcpServerSock = socket(AF_INET,SOCK_STREAM);
# 绑定地址
tcpServerSock.bind(ADDR);
# 监听连接
tcpServerSock.listen(5);

# 3 就是无限的循环 知道监听到客户端的数据
while True:
    print ("waiting connection from client.....");
    # 一旦服务器接受了一个连接 就会利用accept 返回一个独立的客户端套接字,
    # 用来与即将到来的消息进行交换 这一步仅仅是建立连接
    tcpCliSocket,addr = tcpServerSock.accept();
    print ("have connected from:",addr);
    while True:
        # 接受tcp 消息
        data = tcpCliSocket.recv(BUFSIZE);
        if not data:
            # 如果为空 证明客户端没有发送消息 接着循环 进行监听
            break;
        # 不为空   返回接收到的数据给客户端
        str = "i have receive your data";
        data2 = str.encode('utf-8');
        tcpCliSocket.send(data2);

        # 关闭
     #   tcpCliSocket.close();


   # tcpServerSock.close();




