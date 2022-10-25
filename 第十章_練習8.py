# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:27:38 2022

@author: 榮 鼎
"""

class Bicycle :
    def __init__(self ,color,weight,wheelbase,model,money):
        self.__weight= weight
        self.__color = color
        self.__wheelbase = wheelbase
        self.__model = model
        self.__money = money
        
    def getcolor(self):
        return self.__color 
    
    def getweight(self):
        return self.__weight
    def getwheelbase(self):
        return self.__wheelbase
    def getmodel(self):
        return self.__model
    def getmoney(self):
        return self.__money
    def displayVehicle(self):
       
        print("色彩 = " + self.__color)
        print("車重 = " + self.__weight)
        print("輪距 = " + self.__wheelbase)  
        print("車型 = " + self.__model)
        print("車價 = " + self.__money)
        
class RacingBike(Bicycle):
    def __init__(self, color,weight,wheelbase,model,money,speed,date):
        
        super().__init__(color,weight,wheelbase,model,money)
        
        self.__speed = speed
        self.__date = date
        
    def displayVehicle(self):
        print("變速 = " + self.__speed)
        print("資訊 = " + self.__date)
        
        
        
c1 = RacingBike("red", "2.5", "3", "登山", "25000","8","2022")
c1.displayVehicle()
print("\n")
c2 = Bicycle("red", "2.5", "3", "登山", "25000")
c2.displayVehicle()

#p10-31 習題8