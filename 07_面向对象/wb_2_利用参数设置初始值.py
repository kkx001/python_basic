#!usr/bin/ python
#-*- coding:utf-8 _*-

class Cat:

    def __init__(self,name):
        print("这是一个初始化方法!")

        self.name = name

    def eat(self):
        print("%s在吃东西"%self.name)

#使用类名()创建对象的时候，会自动调用初始化方法__init__()
tom = Cat("TOM")
tom.eat()

lazy_cat = Cat("蓝猫")
lazy_cat.eat()
