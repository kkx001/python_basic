#!usr/bin/ python
#-*- coding:utf-8 _*-


class Cat:

    def __init__(self,name):
        self.name = name
        print("%s 我来了!"%self.name)



    def __del__(self):
        print("%s 我去了"%self.name)

    def __str__(self):
        #必须要返回一个字符串
        return "我是小猫[%s]"%self.name


#tom 是一个全局变量
tom = Cat("TOM")

#负责打印__str__返回的字符串
print(tom)


