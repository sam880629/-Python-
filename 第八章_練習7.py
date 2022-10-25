# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:23:46 2022

@author: 榮 鼎
"""

list1 = [1,2,3,4,5,6,7,8,9,10]


def list1_s(x):
    s=0
    for i in range(1,len(x)+1):
        s = s + i
    
    return s 
    
def list1_avg(x):
    s=0
    for i in range(1,len(x)+1):
        s = s + i
    
    return (s/len(x)) 


print("項目值:",len(list1))    
print("項目值總和:",list1_s(list1)) 
print("項目值平均:",list1_avg(list1))  

#p8-34 習題7