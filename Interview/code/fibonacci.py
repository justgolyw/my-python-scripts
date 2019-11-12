#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-07-17
@FileName : fibonacci.py
"""
#fibonacci 数列
def fibonacci(num):
    a, b = 0, 1
    l = [1]
    for i in range(num):
        a, b = b, a+b
        l.append(b)
    return l

if __name__ == "__main__":
    print(fibonacci(2))