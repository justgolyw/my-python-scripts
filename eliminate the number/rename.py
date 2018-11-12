#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: lyw
@Create date: 7/13/2018 
@FileName: rename.py
消除消失的编号
"""

import os,shutil,re

def rename(folder):
    """
    使用正则表达式：
    1．用 import re 导入正则表达式模块。
    2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
    3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
    4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串
    """
    folder = os.path.abspath(folder)
    # cwd = os.getcwd() # 获取当前的工作路径
    fileList = []
    regrex = re.compile(r'test\d{3}.txt')
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if regrex.search(filename).group() != None:
                fileList.append(os.path.join(foldername,filename))

    fileList.sort() # 排序
    print(fileList)

    # 检查fileList里面遗漏的文件打印出来
    num = 1
    for filename in fileList:
        while True:
            # 'C:\\Users\\yangwei.li\\Desktop\\test\\test001.txt' 从后往前数比较方便(-1:-n)
            if int(filename[-7:-4]) == num:
                break
            print('lost ' + str(num).zfill(3) + '.txt')
            num += 1
        num += 1

    # 将所有的文件统一命名
    num = 1
    for filename in fileList:
        newFileName = filename[:-7] + str(num).zfill(3)+'.txt'
        print(newFileName)
        num += 1
        # shutil.move(filename, newFileName)
        os.rename(filename,newFileName)

rename(r"C:\Users\yangwei.li\Desktop\test")





