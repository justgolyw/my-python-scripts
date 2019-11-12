#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 2019-07-17
@FileName : duplicate.py
"""

# 去重
def duplicate(numbers):
    """

    :param numbers:
    :return:
    """
    if numbers is None or len(numbers) <= 1:
        return False
    use_set = set()
    duplication = {}
    l = []
    for index, value in enumerate(numbers):
        if value not in use_set:
            use_set.add(value)
        else:
            # duplication[index] = value
            l.append(value)
    # return duplication
    return l

if __name__ == '__main__':

    d = duplicate([1, 2, -3, 4, 4, 95, 95, 2, 2, -3, 7, 7, 5])
    print(d)

