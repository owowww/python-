# -*- coding: utf-8 -*-
"""
班級:資管4A
學號:104111118
姓名:黃凱裕
日期:2019/07/08
題目:撰寫一個程式，1-100之間產生一個亂數，使用者輸入數字，猜對顯示猜的次數並結束，
否則提示大小。
版本:1.0
說明:使用while
"""
import random
ans =  random.randint(1,100) #取從1到10的亂數
times = 0
print('請猜一個1~100的數字，輸入超過100結束遊戲')
play = True
while(play):
    guess = int(input('猜一個數字:')) #input出來預設為str，轉型為int
    times = times+1 #每猜一次就要+1
    if (guess > 100):
        print('遊戲結束！')
        break
    elif (guess < ans):
        print('太小')
    elif (guess > ans):
        print('太大')       
    else:
        print('恭喜你猜對了！')
        play = False        
print("答案是"+str(ans)+'，你猜了'+str(times)+'次') 