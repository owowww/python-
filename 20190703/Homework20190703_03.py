# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、欄與欄間隔一個空白字元、
每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
版本:1.0
說明:
"""
score=input("輸入:")
score2=input("輸入2:")
score3=input("輸入3:")
score4=input("輸入4:")
msg =("|{:>10} {:>10}|".format(score,score2))
msg2 =("|{:>10} {:>10}|".format(score3,score4))
print(msg)
print(msg2)
msg3 =("|{:10} {:10}|".format(score,score2))
msg4 =("|{:10} {:10}|".format(score3,score4))
print(msg3)
print(msg4)