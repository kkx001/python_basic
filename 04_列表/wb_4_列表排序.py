#!usr/bin/ python
#-*- coding:utf-8 _*-

name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer"]
num_list = [6, 8, 4, 1, 10]
print("原始数据: ")
print(name_list)
print(num_list)

# #升序 没有参数默认升序
# print("升序数据: ")
# name_list.sort()
# num_list.sort()
#
# print(name_list)
# print(num_list)
#
#
# #降序
# print("降序数据: ")
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)
#
# print(name_list)
# print(num_list)
#

#逆序（反转）
print("逆序数据: ")
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)