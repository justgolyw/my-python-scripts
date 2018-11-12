#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author: lyw
@Create date: 7/12/2018 
@FileName: selected_copy.py
项目要求：编写一个程序，遍历一个目录树，查找特定扩展名的文件（诸如.pdf 或.jpg），
不论这些文件的位置在哪里， 将它们拷贝到一个新的文件夹中,并且进行压缩。
"""

import os,shutil,zipfile

def selected_copy(folder,targetFolder):
    """
    :param folder:源文件夹
    :param targetFolder: 目标文件夹
    :return:
    """
    folder = os.path.abspath(folder)  # 绝对路径
    targetFolder = os.path.abspath(targetFolder)
    zipFilename = os.path.basename(targetFolder) +'.zip'
    print('Creating %s...' % (zipFilename))
	# os.path.join(os.path.dirname(targetFolder),zipFilename) 指定压缩文件的位置
    backupZip = zipfile.ZipFile(os.path.join(os.path.dirname(targetFolder),zipFilename),'w')  # 创建压缩文件

    if not os.path.exists(targetFolder):
        os.makedirs(targetFolder,exist_ok=True) # 目录不存在时创建目录 

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.py':
            # if filename.endswith('.py'):
                # 将.py 文件复制到目标文件夹
                shutil.copy(os.path.join(foldername,filename),targetFolder)

    # 压缩
    for foldername, subfolders, filenames in os.walk(targetFolder):

        for filename in filenames:
                # 将文件写入到压缩文件
                # 要想最终保存的路径为相对路径则需要加上arcname 参数
                backupZip.write(os.path.join(foldername,filename),filename)
    backupZip.close()


    print('Done')

selected_copy(r"C:\Users\yangwei.li\Desktop\my python scripts\calculator",r"C:\Users\yangwei.li\Desktop\my python scripts\find")