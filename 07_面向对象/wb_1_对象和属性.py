#!usr/bin/ python
#-*- coding:utf-8 _*-


class Cat:
    #哪一个对象调用的方法，self就是哪一个对象的引用
    def eat(self):

        print("%s 在吃东西"%self.name)

    def drink(self):
        print("%s在喝水"%self.name)

#创建描述对象
tom = Cat()


#可以使用.属性名 利用赋值语句就可以
tom.name = "TOM"


tom.eat()
tom.drink()
