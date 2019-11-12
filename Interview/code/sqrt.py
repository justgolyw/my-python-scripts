#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/24
@FileName : sqrt.py
"""

# 开根号的实现
# n为开根号数，p为精度
import math
from math import fabs

def my_sqrt(n,p):

    _max = n
    _min = 0.0
    mid = (_max+_min)/2.0
    while fabs(mid*mid-n) > p:
        if mid*mid < n:
            _min = mid
        elif mid*mid > n:
            _max = mid
        else:
            return mid
        mid = (_max+_min)/2.0
    return mid

def Sqrt(val):
    low = 0.0
    high = val
    mid = (low+high)/2.0
    while low<=high:
        if mid*mid >val:
            high = mid -1
        elif mid*mid <val:
            low = mid+1
        else:
            return mid
        mid = (low+high)/2.0
    return mid


if __name__ == "__main__":
    # re = Sqrt(1.44)
    re = math.sqrt(0.01)
    print(re)