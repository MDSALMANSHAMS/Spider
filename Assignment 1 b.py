# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:39:27 2022

@author: salma
"""

a=int(input('enter number 1'))
b=int(input('enter number 2'))
c=input('give either & or | or ^ or ~ or >> or <<')

if c=="&":
    print(a&b)
elif c=="|":
    print(a|b)
elif c=="^":
    print(a^b)
elif c=="~":
    print(~b)
elif c==">>":
    print(a>>b)
elif c=="<<":
    print(a<<b)
else:
    print('wrong keyword')
    
    