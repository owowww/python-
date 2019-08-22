# -*- coding: utf-8 -*-
"""
輸入5
#最多二個迴圈
1
123
12345
1234567
123456789
"""
n=int(input("輸入:"))
for i in range(1,n*2,2):
    for j in range(1,i+1):
        print(j,end="")
    print("")
    
