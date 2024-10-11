# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 01:17:18 2024

@author: VanAnh
"""

import math

def tinh(hinh, pheptinh, *args, **kwargs):
    if hinh == 'vuong':
        canh = args[0]
        return canh * 4 if pheptinh == "cv" else canh ** 2
    elif hinh == 'chu_nhat':
        dai, rong = args
        return 2 * (dai + rong) if pheptinh == "cv" else dai * rong
    elif hinh == 'tron':
        bk = args[0]
        return 2 * math.pi * bk if pheptinh == "cv" else math.pi * bk ** 2
    else:
        return "Không hợp lệ"
    
    
print(tinh('vuong', 'cv', 10))  
print(tinh('vuong', 'dt', 50))  
print(tinh('tron', 'cv', 18))  
print(tinh('tron', 'dt', 18)) 
print(tinh('chu_nhat', 'cv', 20, 30)) 
print(tinh('chu_nhat', 'dt', 20, 30))  
