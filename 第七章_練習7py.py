# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:10:58 2022

@author: 榮 鼎
"""

def rate_exchange(TW,rate):
    USD = TW*rate
    return USD
TW = int(input("台幣金額: "))
print("美金金額:",rate_exchange(TW,0.031))
    
#p7.35 習題7