# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/09
題目:請撰寫一個程式，在螢幕上列印如下的圖形。
版本:1.0
說明:
"""
for i in range(7):
    print((' ' * 8) + '***')
for i in range(10):
    for j in range(0,i):
        print(end=" ")
    for j in range(i,10):
        print("$",end=" ")
    print("")