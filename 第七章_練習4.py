# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 13:24:17 2022

@author: 榮 鼎
"""
x = int(input("輸入參數1:"))
y=  int(input("輸入參數2:"))
z=0
def one():
    
    if x > y:
        z = x * y
    else:
        z = x + y
    return z 

def two():
    if  y == 0:
        z = -1
        
    else:
        z= x/y
    return z    
        
print("第一函數:",one())
print("第二函數:",two())
#p7.35 習題4