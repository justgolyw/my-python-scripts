#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
lxml学习笔记
"""
from lxml import etree

xml_string = '<root><foo id="foo-id" class="foo zoo">Foo</foo><bar>Chinese</bar><baz></baz></root>'
root = etree.fromstring(xml_string.encode('utf-8')) # 转化为xml
root.append(etree.Element("child")) # 添加子节点child
root.append(etree.SubElement(root,"child2")) # 添加子节点的另一种方法

print(type(root)) # <class 'lxml.etree._Element'>
# print(etree.tostring(root))
print(etree.tostring(root, pretty_print=True).decode('utf-8'))  # 格式化输出
# .tag 节点名字
print(root.tag) # root 根节点
print('next:',root.getnext())
print(root[0].tag) # foo
print(root[1].tag) # bar
print(root[2].tag) # foo
print("................")
# .text 输出节点内容
print(root[0].text)
print(root[1].text)

for child in root:
    print('子节点：', child.tag,end='  ') # 可以将root 看成一个list

print(">>>>>>>>")
for attr, val in root[0].items(): # root里面的每一个元素(子节点)都可以看成一个字典
    print(attr, val)
print(root[0].get('class'))
print("##############")

print(root[0].getparent().tag) # getparent()获取子节点的父节点
print(root[0].getnext().tag) # getnext()获取相邻节点的下一个节点
print(root[1].getprevious().tag) # getprevious()获取相邻节点的上一个节点

print(root[0].attrib) # attrib 获取字典属性



# # xml 是一个树形结构，lxml 使用etree._Element和 etree._ElementTree来分别代表树中的节点和树
# t = root.getroottree()
# print(t)
# print(t.getroot())
#
# foo_tree = etree.ElementTree(root)
# print(foo_tree.getroot().tag)