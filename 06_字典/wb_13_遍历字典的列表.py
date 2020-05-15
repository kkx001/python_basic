#!usr/bin/ python
#-*- coding:utf-8 _*-

stu = [
    {"name": "王兵"},
    {"name": "袁胜超"}
]

# 在学员列表中搜索指定的姓名
find_name = "张云志"

for stu_dict in stu:
    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了%s "%find_name)
        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break
# 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
# 还希望得到一个统一的提示！

else:
    print("抱歉，没找到%s"%find_name)

print("循环结束")
