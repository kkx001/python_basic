#!usr/bin/ python
#-*- coding:utf-8 _*-

def craet_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a

        a, b = b, a+b
        current_num += 1

    return "ok---"


if __name__ == '__main__':

    obj = craet_num(10)
    while True:
        try:
            ret = next(obj)
            print(ret)

        except Exception as ret:
            print(ret.value)
            break