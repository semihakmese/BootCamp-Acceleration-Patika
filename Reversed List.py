# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:43:14 2022

@author: Semih
"""

l = [[1, 2], [3, 4], [5, 6, 7]]
for i in range(len(l)):
    l = l[::-1]
    for i in range(len(l)):
        l[i] = l[i][::-1]

print(l)