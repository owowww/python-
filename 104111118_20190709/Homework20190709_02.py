# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/09
題目:撰寫一個程式，輸出1到100之間的質數
版本:1.0
說明:
"""
i=2
print("1到100的質數有:",end = "")#end不換行
for i in range(2,101):
   j=2
   for j in range(2,i):
      if i % j == 0 :
         break
   else:
      print(i,end = " ")