#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019/4/21
@FileName : Merger_sort.py
"""
# 归并排序
class Merger_sort:

    # 归并
    def merger(arr,left,mid,right):
        temp = []
        i,j = left,mid+1
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid: # 将左边剩余元素填充进temp中
            temp.append(arr[i])
            i+=1
        while j<=right: # 将右边剩余元素填充进temp中
            temp.append(arr[j])
            j+=1
         # 将temp 中的元素全部拷贝到原始数组中

        t = 0
        while left<=right:
            arr[left] = temp[t]
            left+=1
            t+=1

    def msort(self,arr,left,right):
        if left>=right:
            return
        mid = (left+right)//2
        self.msort(arr,left,mid)
        self.msort(arr,mid+1,right)
        self.merger(arr,left,mid,right)

    def sort(self,arr):
        n = len(arr)
        if n<=1:
            return arr
        self.msort(arr,0,n-1)
        return arr


def Merger_sort2(arr):
    # 归并
    def merger(arr,left,mid,right):
        temp = []
        i,j = left,mid+1
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                temp.append(arr[i])
                i+=1
            else:
                temp.append(arr[j])
                j+=1
        while i<=mid: # 将左边剩余元素填充进temp中
            temp.append(arr[i])
            i+=1
        while j<=right: # 将右边剩余元素填充进temp中
            temp.append(arr[j])
            j+=1

        # 将temp 中的元素全部拷贝到原始数组中
        t = 0
        while left<=right:
            arr[left] = temp[t]
            left+=1
            t+=1

    def msort(arr,left,right):
        if left>=right:
            return
        mid = (left+right)//2
        msort(arr,left,mid)
        msort(arr,mid+1,right)
        merger(arr,left,mid,right)


    n = len(arr)
    if n<=1:
        return arr
    msort(arr,0,n-1)
    return arr

if __name__ == "__main__":
    arr = [1,4,5,2,2]
    # merger_sort = Merger_sort()
    # new_arr = merger_sort.sort(arr)
    new_arr = Merger_sort2(arr)
    print(new_arr)