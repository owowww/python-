# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/09
題目:請撰寫一個程式，在螢幕上列印九九乘法表。
請注意列印結果的排版
版本:1.0
說明:
"""
line = 1
while line<10:  # 迴圈取出行數
    lise = 1
    while lise<=line:  # 迴圈取出列數
        print("%d*%d=%2d"%(lise,line,lise*line),end=" ")  
        lise += 1
    print(" ")
    line += 1
