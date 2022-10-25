# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:42:13 2022

@author: 榮 鼎
"""

def bmi():
    bmi = w/(h*h)
    return bmi

w = int(input("體重是:"))
h = int(input("身高是:"))/100
print(bmi())

#p7.35 習題8