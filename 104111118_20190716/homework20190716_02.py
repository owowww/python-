# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/16
題目:請撰寫一個程式，將數組資料中的”Amy”改成“Mary”。
版本:1.0
說明:
"""
multi=("Amy",1,1.0,"Amy",True,"Amy")
print(multi)

multi_list=list(multi)
multi_list[0] = "Mary"
multi_list[3] = "Mary"
multi_list[5] = "Mary"        
       

multi=tuple(multi_list)
print(multi)