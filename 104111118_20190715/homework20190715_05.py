# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/10
題目:
請撰寫一個程式，定義一個函數，接收一個參數，
判斷該參數是否為數字，若是則回傳該數的絕對值，若不是數字則回傳錯誤訊息。
版本:1.0
說明:Hint: isinstance(object, classinfo) 
          不可以用abs()
"""
def number(num=1):
    if isinstance(num,(int,float)):
        if num<0:
            return (num*-1)
        else:
            return (num)
    else:
        print("不是數字。")
        return ("")


user=eval(input("輸入數字:"))

print(number(user))
