# -*- coding: utf-8 -*-
"""
輸入檔名，並請將 list, tuple, set, dictionary的差別 寫到此檔案中。
"""
k=input()
with open(k+".txt","a") as f:
    f.write("list, tuple, set, dictionary的差別")