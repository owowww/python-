# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/08
題目:撰寫一個程式，判斷是否為質數
版本:1.0
說明:
"""
num = int(input("輸入一個數字:"))
 # 質數大於 1
if num > 1:   # 查看
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"不是質數")
           break
   else:
       print(num,"是質數")# 如果輸入的數字小於或等於1，不是質數
else:
   print(num,"不是質數")