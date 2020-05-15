#!usr/bin/ python
#-*- coding:utf-8 _*-
import time
from collections import Iterable
from collections import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个可以迭代的对象，
        即可以使用for，那么必须实现__iter__方法"""
        return ClassIterator()

class ClassIterator(object):
    def __iter__(self):
        pass
    def __next__(self):
        return 11


if __name__ == '__main__':
    classmate = Classmate()
    classmate.add("老王")
    classmate.add("张三")
    classmate.add("王五")


    for name in classmate:
        print(name)
        time.sleep(1)