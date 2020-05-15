#!usr/bin/ python
#-*- coding:utf-8 _*-
"""
@author:
@file: wb_continue.py
@time: 2018/10/{DAY}
"""

i=0
while i<10:
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1
