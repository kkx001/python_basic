#!usr/bin/ python
#-*- coding:utf-8 _*-

def creat_num(all_num):
    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        ret = yield a
        print(">>>> ret >>>>", ret)

        a, b = b, a+b
        current_num += 1

if __name__ == '__main__':
    obj = creat_num(10)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    ret = obj.send("hahaha")
    print(ret)