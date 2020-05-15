#!usr/bin/ python
#-*- coding:utf-8 _*-

import socket

def send_msg(udp_socket):
    #发送消息
    #获取要发送的内容
    dest_ip = input("请输入对方的ip: ")
    dest_port = int(input("请输入对方的port: "))
    send_data = input("请输入要发送的内容: ")
    udp_socket.sendto(send_data.encode("GBK"),(dest_ip,dest_port))

def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s : %s" %(str(recv_data[1]),recv_data[0].decode("GBK")))

def main():
    #创建套接字
    upd_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #绑定信息
    upd_socket.bind(("",7666))

    #循环收发数据

    while True:
        print("-----xxx聊天器------")
        print("1:发送数据")
        print("2.接收数据")
        print("0.退出系统")
        op = input("请输入功能: ")

        if op == "1":
            #发送
            send_msg(upd_socket)

        elif op == "2":
            #接收并显示
            recv_msg(upd_socket)

        elif op == "0":
            break
        else:
            print("输入有误,请重新输入...")


if __name__ == "__main__":
    main()