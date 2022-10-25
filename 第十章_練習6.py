# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:17:22 2022

@author: 榮 鼎
"""
param = int (input("請輸入攝氏溫度:"))
def temp_change():
    f = (9.0*param)/5+32
    return f

print("華氏溫度:%s" % temp_change())

#p10-31 習題6