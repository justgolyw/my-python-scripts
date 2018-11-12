# -*- coding: utf-8 -*-
"""
第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数
"""
# a-z：97-122
#
# A-Z：65-90
#
# 0-9：48-57

count = 0
_list = []
# 读取文件
with open("0004Test.txt",'r') as f:
    text = f.read()  # return str

for t in text:
    if ord(t) in range(97,123) or ord(t) in range(65,91):
        _list.append(t)
        count += 1
    # if ord(t) in range(65,91):
    #     count += 1
    #     _list.append(t)

print(count)
print(_list)


