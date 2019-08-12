# -*- coding: utf-8 -*-
"""
請設計一個 function TRI(a,b,c)，輸入三個邊長，此 function 可以判斷，
此三邊長能否組成三角形。三角形必要條件，最小兩邊加總大於第三邊。 
"""

def TRI(a,b,c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        print("可以")
    else:
        print("不可以")
    return
a=int(input("輸入a:"))
b=int(input("輸入b:"))
c=int(input("輸入c:"))
TRI(a,b,c)