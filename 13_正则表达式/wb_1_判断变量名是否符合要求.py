#!usr/bin/ python
#-*- coding:utf-8 _*-

import re

def main():
    names = ["ages", "_ages", "1_ages", "lage", "age1", "a_age", "age_1_", "age!", "a#123", "____"]

    for name in names:
    # ^表示规定开头， $规定结尾
    #python中的match默认是从开头判断的，所以，在match中可以不写^
    #但是match不会判断结尾，所以当需要以xxx结尾的时候，要写上$

        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$",name)
        if ret:
            print("变量名: %s 符合要求...通过正则表达式匹配出来的数据是:%s" %(name,ret.group()))

        else:
            print("变量名: %s 不符合要求...." %name)


if __name__ == '__main__':
    main()