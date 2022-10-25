# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:41:30 2022

@author: 榮 鼎
"""
list1=[]
for i in range(1,7):
    number = int(input("輸入第"+ str(i) +"個數字:"))
    if 1 <= number <= 500:
        list1.append(number)
        if len(list1) == 6:
            find = max(list1)
            print("最大數:",find)
    else:
        print("\n請輸入正確範圍!!")
        number = int(input("輸入第"+ str(i) +"個數字:"))
        list1.append(number)
print(list1)

#p8-34 習題9