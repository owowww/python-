# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/10
題目:撰寫一個程式，班級學生串列
版本:1.0
說明:
"""
student = ["李柏叡", "張家豪", "黃庭孜", "闕伯翰", "呂湧儒", "黃凱裕", "王宏宇", "連于瑄", "黃彥霖", "田立廣"]
print(student)#直接印出
#print(student[::-1])#反轉[::-1]

"--------逐一列印 左至右---------"
for i in range(len(student)):
    print(student[i])#逐一列印 左至右
    
"--------逐一列印 右至左---------"
for i in range(-1,-(len(student)+1),-1):
    print(student[i])#逐一列印 右至左  
    
"----------1到-10，間隔-1-------"  
print(student[-1:-11:-1])#-1到-10，間隔-1

"-----------刪除陣列元素---------"
del student[3]#刪除陣列元素
for i in range(len(student)):    
    print(student[i])#逐一列印 左至右
    
print("---------重複n次-----------")
student*=2#重複n次
for i in range(len(student)):
    print(student[i])
    
print("-----------刪除串列元素(remove)-------------")  
n=student.count("闕伯翰")
if n!=0:
    for i in range(n):
        student.remove("闕伯翰")
for i in range(len(student)):
    print(student[i])        