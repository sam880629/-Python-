# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:04:54 2022

@author: 榮 鼎
"""

m = int(input("請輸入里程數: "))
if m <= 1500:
    print("80元")
else:
    c = int((((m-1500)/500)+1))
    print( str(c*5+80) + "元")

#P5-28.習題8