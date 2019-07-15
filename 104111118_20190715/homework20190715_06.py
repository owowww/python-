# -*- coding: utf-8 -*-
"""
請定義一個函數 ’my_sort(*args)‘，接收數個參數，回傳這些參數的排序結果。
提示：
1、請利用list()函數將數組轉成串列
2、可利用串列的sort()函數進行排序
3、利用迴圈將排序結果串列印出來 

"""
def max(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print("數字的總和是:{}".format(max(10,20,30,40,50)))