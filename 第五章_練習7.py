# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 09:49:38 2022

@author: 榮 鼎
"""

kg = float(input("請輸入公斤數: "))
if  1<= kg <= 5:
    print("運費: " + str( kg * 50)  )
    print("物流處理費: 199 "   )
    print("總共: " + str( kg * 50 + 199 ))
if kg > 5:
    print("運費: " + str( kg * 30  ))
    print("物流處理費: 199 "   )
    print("總共: " + str(kg * 30 + 199 ))
    
#P5-28.習題7