#!usr/bin/ python
#-*- coding:utf-8 _*-
import multiprocessing
import os
import time

nums = [11,22,33]

def test1():
    nums.append(44)
    print("----test1----nums = %s" %str(nums))
    time.sleep(1)


def test2():
    print("----test2---nums = %s" %str(nums))


def main():
    print("---主进程pid = %d----父进程pid= %d---" %(os.getpid(),os.getppid()))

    p1 = multiprocessing.Process(target=test1)
    p1.start()

    p1.join()

    p2 = multiprocessing.Process(target=test2)
    p2.start()


if __name__ == '__main__':
    main()