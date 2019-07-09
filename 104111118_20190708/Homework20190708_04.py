# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:39:10 2019

@author: MIS801
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