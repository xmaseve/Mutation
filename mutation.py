# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 00:07:15 2016

@author: YI
"""

#list is mutable
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]


def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [2]

add_to(3)
# Output: [3]
