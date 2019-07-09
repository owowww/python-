# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/08
題目:撰寫一個程式，由使用者輸入基數(b)及指數(n)，輸出b**0到b**n
版本:1.0
說明:
"""
b = eval(input("輸入基數:"))
n = eval(input("輸入指數:"))

for i in range(n+1):#建一個整數列表
  print(b,"的",i,"次方=",pow(b,i),end="\n")
#print(b,"的",n,"次方=",pow(b,n))