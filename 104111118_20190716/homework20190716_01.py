# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/16
題目:
版本:1.0
說明:
"""
"""數組"""
num=(9,20,30)

"""印出整個數組"""
print(num)

"""逐一印出整個數組(1)"""
for i in num:
    print(i)

"""逐一印出整個數組(2)"""    
for i in range(len(num)):
    print(num[i])
    
"""Tuple也允許不同資料型態"""    
multi=("Amy",1,1.0,True,"Amy")
print(multi)

"""Tuple不可改變內容"""
#multi[3]="Mary"

"""數組的方法"""
print(multi.count("Amy"))
print(multi.index("Amy"))
