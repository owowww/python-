# -*- coding: utf-8 -*-
"""
請輸入一個數字 1~6，如果數字介於 1~3，則顯示小，數字介於
4~6，則顯示大，超出範圍顯示不要亂
"""
a=int(input("請輸入一個數字 1~6:"))
if a>=1 and a<=6:
    if a>=1 and a<=3:
        print("小")
    elif a>=4 or a<=6:
        print("大")
else:
        print("不要亂")