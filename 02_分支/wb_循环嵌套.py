#!usr/bin/ python
#-*- coding:utf-8 _*-
"""
@author:
@file: wb_循环嵌套.py
@time: 2018/10/{DAY}
"""
"""
#输入三角形
row = 1
while row <= 5:
    print("*" *row)

    row += 1 
"""
#输出三角形
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*",end="")

        col += 1
    print("")
    row += 1

"""
#输入正方形
row=1
while row <=5:
    #low负责列的星星显示
    low = 1
    while low <=5:
        print("*",end=' ')
        low += 1
    print("")
    row += 1

print("over")

"""

