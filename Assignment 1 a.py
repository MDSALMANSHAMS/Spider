# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:36:18 2022

@author: salma
"""
#assignment

a=int(input('enter number 1'))
b=int(input('enter number 2'))
c=input('give either add or sub or mul or div')

if c=="add":
    print(a+b)
elif c=="sub":
    print(a-b)
elif c=="mul":
    print(a*b)
elif c=="div":
    print(a/b)
else:
    print('wrong keyword')