#!usr/bin/ python
#-*- coding:utf-8 _*-
# 假设：以下内容是从网络上抓取的
# 要求：顺序并且居中对齐输出以下内容
poem = ["\t \n登鹳雀楼",
         "王之涣",
         "白日依山尽\t\n",
         "黄河入海流",
         "欲穷千里目",
         "更上一层楼"]

for poems in poem:

    # 先使用strip方法去除字符串中的空白字符
    # 再使用center方法居中显示文本

    #中间对齐
    print("|%s|"%poems.strip().center(10,"　"))
    #左对齐
    #print("|%s|" % poems.ljust(10, "　"))
    #右对齐
    #print("|%s|" % poems.rjust(10, "　"))

