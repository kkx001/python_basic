#!usr/bin/ python
#-*- coding:utf-8 _*-

class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self,name):
        self.name = name
        # 让类属性的值+1
        Tool.count += 1

# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")

# 2. 输出工具对象的总数
#这里相当于赋值语句，将99赋值给了tool3
tool3.count = 99
print("工具对象总数 %d" % tool3.count)

#这里还是总数为3
print("===> %d" % Tool.count)
