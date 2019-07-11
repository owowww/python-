# -*- coding: utf-8 -*-
"""
"""
import random
list=[]

color=["♠️","♥️","♦️","♣️"]#花色
royal=["J","Q","K","A"]#三騎士牌跟A

for j in color:
    for i in range(1,14):
        if i<10:
            list.append([j+str(i+1)])#加入1到10
        elif 13>i>9:
            list.append([j+"".join(royal[i-10:i-9])]) #i>10後是JQK
            #join() 用來轉換royal為字符
        elif i==13:
            list.append([j+"".join(royal[3:4])])            
#print(list)   #測試是否有52張

player=random.sample(list,k=5)#隨機抽5張
player.sort(reverse=True)
print("玩家的牌:",player)

list2 = [i for i in list if i not in player]#移除玩家的牌

computer=random.sample(list2,k=5)#隨機抽5張
print("電腦的牌:",computer)

if player>computer:
    print("win")
elif player==computer: 
    print("draw")
else:
    print("lose")

