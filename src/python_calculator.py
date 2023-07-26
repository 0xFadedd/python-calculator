#!/usr/bin/env python

class PythonCalculator:
    def __init__(self):
        self.calculation = ''
        self.memory = 0

    def clear(self):
        self.memory = 0
        self.calculation = ''
        
    def add(self, value):
        self.memory = self.memory + value 
                
    def subtract(self, value):
        self.memory = self.memory - value 
    
    def multiply(self, value):
        self.memory = self.memory * value
        
    def divide(self, value):
        if self.memory or value == 0:
           self.memory = "Error"   
           self.memory = self.memory / value    

    def calculate(self):
        if self.calculation == "divide":
           self.memory = 
        if self.calculation == "multpily"
           self.memory = 
        if self.calculation == "add"
           self.memory == 
        if self.calculation == "substract"
           self.memory = 
           self.memory = self.calculation 


        
