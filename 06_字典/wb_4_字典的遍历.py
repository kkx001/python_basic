#!usr/bin/ python
#-*- coding:utf-8 _*-

wb = {"name": "王兵",
      "age": 24,
      "gander": True,
      "height": 168,
      "weight": 75.5}

# 迭代遍历字典
# 变量k是每一次循环中，获取到的键值对的key
for k in wb:
  print("%s - %s "%(k,wb[k]))


for key,value in wb.items():
    print(key+":",value)