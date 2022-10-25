# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:23:23 2022

@author: 榮 鼎
"""

try:
        month = int(input("請輸入月份:" ))
        if month == 3 or month ==4 or month ==5:
            print("春季")
        if month == 6 or month ==7 or month ==8:
            print("夏季")
        if month == 9 or  month ==10 or month ==11:
            print("秋季")
        if month == 12 or month == 1 or month == 2:
            print("冬季")
except:
        print("請輸入正確數字")
    
#P5-28.習題10