# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/10
題目:請撰寫一個程式，利用亂數產生10個不重覆的亂數，存放於串列中。
版本:1.0
說明:
"""
import random
all_num = int(input("輸入一個數字:"))
num = 10
result=random.sample(range(1,all_num),num)
print("產生的亂數:",result)
print("總共有",len(result),"個亂數")