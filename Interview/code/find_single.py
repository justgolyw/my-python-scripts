#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-07-17
@FileName : find_single.py
"""

# 找到落单的元素

def find_single(L):
    result = 0
    for v in L:
        result ^= v
    if result == 0:
        print("没有落单的元素")
    else:
        print(f"落单元素是：{result}")

if __name__ == "__main__":
    L = [1,2,1,2,3,4]
    find_single(L)