#!usr/bin/ python
#-*- coding:utf-8 _*-

import socket

def send_msg(udp_socket):
    """发送信息"""
    #1.获取要发送的内容

    dest_ip = input("请输入对方的ip: ")
    dest_port = int(input("请输入对方的port: "))
    send_data = input("请输入要发送的数据: ")
    udp_socket.sendto(send_data.encode("GBK"),(dest_ip,dest_port))

def recv_msg(udp_socket):

    #接收数据
    recv_data = udp_socket.recvfrom(1024)
    print("%s : %s" %(str(recv_data[1]),recv_data[0].decode("GBK")))


def main():
    #创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #绑定信息
    udp_socket.bind(("",7789))

    #循环收发数据
    while True:
        #发送
        send_msg(udp_socket)

        #接收并显示
        recv_msg(udp_socket)

if __name__ == "__main__":
    main()