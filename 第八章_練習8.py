# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:39:03 2022

@author: 榮 鼎
"""

list1 =[]

s = 0
while True:
    w = int(input("請輸入數字:"))
    list1.append(w)
    if len(list1) == 4:
        for i in range(len(list1)):
            s =s + list1[i]
        break
print(list1)
print("總共:",s)
print("平均:",s/len(list1))

#p8-34 習題8