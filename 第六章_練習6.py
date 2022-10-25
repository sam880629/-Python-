# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 10:30:13 2022

@author: 榮 鼎
"""

i = int(input("請輸入繩索長度:"))
c = 0
while i >20:
    i=i/2
    c = c + 1 
    if i<=20:
        print("需對折:",c,"次，才會小於20公分")
        break
    
#P6-28.習題6