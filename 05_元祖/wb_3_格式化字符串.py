#!usr/bin/ python
#-*- coding:utf-8 _*-

info_tuple = ("小明", 21, 1.85)
# 格式化字符串后面的 `()` 本质上就是元组

print("%s的年龄是 %d 身高是 %.2fcm"%("小明",18,175))
print("%s的年龄是 %d 身高是 %.2fm"%info_tuple)

info_str = "%s的年龄是 %d 身高是 %.2fm" %info_tuple
print(info_str)

