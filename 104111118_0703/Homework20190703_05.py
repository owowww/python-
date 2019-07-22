# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、
寬（Width）、周長（Perimeter）及面積（Area）。
提示：輸出浮點數到小數點後第二位。
版本:1.0
說明:
"""
height = eval(input("輸入高:"))
width = eval(input("輸入寬:"))
perimeter = (height + width) * 2
area = height * width
print('高 = {:.2f}\n寬 = {:.2f}\n周長 = {:.2f}\n面積 = {:.2f}'.format(height,width,perimeter,area))