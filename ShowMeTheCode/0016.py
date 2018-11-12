#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
"""
import openpyxl
import json

# 本题考查json文件转化为excel文件
def json_to_excel(path):
    # 创建excel文件
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "example"
    try:
        with open(path,"r",encoding="utf-8") as f:
            # 使用load函数将包含json数据的文本转化为python(dict)对象
            # 使用loads函数将包含json数据的字符串转化为python(dict)对象
            data = json.load(f) # return list
            print(data)
            for index, value in enumerate(data):
                for index2, value2 in enumerate(value):
                    sheet.cell(index+1,index2+1,value2)
            wb.save("number.xlsx")
            wb.close()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    json_to_excel("number.txt")