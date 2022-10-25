# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 12:58:01 2022

@author: 榮 鼎
"""
n = 0
s = 1 
while n<5:
    i = int(input("輸入一個數:"))
    if n < 5 and i > 0 :
        s = s * i
        n+=1
    if n < 5 and i ==0 :
        print("跳過此數字")
        n+=1
    if n >=4:
        print("和:" , s)
        break
    
#P6-28.習題10