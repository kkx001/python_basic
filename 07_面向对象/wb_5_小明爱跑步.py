#!usr/bin/ python
#-*- coding:utf-8 _*-

class Person:
    def __init__(self,name,weight):
        #self.属性 = 形参

        self.name = name
        self.weight = weight

    def __str__(self):
        return  "我的名字叫%s, 体重%.2f千克"%(self.name,self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)
        self.weight += 1

xm = Person("小明",75.5)

xm.run()
xm.eat()
print(xm)

xiaomei = Person("小美",46)
xiaomei.run()
print(xiaomei)
