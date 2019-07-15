# -*- coding: utf-8 -*-
"""
請定義一個函數 ’my_max(*args)‘，接收不定個數的參數，回傳這些參數的最大值。

"""
def my_max(*args):
    number=0
    for i in args:
        if i > number:
            number = i
    return number

print("數字的最大值是:{}".format(my_max(10,20,30,40,500,55)))
