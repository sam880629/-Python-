# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:21:20 2022

@author: 榮 鼎
"""

def volume():
    v = w * h * l 
    return v

def area():
    a  = l * w
    return a

w = int(input("寬度:"))
h = int(input("高度:"))
l = int(input("長度:"))

print("\n體積:%s" % volume())
print("\n面積:%s" % area())

#p10-31 習題7