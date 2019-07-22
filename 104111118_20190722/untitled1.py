# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:22:06 2019

@author: MIS801
"""

with open("student.txt","r",encoding="UTF-8-SIG") as f:
    student = f.readlines()
    #print (student)

t = list()#命名空清單t
for k in range(len(student)):
    a = student[k]
    b = a.split()#分割每一行第k位
    print(b)
    for i in range(0,len(b),3):
        c = b[i:i+3]#每三字串為一次進行迴圈
        t.append(c)#加入清單t
        
        
        
        
#for g in range(10):
#    print("第" + str(g+1) + "組:" + str(t[g]))