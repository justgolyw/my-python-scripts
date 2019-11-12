#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/20
@FileName : shell_sort.py
"""

# shell 排序：缩小增量排序
def Shell_sort(array):
    def shell_sort(arr,gap):
        n =len(arr)
        for i in range(gap,n):
            target = arr[i]
            j = i-gap
            while j>=0 and target<arr[j]:
                arr[j+gap]=arr[j]
                j -= gap
            if j != i - gap:
                arr[j+gap] = target

    N = len(array)
    if N<=1:
        return array
    gap = N//2
    while gap>=1:
        shell_sort(array,gap)
        gap=gap//2
    return arr

def insert_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    # 假设第一个数据为有序的数据
    for i in range(1,n):
        j = i
        target = arr[i] # 待排序数据下标
        while j>0 and target<arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = target
    return arr

if __name__ == "__main__":
    arr = [3, 1, 18, 2, 4,19,0,2,1]
    new_arr = Shell_sort(arr)

    print(new_arr)











