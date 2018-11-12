#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""

import random, string
import uuid

forSelect = string.ascii_letters + "0123456789"
codeList = []

def generate(count, length):
    for i in range(count):
        code = ""
        for j in range(length):
            code += random.choice(forSelect)
        codeList.append(code)
    for code in codeList:
        print(code)


# 使用UUID
def generate2(count):
    codeList = []
    for i in range(count):
        code = str(uuid.uuid4()).replace('-','')
        codeList.append(code)
    for code in codeList:
        print(code)


if __name__ == "__main__":
    # generate(200,20)
    generate2(200)