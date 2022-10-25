# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 14:52:30 2022

@author: 榮 鼎
"""

def fib(n):
    if n >= 2:
       return fib(n-1)+fib(n-2)
    return n
for i in range(8):
    print(fib(i),end=" ")    
    
#p7.35 習題9