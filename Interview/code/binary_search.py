#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/21
@FileName : binary_search.py
"""

# 二分查找算法
def binary_search(arr,target):
    n = len(arr)
    left,right = 0,n-1
    while left <= right:
        mid = (left+right)//2
        if target > arr[mid]:
            left = mid+1
        elif target < arr[mid]:
            right = mid-1
        else:
            return mid
    return -1

if __name__ == "__main__":
    arr = [1,3,5,7,9]
    index = binary_search(arr,5)
    print(index)