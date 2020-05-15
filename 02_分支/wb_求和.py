#!usr/bin/ python
#-*- coding:utf-8 _*-
"""
@author:
@file: wb_求和.py
@time: 2018/10/{DAY}
"""

"""
#0到100求和
result=0
i=0
while i<=100:
    print(i)
    result+=i
    print("sum=%d " % result)
    i+=1
"""

#0到100偶数求和

result=0
i=0

while i<=100:
    if i % 2 == 0:
        print("i= %d"%i)
        result += i
        print("result= %d"%result)

    i+=1
