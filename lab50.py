# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:22:20 2024

@author: VanAnh
"""

def ktra_so(n):
    if n<0 and n%2 !=0:
        return -1
    elif n>0 and n%2 ==0:
        return 1
    return 0
        
        
if __name__=="__main__":
    print(ktra_so(-3))  