# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""開啟檔案"""  
#f=open("student.txt","r",encoding="utf-8")
#for student in f:
#    print(student,end="")
#f.close()  
"""開啟檔案 簡易"""  
#with open("student.txt","r",encoding="utf-8") as f:
#    for student in f:
#        print(student,end="")
"""開啟檔案 簡易"""  
#with open("student.txt","r",encoding="UTF-8-SIG") as f:
#    student=[]
#    for line in f:
#        student.append(line.strip('\t\n'))        
#    print(student)  
"""開啟檔案 readlines()"""  
with open("student.txt","r",encoding="UTF-8-SIG") as f:
    student=f.readlines()
    print(student)  