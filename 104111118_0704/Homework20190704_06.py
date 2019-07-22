# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/4
題目:請設計一個餐廳結帳系統，結帳金額計算方式如下：
1、總消費金額再加上10%的營業稅
2、若消費者有金卡 (g/G?)，則結帳金額可再打8折。
3、若消費者有銀卡 (s/S?)，則結帳金額可再打9折。
4、一般消費者打95折。

"""
money = eval(input("輸入:"))
vip=input("是否有金卡?(g/G?)銀卡?(s/S?):")
total = round((money *1.1)*0.95)#四捨五入
viptotal = round((money *1.1)*0.9)#四捨五入
vviptotal = round((money *1.1)*0.8)#四捨五入
if vip=="g" or vip=="G":#if 必須縮排
    print ("總金額 = {:.0f}".format(vviptotal))
elif vip=="s" or vip=="S":#if 必須縮排
    print ("總金額 = {:.0f}".format(viptotal))
else:
    print ("總金額 = {:.0f}".format(total))