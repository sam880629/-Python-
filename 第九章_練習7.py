# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:55:02 2022

@author: 榮 鼎
"""

name=("tom","mary","joe")
score=(85,76,58)
s = 0
for a in range(len(score)):
    s=s+score[a]
print("學生數:",len(name))
print("成績總分:",s)
print("成績平均:",s/(len(score)))
i = int(input("輸入學號:"))-1
t = zip(name,score)
print(tuple(t)[i])

#p9-33 習題7
