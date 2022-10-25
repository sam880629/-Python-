# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 10:59:25 2022

@author: 榮 鼎
"""

money = int(input("請輸入金額:"))
yearsp =int(input("請輸入多少年:"))
year = 0
s = 0

while year < yearsp:
    s = (money  * 0.12 ) + money
    money = money + s
    year = year+1
    if year == yearsp:
        break
print( "本利和:", int(s) )

#P6-28.習題8
