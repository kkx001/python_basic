#!usr/bin/ python
#-*- coding:utf-8 _*-

import multiprocessing
import os
import time

def test():
    while True:
        print("---子进程pid = %d-----父进程pid = %d" %(os.getpid(),os.getppid()))
        time.sleep(1)


def main():
    print("----主进程pid = %d----父进程 pid = %d" %(os.getpid(),os.getppid()))
    p = multiprocessing.Process(target=test)
    p.start()


if __name__ == "__main__":
    main()
