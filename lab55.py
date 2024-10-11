# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:00:31 2024

@author: VanAnh
"""

# chu vi hình chữ nhật
def chu_vi(dai, rong):
    return 2 * (dai + rong)

# diện tích hình chữ nhật
def dien_tich(dai, rong):
    return dai * rong

#  vẽ hình chữ nhật bằng dấu *
def ve_hinh_chu_nhat(dai, rong):
    for i in range(rong):
        print('* ' * dai)

# Ví dụ
dai = 5
rong = 3
print("Chu vi:", chu_vi(dai, rong))
print("Diện tích:", dien_tich(dai, rong))
ve_hinh_chu_nhat(dai, rong)
