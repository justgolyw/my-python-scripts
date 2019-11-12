#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/20
@FileName : insert_sort.py
"""

# 插入排序
def insert_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    # 假设第一个数据为有序的数据
    for i in range(1,n):
        j = i-1
        target = arr[i] # 待排序数据
        while j>=0 and target<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        if j!=i-1:
            arr[j+1] = target
    return arr

if __name__ == "__main__":
    arr = [1,3,5,2,4]
    new_arr = insert_sort(arr)

    print(new_arr)