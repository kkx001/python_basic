#!usr/bin/ python
#-*- coding:utf-8 _*-
import threading
import time

def test1(temp):
    temp.append(33)
    print("---in test1 temp =%s" %temp)

def test2(temp):
    print("---in test2 temp = %s"%temp)

g_num = [11,22]


def main():
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用 函数的时候 传递什么数据过去
    t1 = threading.Thread(target=test1,args=(g_num,))
    t2 = threading.Thread(target=test2,args=(g_num,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("----in main Thread g_num=%s---" %str(g_num))


if __name__ == "__main__":
    main()