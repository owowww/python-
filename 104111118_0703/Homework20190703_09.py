# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，讓使用者輸入一個正數s，代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。
提示1：建議使用import math模組的math.pow及math.tan
提示2：正五邊形面積的公式： Area=(5∗s2)/(4∗tan(pi/5))Area=(5∗s2)/(4∗tan(pi/5))
提示3：輸出浮點數到小數點後第四位。

版本:1.0
說明:
"""
import math
s = eval(input("輸入正五邊形之邊長:"))
area = (5*math.pow(s,2))/(4*math.tan(math.pi/5))
print("正五邊形之面積 = {:.4f}".format(area))