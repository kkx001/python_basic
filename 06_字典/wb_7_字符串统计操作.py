#!usr/bin/ python
#-*- coding:utf-8 _*-

str1 = "hello python"

# 1. 统计字符串长度
print(len(str1))

# 2. 统计某一个小（子）字符串出现的次数
print(str1.count("h"))
print(str1.count("asd"))

# 3. 某一个子字符串出现的位置
# 注意：如果使用index方法传递的子字符串不存在，程序会报错！

print(str1.index('py'))