#!usr/bin/ python
#-*- coding:utf-8 _*-
import os
import multiprocessing
import time


def test(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


def main():
    print("----主进程pid = %d----父进程pid = %d" %(os.getpid(),os.getppid()))

    p = multiprocessing.Process(target=test,args=(11,22,33,44,55),kwargs={"name":"wb"})

    p.start()

if __name__ == '__main__':
    main()