#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:24:03 2020

@author: chenyinghui
"""
class Usernumber:
    def __init__(self,b,s):
        self.number1=b
        self.number2=s
    def bigsmall(self):
        if b>s:
            print(self.number1,">",self.number2)
        elif b==s:
            print(self.number1,"=",self.number2)
        else:
            print(self.number1,"<",self.number2)
    def plusplus(self):
        numberplus = int(b)+int(s)
        print(self.number1,"+",self.number2,"=",numberplus)
    def output(self):
        print("A是",self.number1,"，","B是",self.number2)
b=input("請輸入數字")
s=input("請再輸入一個數字")
number=Usernumber(b,s)
number.bigsmall()
number.plusplus()
number.output()
