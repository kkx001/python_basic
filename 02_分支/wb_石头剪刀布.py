#!usr/bin/ python
#-*- coding:utf-8 _*-
"""
@author:
@file: wb_石头剪刀布.py
@time: 2018/10/{DAY}
"""
import random
#从控制台输入要出的拳
player=int(input("请输入要输入的拳 (1)石头 ,(2)剪刀 , (3)布: "))

computer=random.randint(1,3)
print("玩家输入的是: %d -- 电脑输入的拳是: %d"%(player,computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("玩家胜利!")
elif player == computer:
    print("平手！！")


else:
    print("电脑胜利!")


