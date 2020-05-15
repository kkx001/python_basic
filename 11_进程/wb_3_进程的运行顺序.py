#!usr/bin/ python
#-*- coding:utf-8 _*-
import multiprocessing
import os
import time

def test1():
    while True:
        print("----test1---子进程pid = %d----父进程pid = %d" %(os.getpid(),os.getppid()))
        time.sleep(1)

def test2():
    while True:
        print("----test2---子进程pid = %d----父进程pid = %d" %(os.getpid(),os.getppid()))
        time.sleep(1)

def main():
    print("-------主进程---pid = %d-----父进程pid = %d" %(os.getpid(),os.getppid()))

    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()