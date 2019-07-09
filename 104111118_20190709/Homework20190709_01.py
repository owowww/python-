# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/09
題目:撰寫一個程式，輸出因數
版本:1.0
說明:利用for跟contiune
"""
num = int(input("輸入一個數字:"))
for i in range(1,num+1):
        if num % i != 0 : 
            continue
        else:
            print(i)
            
