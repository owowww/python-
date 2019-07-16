# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/16
題目:請撰寫一個程式，由使用者輸入數個數字，排序後輸出。
版本:1.0
說明:
"""
number_list=[]
number = input("輸入數個數字:").split(",")
number_list = list(number)
print("數字：",number_list)
number_list.sort()
print("排序後的數字：",number_list)