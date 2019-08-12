# -*- coding: utf-8 -*-
"""
請設計一支程式可以計算出 a
3
-3a2b+3ab2
-b
3
"""
a=int(input("輸入a:"))
b=int(input("輸入b:"))
c=a**3-3*a*a*b+3*a*b*b-b**3
print(c)
