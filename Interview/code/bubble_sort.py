#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/20
@FileName : bubble_sort.py
"""

# 冒泡排序
def bubble_sort(arr):

    n=len(arr)
    if n<=1:
        return arr

    for i in range(0,n):
        flage = True
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flage=False

        if flage:
            break


    return arr


if __name__ == "__main__":
    arr = [3,1,5,2,4]
    new_arr = bubble_sort(arr)

    print(new_arr)
