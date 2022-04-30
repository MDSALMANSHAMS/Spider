# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 10:01:41 2022

@author: salma
"""

#pattern problem
n=int(input('enter number'))
for i in range(n):
     for j in range(i+1):
         print("*",end=" ")
     print()
     