# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/4
題目:
"""
a = int(input('請輸入a：'))
b = int(input('請輸入b：'))
c = input('請輸入算術運算子：')
total = a+b
total1 = a-b
total2 = a*b
total3 = a/b#浮點除法
total4 = a//b#整數除法(去除小數點)
total5 = a%b#相除後求餘數
if c=="+":#if 必須縮排
    print (total)
elif c=="-":#if 必須縮排
    print (total1)
elif c=="*":#if 必須縮排
    print (total2)
elif c=="/":#if 必須縮排
    print (total3)
elif c=="//":#if 必須縮排
    print (total4)
elif c=="%":#if 必須縮排
    print (total5)
else:
    print ("錯誤")