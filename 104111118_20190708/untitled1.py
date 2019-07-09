# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/08
題目:撰寫一個程式，1-10之間產生一個亂數，使用者輸入數字，猜對顯示猜的次數並結束，
否則提示大小，最多猜5次。
版本:1.1
說明:使用for
"""
import random
ans =  random.randint(1,10) #取從1到10的亂數
times = 0
print('請猜一個1~10的數字，最多猜5次')
for i in range(5):#建一個整數列表
    guess = int(input('猜一個數字:')) #input出來預設為str，轉型為int
    times = times+1 #每猜一次就要+1 
    if (guess > ans):
        print('太大')
    elif (guess < ans):
        print('太小')
    else:
        print('恭喜你猜對了！')
        break
print("答案是"+str(ans)+'，你猜了'+str(times)+'次') 