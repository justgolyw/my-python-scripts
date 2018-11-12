#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
第 0008 题： 一个HTML文件，找出里面的正文
第 0009 题： 一个HTML文件，找出里面的链接
"""

import requests
from bs4 import BeautifulSoup

def find_text(url):
    # 获取协议，域名
    # proto, rest = urllib.splittype(url)
    # domain = urllib.splithost(rest)[0]

    response = requests.get(url)
    response.raise_for_status() # 判断网页是否正确响应
    # print(response.text)
    # with open("test.html",'w',encoding='utf-8') as f:  # 文本不存在时会自动创建文本
    #     # 注意：必须制定编码为utf-8，否则会报告编码错误
    #     f.write(response.text) # 将网页内容写入文本

    soup = BeautifulSoup(response.text,features='html.parser')
    print(soup.body.text) # 打印HTML正文
    a = soup.find_all('a')
    # print(a)
    print("***************")
    for i in a:
        print(i['href'])  # 打印HTML连接

    # print(response.text)

if __name__ == "__main__":
    # find_text("http://www.baidu.com")
    find_text("https://123.sogou.com/")
