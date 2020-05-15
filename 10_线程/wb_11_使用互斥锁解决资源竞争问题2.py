#!usr/bin/ python
#-*- coding:utf-8 _*-
import threading
import time

g_num = 0

mutex = threading.Lock()


def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  #上锁
        g_num += 1
        mutex.release()  #解锁

    print("----test1----g_num=%d===" %g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    print("----test2----g_num=%d--" %g_num)


def main():
    t1 = threading.Thread(target=test1,args=(10000000,))
    t2 = threading.Thread(target=test2,args=(10000000,))

    t1.start()
    t2.start()

    time.sleep(1)

    print("----main----g_num=%d---" %g_num)


if __name__ =="__main__":
    main()