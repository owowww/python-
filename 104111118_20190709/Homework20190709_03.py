# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/09
題目:請使用while迴圈敍述撰寫一個程式，讓使用者輸入一個正整數num，
計算從1到num之間，所有5的倍數數字的總和
版本:1.0
說明:使用while
"""
num = int(input("輸入一個數字:"))
total=0
i=0
while i<=num:
    total += i
    i += 5
print(total)
    