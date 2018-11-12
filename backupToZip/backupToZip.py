#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: lyw
@Create date: 7/12/2018 
@FileName: backupToZip.py
"""

import zipfile, os


def backupToZip(folder):
    folder = os.path.abspath(folder)
    # 取相对路径
    # folder = os.path.relpath(folder,'.')
    num = 1
    # 利用此while循环确保zipFilename唯一
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(num) + '.zip'
        if not os.path.exists(zipFilename):
            break
        num = num + 1

    # create the zip file
    print('Creating %s...' %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w',zipfile.ZIP_DEFLATED)

    # 使用 os.walk()函数， 列出文件夹以及子文件夹中的每个文件
    for foldername, subfolders, filenames in os.walk(folder):
        # print(folder)
        fpath = folder.replace(folder, '')

        # 嵌套的 for 循环将遍历
        # filenames 列表中的每个文件。每个文件都被添加到 ZIP 文件中
        for filename in filenames:
            newBase = os.path.basename(folder)+'_'
            # 以前生成的备份ZIP 文件除外
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            # arcname:文件写入ZIP文档后保存的文件名
            backupZip.write(os.path.join(foldername,filename),filename)

    backupZip.close()
    print('Done')

backupToZip(r"C:\Users\yangwei.li\Desktop\my python scripts\find")