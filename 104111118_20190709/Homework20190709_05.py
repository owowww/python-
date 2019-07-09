# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/09
題目:請撰寫一個程式，在螢幕上列印如下的圖形。
版本:1.0
說明:
"""
height = 7
stars = 1
for i in range(height):
    print((' ' * (height - i)) + ('*' * stars))
    stars += 2
print((' ' * (height - i)) + ('*' * stars))
