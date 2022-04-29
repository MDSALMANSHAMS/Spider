# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:11:33 2022

@author: salma
"""

#Febbonaci problem
a=0
b=1
n=int(input('enter number of febbo to be printed'))
if n==0:
    print('wrong input')
elif n==1:
    print(a)
    
c=0

while c<n:
    print(a)
    s=a+b
    a=b
    b=s
    
    c=c+1
    
     
    