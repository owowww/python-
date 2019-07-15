# -*- coding: utf-8 -*-
"""
定義函數:
    有傳入參數(有預設值)，有回傳值
""" 
"函數定義"
def greeting(name="預設值"):
    print("Hello {}!".format(name))
    return ("回傳值")

"呼叫函數" 
print(greeting("kevin"))
result=greeting()
print(result)