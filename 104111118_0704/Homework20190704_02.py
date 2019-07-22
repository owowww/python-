# -*- coding: utf-8 -*-
"""

班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/4
題目:
"""
money = eval(input("輸入:"))
vip=input("是否有貴賓卡?(y/Y):")
total = round(money *1.1)#四捨五入
viptotal = round((money *1.1)*0.9)#四捨五入
if vip=="y" or vip=="Y":#if 必須縮排
    print ("總金額 = {:.0f}".format(viptotal))
else:
    print ("總金額 = {:.0f}".format(total))