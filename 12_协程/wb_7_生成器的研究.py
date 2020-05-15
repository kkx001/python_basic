#!usr/bin/ python
#-*- coding:utf-8 _*-

def creat_num(all_num):
    print("----1----")

    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        print("----2----")

        yield a
        print("----3----")

        a, b = b, a+b
        current_num += 1
        print("----4----")


if __name__ == '__main__':
    obj1 = creat_num(10)
    obj2 = creat_num(5)

    ret = next(obj1)
    print("obj1: ",ret)

    ret = next(obj1)
    print("obj1: ", ret)

    ret = next(obj2)
    print("obj2: ", ret)

    ret = next(obj1)
    print("obj1: ", ret)

    ret = next(obj2)
    print("obj2: ", ret)

    ret = next(obj1)
    print("obj1: ", ret)

    ret = next(obj1)
    print("obj1: ", ret)

    ret = next(obj1)
    print("obj1: ", ret)

    ret = next(obj2)
    print("obj2: ",ret)