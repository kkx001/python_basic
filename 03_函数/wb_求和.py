#!usr/bin/ python
#-*- coding:utf-8 _*-

"""
def sum_2_num():
    #函数求和
    num1 = float(input("输入num1 的值: "))
    num2 = float(input("输入num2 的值: "))

    result = num1 + num2

    print("求和结果为: %f"%result)


sum_2_num()

"""
"""
#第二种方法

def sum_2_num(num1,num2):
    #函数求和

    result = num1 + num2

    print("%d + %d = %f"%(num1,num2,result))


sum_2_num(45,65)
"""

#第三种方法

def sum_2_num(num1,num2):

    result = num1 + num2
    return result #return表示返回，下放代码不会被执行


    print("会被执行吗?")   #这不会被执行

print("求和结果为: %d"%sum_2_num(30,45))
