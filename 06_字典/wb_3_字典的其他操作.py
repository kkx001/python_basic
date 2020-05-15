#!usr/bin/ python
#-*- coding:utf-8 _*-

wb = {"name": "王兵",
      "age": 18,
      "gander": True,
      }
# 1. 统计键值对数量len()
print(len(wb))

# 2. 合并字典update()
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
temp={"height": 168,
      "weight": 75.5,
      "age": 24}
wb.update(temp)
print(wb)

# 3. 清空字典clear()
wb.clear()
print(wb)
