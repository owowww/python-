# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。
提示：總和與平均數皆輸出到小數點後第1位
版本:1.0
說明:
"""
a = eval(input("輸入1:"))
b = eval(input("輸入2:"))
c = eval(input("輸入3:"))
d = eval(input("輸入4:"))
e = eval(input("輸入5:"))
total = a+b+c+d+e
print('{} {} {} {} {}'.format(a,b,c,d,e))
print('總和 = {:.1f}'.format(total))
print('平均數 = {:.1f}'.format(total/5))