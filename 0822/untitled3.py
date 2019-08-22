# -*- coding: utf-8 -*-
"""
建立一個資料夾 “abc”，並在裡面產生100個檔案(1.txt to 100.txt)，
每個檔案裡面寫入數值，其數值加上檔名的數值，總和為100
"""
import os
os.mkdir("abc")
for i in range(1,101):
    f = open("abc"+"/"+str(i)+".txt","a")
    j=100-i
    f.write(str(j))
    f.close

