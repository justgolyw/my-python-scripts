#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 11/7/2018
@FileName : window.py
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton, QFileDialog,
                             QMessageBox, QVBoxLayout, QHBoxLayout)
from PyQt5 import QtCore
import sys

from xml2excel.Xml2Excel import Xml2Excel
import logging

# 添加log记录错误消息
logger = logging.getLogger("error_log")
logger.setLevel(logging.ERROR)
# 日志写入文件的方式默认是追加写入，改为覆盖写入，即日志中记录当次运行出错信息
file_hander = logging.FileHandler("error_output.log", encoding="utf-8", mode="w")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_hander.setFormatter(formatter)
logger.addHandler(file_hander)


class window(QWidget):

    def __init__(self):

        # 调用父类初始化函数
        super().__init__()
        self.element_dict = {}
        self.initUI()

    def initUI(self):
        label_1 = QLabel('导入xml文件:')
        self.msg_text1 = QLineEdit()
        button_Open1 = QPushButton('Open')

        label_2 = QLabel('导出文件保存路径:')
        self.msg_text2 = QLineEdit()
        button_Open2 = QPushButton('Open')

        # 设置按钮大小
        button_Open1.setFixedSize(QtCore.QSize(60,30))
        # 点击打开按钮打开选择文件对话框
        button_Open1.clicked.connect(self.open_fileDialog)

        # 设置按钮大小
        button_Open2.setFixedSize(QtCore.QSize(60, 30))
        # 点击打开按钮打开保存文件对话框
        button_Open2.clicked.connect(self.save_fileDialog)

        button_start = QPushButton('start')
        button_start.setFixedSize(QtCore.QSize(60, 30))
        button_start.clicked.connect(self.convert_xml_to_excel)
        button_quit = QPushButton('exit')
        button_quit.setFixedSize(QtCore.QSize(60, 30))
        # 点击quit按钮退出程序
        button_quit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        # 使用表格布局
        grid = QGridLayout()
        # 设置表格组件之间的间距
        grid.setSpacing(10)
        # 设置组件存放位置，在表格布局中所处的行和列
        grid.addWidget(label_1,1,1)
        grid.addWidget(self.msg_text1,1,2)
        grid.addWidget(button_Open1,1,3)

        grid.addWidget(label_2,2,1)
        grid.addWidget(self.msg_text2,2,2)
        grid.addWidget(button_Open2,2,3)

        grid.addWidget(button_start,3,1)
        grid.addWidget(button_quit,3,3)
        # grid.addWidget(button_clean,3,3)

        self.setLayout(grid)

        # 设置窗口标题
        self.setWindowTitle('测试用例转换')
        self.setGeometry(300,300,500,300)
        self.show()

    # 打开文件对话框
    def open_fileDialog(self):
        """
        getOpenFileName()方法的第一个字符串参数'Open File'将显示在弹出对话框的标题栏。
        第二个字符串参数用来指定对话框的工作目录。
        默认情况下文件过滤器被设置为不过滤任何文件(所有工作目录中的文件/文件夹都会被显示)。

        """
        self.file_path = QFileDialog.getOpenFileName(self,'Open File','.',"Text Files (*.xml)")
        print(self.file_path)
        # self.file_path = QFileDialog.getExistingDirectory(self,'Open File','.')
        # print('路径',file_path)
        if self.file_path[0]:
            self.msg_text1.setText(self.file_path[0])
        else:
            # 没有选择任何文件时弹出警告框，必须加上self参数
            QMessageBox.information(self,"Waring!","没有选择任何文件")

    # 保存文件对话框
    def save_fileDialog(self):
        """
        getOpenFileName()方法的第一个字符串参数'Open File'将显示在弹出对话框的标题栏。
        第二个字符串参数用来指定对话框的工作目录。
        默认情况下文件过滤器被设置为不过滤任何文件(所有工作目录中的文件/文件夹都会被显示)。

        """
        # self.save_path = QFileDialog.getOpenFileName(self,'Save File','.',"All Files (*);;Text Files (*.xlsx)")
        # 开始设置的文件夹路径
        # self.save_path = QFileDialog.getExistingDirectory(self, "Save Directory", ".")
        # 设置保存文件的路径
        self.save_path = QFileDialog.getSaveFileName(self, 'Save File', '.', 'Text Files (*.xlsx)')
        print(self.save_path)
        # self.file_path = QFileDialog.getExistingDirectory(self,'Open File','.')
        # print('路径',file_path)
        if self.save_path[0]:
            self.msg_text2.setText(self.save_path[0])
        else:
            # 没有选择任何文件时弹出警告框，必须加上self参数
            QMessageBox.information(self,"Waring!","没有选择保存路径")

    # xml转换成excel
    def convert_xml_to_excel(self):
        try:
            file_path = self.file_path[0]  # 获取xml文件路径
            save_path = self.save_path[0]  # 获取导出文件的保存路径

            convert_instance = Xml2Excel()
            content = convert_instance.generate_excel(file_path)
            convert_instance.wriet2Excel2(save_path,content)
            QMessageBox.information(self, "转换成功提示", "生成的excel文件保存在{path}路径下".format(path=save_path))
        except Exception:
            logger.exception("xml转换成excel过程中出现异常", exc_info=True)
            QMessageBox.information(self, "转换失败提示", "转换失败！")


    # 清除文本框
    def clean_text(self):
        if self.msg_text1:
            self.msg_text1.setText('')
        if self.msg_text2:
            self.msg_text2.setText('')
        if self.display:
            self.display.setText('')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())