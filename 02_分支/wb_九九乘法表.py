#!usr/bin/ python
#-*- coding:utf-8 _*-
"""
@author:
@file: wb_九九乘法表.py
@time: 2018/10/{DAY}
"""

row = 1

while row <= 9:
    col = 1
    while col <= row:
        #\t:制表符，在文本输出时，使得垂直方向对齐
        print("%d * %d = %d\t" % (row, col, row * col), end=" ")

        #\n换行
        #print("%d * %d = %d\n" % (row, col, row * col), end=" ")

        col += 1
    print(" ")
    row += 1
