# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 00:34:12 2024

@author: VanAnh
"""

import math

# a) Phương thức tính căn bậc x của số n
def can_bac_x(n, x):
    return n ** (1/x)

# b) Phương thức trả về số đảo
def so_dao(n):
    return int(str(n)[::-1])

# c) Phương thức kiểm tra có phải là số chính phương
def so_chinh_phuong(n):
    return int(math.sqrt(n))**2 == n

# d) Phương thức kiểm tra có phải là số nguyên tố
def so_nguyento(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# e) Phương thức tính tích các chữ số lẻ
def tich_so_le(n):
    tich = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            tich *= int(digit)
    return tich

# f) Phương thức tính tổng các số nguyên tố nhỏ hơn n
def tong_so_nguyen_to_nho_hon(n):
    return sum(i for i in range(2, n) if so_nguyento(i))

# g) Phương thức tính tổng các số chính phương nhỏ hơn n
def tong_so_chinh_phuong_nho_hon(n):
    return sum(i for i in range(1, n) if so_chinh_phuong(i))

# h) Phương thức tính tổng các ước số dương của n
def tong_uoc_so(n):
    return sum(i for i in range(1, n+1) if n % i == 0)

# Test
n = 36
x = 2
print ("a)",(can_bac_x(n, x)))
print("b)", so_dao(n))
print("c)", so_chinh_phuong(n))
print("d)", so_nguyento(n))
print("e)", tich_so_le(n))
print("f)", tong_so_nguyen_to_nho_hon(n))
print("g)", tong_so_chinh_phuong_nho_hon(n))
print("h)", tong_uoc_so(n))