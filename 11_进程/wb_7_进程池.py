#!usr/bin/ python
#-*- coding:utf-8 _*-
from multiprocessing import Pool
import os,time,random


def workder(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d " %(msg,os.getpid()))

    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f" %(t_stop-t_start))


#windows下要用if __name__ == '__main__':包含主函数
if __name__ == '__main__':
    po = Pool(3)

    for i in range(0, 10):
        po.apply_async(workder, (i,))

    print("-----start------")
    po.close()
    po.join()
    print("-----end-----")
