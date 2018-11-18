#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 11/17/2018
@FileName : get_pictures.py
"""
import os

import requests
from bs4 import BeautifulSoup

# 图片爬取
def get_pictures(url):
    # 获取html
    html = requests.get(url).text
    # 使用BeautifulSoup解析html
    bs = BeautifulSoup(html,features="html.parser")
    imgs = bs.find_all("img",class_ = "BDE_Image")
    # 创建一个存放图片的文件夹
    os.makedirs("Imgs",exist_ok=True)
    index = 1 # 图片编号
    print("开始下载......")
    for img in imgs:
        img_name = str(index)+".jpg"
        img_url = img['src']
        response = requests.get(img_url)
        response.raise_for_status()
        # with open(os.path.join("Imgs",img_name),os.path.basename(img_url)) as img_file:
        with open(os.path.join("Imgs",img_name),'wb') as img_file:
            # response.content 返回字节
            # response.text 返回str
            # 所以写入图片内容时必须使用response.content
            img_file.write(response.content)

        index += 1

    print("下载完成，总共%d张图片" % (index-1))

url = "http://tieba.baidu.com/p/2166231880"

get_pictures(url)







