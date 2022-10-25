# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:19:00 2022

@author: 榮 鼎
"""

cm = int(input("請輸入身高: "))
if cm < 120:
    print("免費")
if 120 <= cm <= 150:
    print("半價")
if cm >150:
    print("全票")
    
#P5-28.習題9