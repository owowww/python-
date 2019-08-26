# -*- coding: utf-8 -*-
"""
一、新北市垃圾清運車輛所在位址。 
二、資料僅顯示目前出勤中之垃圾車所在位址，故不同時段，資料數會有明顯不同（每2分鐘更新1次），
甚至少數時段可能為零。 
三、垃圾車車機採4G訊號傳輸，倘有訊號不良情形，可能導致資料延遲。
lineid(清運路線編號)、car(車牌號碼)、time(回報時間)、location(所在位址)、
longitude(經度)、latitude(緯度)、cityid(行政區代號)、cityname(行政區名稱)
"""
#RealtimeWaterLevel_OPENDATA
import json

from urllib.request import urlopen
u = urlopen("http://data.ntpc.gov.tw/od/data/api/28AB4122-60E1-4065-98E5-ABCCB69AACA6?$format=json")


resp = json.load(u)
#print(resp)
keyword = input("請輸入要查詢的區域:")
for i in range(len(resp)):
    #print([i]["cityname"])
    if(keyword in resp[i]["location"]): # in
        print("時間:",resp[i]["time"])
        print("所在位置:",resp[i]["location"])
        
    
        
        