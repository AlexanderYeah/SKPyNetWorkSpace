#coding=utf-8;

import ftplib
import os
import socket

# 此处是IP地址的话，不需要带ftp前缀，要不总是连接失败
HOST = "172.16.102.119";
# 到指定的文件夹下载一个txt文件
DIR = "/Users/zhengfangnan/Desktop/ForAlexFtp";
FILE = "xiazai.txt";
#  上传的文件夹 路径已经省略
UPLOADDIR ="/Users//Desktop/ForAlexFtp/UploadFolder"
LOCALPATH = "/Users//Desktop/SKPy/SKPyNetWorkSpace/willUpload.txt"
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
    try:
        # 直接执行匿名登录操作
        # 登录的是已经设置的账户
        # 密码用户名都要输入
        f.login("","");
    except ftplib.error_perm:
        print ("cannot login anonymously");
        # 退出操作
        f.quit();
        return ;
    print ("has logged as 'username'");
    #
    # 3 切换到要下载的路径
    try:
        f.cwd(DIR);
    except ftplib.error_perm:
        print ("cannot co change folder %s" % DIR);
    print ("change to target floder successfully");

    #
    # 4 下载操作 就下载到当前目录了
    try:
        f.retrbinary("RETR %s"%FILE,open(FILE,'wb').write);

    except ftplib.error_perm:
        print ("ERROR:cannot read file");
        os.unlink(FILE);
    else:
        print ("Download  %s Successful" % FILE);



    # 5 创建文件夹
    try:
        f.cwd(UPLOADDIR);
    # 进入文件夹失败 证明没有此文件夹 就要创建一个文件夹
    except ftplib.error_perm:
        try:
            f.mkd(UPLOADDIR);
        except ftplib.error_perm:
            print ("you have no authority to make dir");
        print ("create folder successfully");
    # 成功进入 下一步操作
    # 5.1 读取当前文佳夹的txt 文本 进行上传
    willUploadFile = open(LOCALPATH,'rb');

    # 5.2 进行上传 使用sortline 函数
    try:
        # 给FTP 命令 进行上传文件 后面跟上文件的名字
        f.storlines("STOR %s"%"129.txt", willUploadFile);
        # 上传完毕 关闭文件
        willUploadFile.close()
        print ("you have upload a file successfully!!!");
    except ftplib.error_perm:
        print ("upload error occur");


    #6 删除指定远程目录的文件
    deleteTargetFile = UPLOADDIR + "/128.txt";
    try:
        f.delete(deleteTargetFile);
        print ("you have delete %s"%deleteTargetFile);
    # 如果远程目录没有此文件 就会进行报错
    except ftplib.error_perm:
        print ("delete file error occur");

    #7 获取指定目录下面的所有文件
    try:
        f.dir(UPLOADDIR);
        print ("got dir successfully");
    except ftplib.error_perm:
        print ("got dir error happened");



if __name__ == '__main__':
    main();