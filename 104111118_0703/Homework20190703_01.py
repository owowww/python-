# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、
欄與欄間隔一個空白字元，再以每列印兩個的方式，先列印向右靠齊，
再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
版本:1.0
說明:
"""
score=eval(input("輸入:"))
score2=eval(input("輸入2:"))
score3=eval(input("輸入3:"))
score4=eval(input("輸入4:"))
msg ="|"+ '%5s' % score + '%5s' % score2+"|"
msg2 ="|"+ '%5s' % score3 + '%5s' % score4+"|"
print(msg)
print(msg2)
msg3 = "|"+ '%-5s' % score + '%-5s' % score2+"|"
msg4 = "|"+ '%-5s' % score3 + '%-5s' % score4+"|"
print(msg3)
print(msg4)