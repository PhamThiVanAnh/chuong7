# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:46:12 2024

@author: VanAnh
"""
def f(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

f(10)  


