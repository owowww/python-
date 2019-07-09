# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，
最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。
提示1：需import math模組，並使用math.pi。
提示2：輸出浮點數到小數點後第二位。
版本:1.0
說明:
"""
import math
r = eval(input("輸入一圓的半徑:"))    
print('半徑 = {:.2f}\n周長 = {:.2f}\n面積 = {:.2f}'.format(r,2*r*math.pi,r*r*math.pi))
#.2f 輸出浮點數到小數點後第二位。 \n 換行