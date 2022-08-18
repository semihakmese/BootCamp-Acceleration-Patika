# -*- coding: utf-8 -*-
"""
@author: Semih
"""

#First of all we need to define our list
#After that we have to create a empty list to add flatten values
#So the function is going to scan whole values and check them if,
#is there any list object, that's gonna be converted by applying the function again.
#If not the value is going to add to our new list.


l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
l_flatten = []
def flatten(n):
    for item in n:
        if isinstance(item, list):
            flatten(item)
        else:
            l_flatten.append(item)

flatten(l)
print(l_flatten)