#!usr/bin/ python
#-*- coding:utf-8 _*-

wb = {"name": "王兵"}

#1.取值
# 在取值的时候，如果指定的key不存在，程序会报错！
print(wb["name"])

#2.增加/修改
# 如果key不存在，会新增键值对
wb["age"] = 18
print(wb)

# 如果key存在，会修改已经存在的键值对
wb["name"] = "袁胜超"
print(wb)
#3.删除
# 在删除指定键值对的时候，如果指定的key不存在，程序会报错！
wb.pop("age")

print(wb)
