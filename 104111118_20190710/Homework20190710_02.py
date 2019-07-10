# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/10
題目:撰寫一個程式，班級隨機抽5位
版本:1.0
說明:
"""
import random
student = ["李柏叡", "張家豪", "黃庭孜", "闕伯翰", "呂湧儒", "黃凱裕", "王宏宇", "連于瑄", "黃彥霖", "田立廣"]
#print(random.sample(student,k=5))#直接印出
a=random.sample(student,k=5)
for i in range(0,5):
    print(a[i])#逐一列印 左至右