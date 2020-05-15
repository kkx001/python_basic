#!usr/bin/ python
#-*- coding:utf-8 _*-

import socket

def main():
    #1.买个手机(创建套接字socket)
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.插入手机卡(绑定信息)
    tcp_server_socket.bind(("",7878))

    #3.将手机设置为正常(让默认的套接字有主动变为被动listen)
    tcp_server_socket.listen(128)

    print("-----1-----")

    #4.等待别人电话到来(等待客户端的链接accept)
    new_client_socket,client_addr = tcp_server_socket.accept()

    print("-----2-----")
    print(client_addr)

    #接收客户点发来的请求
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    #回送一部分数据
    new_client_socket.send("---hahaha----0k----".encode("GBK"))

    #关闭套接字
    new_client_socket.close()
    tcp_server_socket.close()
if __name__ == "__main__":
    main()