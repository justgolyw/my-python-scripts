#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来
"""
# python 3中只有unicode str，所以把decode方法去掉了

import re,os

def count_codeline(path):
    file_list = read_from_folder(path)
    # 遍历文件夹中的文件
    for file in file_list:
        file_path = os.path.join(path,file)
        # file_name = os.path.basename(file_path)
        file_name = file
        line_num = 0
        empty_line_num = 0
        note_num = 0
        note_flag = False
        # 读取文件时加上encoding="utf-8" 则不会出现打印乱码
        with open(file_path,'r',encoding="utf-8") as f:
            for line in f.readlines():
                # print(line)
                line_num += 1
                if line.strip().startswith('"""') and not note_flag: # 注释开始
                    note_num += 1
                    note_flag = True
                    continue   # 不加continue,则注释会比实际少一行，这一点我也没弄明白！！
                if line.strip().startswith('"""'):
                    note_flag = False
                    note_num += 1
                if line.strip().startswith('#') or note_flag: # 注释结束
                    note_num += 1

                if line.strip() == '':
                    empty_line_num += 1

        print("在%s中，共有%d行代码，其中有%d行空行，有%d行注释" % (file_name, line_num, empty_line_num, note_num))

# 遍历文件夹
def read_from_folder(path):
    file_list = []
    try:
        file_list = os.listdir(path)
    except Exception as e:
        print(e)
    return file_list  # 得到文件夹里面的文件


if __name__ == "__main__":
    count_codeline("0006Test")
    # file_list = read_from_folder("0006Test")
    # for file in file_list:
    #     print(file)
