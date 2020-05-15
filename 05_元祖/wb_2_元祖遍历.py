#!usr/bin/ python
#-*- coding:utf-8 _*-

info_tuple=("张三", 18, 1.75)

# 使用迭代遍历元组
for my_info in info_tuple:
    # 使用格式字符串%s %s等拼接 my_info 这个变量不方便！
    # 因为元组中通常保存的数据类型是不同的！

    print(my_info)