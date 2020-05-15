#!usr/bin/ python
#-*- coding:utf-8 _*-

# 使用 多个键值对，存储 描述一个 物体 的相关信息 —— 描述更复杂的数据信息
# 将 多个字典 放在 一个列表 中，再进行遍历

name_list = [
    {"name": "王兵",
      "age": 24,
      "gander": True,
      "height": 168,
      "weight": 75.5},
    {"name": "袁胜超",
      "age": 25,
      "gander": True,
      "height": 168,
      "weight": 65}
]
print(name_list)

for names in name_list:
    print(names)