#!usr/bin/ python
#-*- coding:utf-8 _*-

def creat_num(all_num):
    print("----1----")

    a, b = 0, 1

    current_num = 0
    while current_num < all_num:
        print("----2----")

        # 如果一个函数中有yield语句，那么这个就不在是函数，而是一个生成器的模板
        yield a
        print("----3----")

        a, b = b, a+b
        current_num += 1
        print("----4----")


if __name__ == '__main__':

    # 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
    obj = creat_num(10)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)

    ret = next(obj)
    print(ret)


    obj2 = creat_num(4)
    ret = next(obj2)
    print(ret)

    ret = next(obj2)
    print(ret)

    ret = next(obj2)
    print(ret)
