# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，計算並輸出此正n邊形之面積（Area）。
提示1：建議使用import math模組的math.pow及math.tan
提示2：正n邊形面積的公式如下：Area=(n∗s2)/(4∗tan(pi/n))Area=(n∗s2)/(4∗tan(pi/n))
提示3：輸出浮點數到小數點後第四位

版本:1.0
說明:
"""
import math
n = eval(input("輸入正n邊形之n:"))
s = eval(input("輸入正n邊形之邊長:"))
area = (n*math.pow(s,2))/(4*math.tan(math.pi/n))
print("正n邊形之面積 = {:.4f}".format(area))