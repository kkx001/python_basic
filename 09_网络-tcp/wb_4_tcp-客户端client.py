#!usr/bin/ python
#-*- coding:utf-8 _*-

import socket
def main():
    #1.创建tcp套接字
    tcp1_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.链接服务器
    #tcp_socket.connect(("192.168.1.101",7890))

    server_ip = input("请输入要连接的服务器的ip: ")
    server_port = int(input("请输入要连接的服务器的port: "))
    server_addr = (server_ip,server_port)
    tcp1_socket.connect(server_addr)

    #3.要发送数据/接收数据
    send_data = input("输入要发送的数据: ")
    tcp1_socket.send(send_data.encode("GBK"))

    #4.关闭套接字
    tcp1_socket.close()

if __name__ == "__main__":
    main()