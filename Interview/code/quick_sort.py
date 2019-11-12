#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/20
@FileName : quick_sort.py
"""

# 快速排序
def Quick_sort(arr):
    def partion(arr,left,right):
        key = left # 基准值
        while left < right:
            while left < right and arr[right]>=arr[key]:
                right -= 1
            # arr[key], arr[right] = arr[right], arr[key]

            while left < right and arr[left]<=arr[key]:
                left += 1
            # arr[key], arr[left] = arr[left], arr[key]

            arr[left],arr[right]=arr[right],arr[left]

        arr[left],arr[key]=arr[key],arr[left]
        return left #返回目前基准所在位置的索引

    def quick_sort(arr,left,right):
        if left >= right:
            return

        mid = partion(arr,left,right)
        quick_sort(arr,left,mid-1)
        quick_sort(arr,mid+1,right)

    # 主函数
    n = len(arr)
    if n<=1:
        return arr
    quick_sort(arr,0,n-1)
    return arr

if __name__ == "__main__":
    arr = [12,1,5,16,4,30,20]
    new_arr = Quick_sort(arr)
    print(new_arr)

