#!usr/bin/ python
#-*- coding:utf-8 _*-
"""
@author:
@file: ex.py.py
@time: 2018/10/{DAY}
"""


#将九九乘法表用函数写出来

def math_result(i):
    """九九乘法表"""
    row = 1
    while row <= i:
        col = 1
        while col <= row:
            """行列"""
            #\t:制表符，在文本输出时，使得垂直方向对齐
            print("%d * %d = %d\t"%(row,col,row*col),end=" ")

            #\n换行
            #print("%d * %d = %d\n" % (row, col, row * col), end=" ")

            col +=1
        print(" ")
        row += 1


math_result(9)