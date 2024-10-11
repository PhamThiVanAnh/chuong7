# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:25:47 2024

@author: VanAnh
"""

def ktra_giatri():
    gtri = input ('nhap vao gia tri :')
    if gtri.strip('-').isdigit():
        gtri = int(gtri)
    if -89 <= gtri <= 90:
        return gtri
    print('khong hop le, nhap lai')
    return ktra_giatri()

if __name__=="__main__":
    print(ktra_giatri())  
