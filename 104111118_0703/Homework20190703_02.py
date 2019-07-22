# -*- coding: utf-8 -*-
"""
Spyder Editor
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/7/3
題目:請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，然後將這四個浮點數以欄寬為7、
欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，
左右皆以直線 |（Vertical bar）作為邊界。
提示：輸出浮點數到小數點後第二位。
版本:1.0
說明:
"""
score=eval(input("輸入:"))
score2=eval(input("輸入2:"))
score3=eval(input("輸入3:"))
score4=eval(input("輸入4:"))
msg ="|"+ '%7.2f' % score + ' %7.2f' % score2+"|"
msg2 ="|"+ '%7.2f' % score3 + ' %7.2f' % score4+"|"
print(msg)
print(msg2)
msg3 = "|"+ '%-7.2f' % score + ' %-7.2f' % score2+"|"
msg4 = "|"+ '%-7.2f' % score3 + ' %-7.2f' % score4+"|"
print(msg3)
print(msg4)