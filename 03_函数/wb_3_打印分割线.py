#!usr/bin/ python
# -*- coding:utf-8 _*-


def print_line(char, time):
    print(char * time)


# print_line('-',20)

def print_lines(char, time):
    """打印文档分隔线
    :param char: 使用的分隔符
    :param time: 分隔符重复的次数
    """
    row = 0
    while row < 5:
        print_line(char, time)
        row += 1


print_lines("+", 30)
