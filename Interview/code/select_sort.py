#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/20
@FileName : select_sort.py
"""

# 选择排序
def select_sort(arr):
    n = len(arr)
    if n<=1:
        return arr
    for i in range(0,n-1):
        min_index= i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index = j
        if min_index != i:
            arr[min_index],arr[i]=arr[i],arr[min_index]


    return arr

if __name__ == "__main__":
    arr = [3,1,5,2,4]
    new_arr = select_sort(arr)

    print(new_arr)