# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:56:56 2024

@author: VanAnh
"""

# a) 
def sum_a(n):
    return sum(range(1, n + 1))

# b) 
def sum_b(n):
    return sum(i**2 for i in range(1, n + 1))

# c) 
def sum_c(n):
    return sum(1/i for i in range(1, n + 1))

# d) 
def sum_d(n):
    from math import factorial
    return sum(factorial(i) for i in range(1, n + 1))

# e)
def e(n):
    from math import prod
    return prod(range(1, n + 1))


n = 2
print(sum_a(n))  
print(sum_b(n))  
print(sum_c(n))  
print(sum_d(n))  
print(e(n))  
