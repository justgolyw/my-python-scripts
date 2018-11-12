# -*- coding: utf-8 -*-
import os,re
from collections import Counter
"""
第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词
"""

# 从一个txt文件中找出出现次数最高的词及其对应次数，以元组形式返回
def count_words(path):
    _list = []
    if os.path.exists(path) and os.path.isdir(path):
        _list = os.listdir(path)
    # print(_list)

    for diary in _list:
        diary_path = os.path.join(path,diary)
        # print(diary_path)
        with open(diary_path,'r') as f:
            text = f.read().lower()
            # 正则表达式的用法？？
            pattern = '[a-z0-9\']+'

            words = re.findall(pattern,text)
            word_list = Counter(words)
        print(word_list.most_common()[0])


if __name__ == "__main__":
    count_words("diary")

