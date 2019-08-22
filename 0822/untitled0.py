# -*- coding: utf-8 -*-
"""
印出1~100的質數，並顯示總共有幾個
"""
s=[2]
for i in range(1,101):
    if i%2 !=0:
        s.append(i)
print(s) 
print(len(s))        
