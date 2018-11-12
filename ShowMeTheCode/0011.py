#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，
则打印出 Freedom，否则打印出 Human Rights
"""


# 对文件的处理，最好加上try,except,处理异常
def filter():
    try:
        with open('0011Test.txt','r',encoding='utf-8') as f:
            sensitive_words = []
            for line in f:
                sensitive_words.append(line.strip())
        print(sensitive_words)
        while True:
            # 从键盘输入词语
            word = input('输入词语：')
            if word == "exit":
                break
            elif word in sensitive_words:
                print("Freedom")
            else:
                print("Human Rights")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    filter()