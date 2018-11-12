#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，
则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

import re
# 对文件的处理，最好加上try,except,处理异常
def filter():
    try:
        with open('0011Test.txt','r',encoding='utf-8') as f:
            sensitive_words = []
            for line in f:
                sensitive_words.append(line.strip())
        print(sensitive_words)
        while True:
            s = input('输入语句:\n')
            if s == 'exit':
                break
            for x in sensitive_words:
                if x in s:
                    s = s.replace(x, '*'*len(x))
            print(s)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    filter()