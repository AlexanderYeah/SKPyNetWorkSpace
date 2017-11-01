#coding=utf-8;

import ftplib
import os
import socket

#ftp://ygdy8:ygdy8@yg45.dydytt.net:6038/[阳光电影www.ygdy8.com].杀破狼·贪狼.HD.720p.国语中字.mkv
HOST = "ftp:mozilla.org";
DIR = "C/FTPdownload";
FILE = "xiazai.txt";

def main():

    # 1 实例化
    try:
    # 实例化一个ftp 对象
        f = ftplib.FTP(HOST);
    except (socket.error,socket.gaierror) as e:
        print("ERROR:cannot reach %s"%HOST);
        return ;
    print ("have connect host %s"%HOST);
    #
    # #2 登录操作
    # try:
    #     # 直接执行匿名登录操作
    #     f.login();
    # except ftplib.error_perm:
    #     print ("cannot login anonymously");
    #     # 退出操作
    #     f.quit();
    #     return ;
    # print ("has logged as 'anonymous'");
    #
    # # 3 切换到要下载的路径
    # try:
    #     f.cwd(DIR);
    # except ftplib.error_perm:
    #     print ("cannot co change menu");
    # print ("change to target floder successfully");
    #
    #
    # # 4 下载操作
    # try:
    #     f.retrbinary("RETR %s"%FILE,open(FILE,'wb').write);
    #
    # except ftplib.error_perm:
    #     print ("ERROR:cannot read file");
    #     os.unlink(FILE);
    # else:
    #     print ("Download Successful");
    # f.quit();









if __name__ == '__main__':
    main();