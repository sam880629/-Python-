# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:02:02 2022

@author: 榮 鼎
"""
#計算Internet費用
def bill():
    if h <= 50:
        mon = (h*60)*0.3
    else:
        mon = (h*60)*0.2
    return mon
        
h = int(input("請輸入多少小時:"))
print(bill(),"元")

#p7.35 習題6