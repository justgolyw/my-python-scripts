#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author : yangwei.li
@Create date : 10/23/2018
@FileName : calculate.py
"""

import sys
from math import sqrt

from PyQt5.QtWidgets import (QWidget, QGridLayout, QLineEdit,
                             QPushButton, QApplication, QMainWindow, QMenu, QAction)

from PyQt5 import QtCore, QtGui
import pyperclip

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.string = ''

        self.initUI()


    def initUI(self):
        main_frame = QWidget()
        self.setCentralWidget(main_frame) # 设置窗口中心的控件

        # 设置菜单栏
        menubar = self.menuBar()
        menu_view = menubar.addMenu('View')
        menu_edit = menubar.addMenu('Edit')
        menu_help = menubar.addMenu('Help')

        copyAct = QAction('Copy',self)
        copyAct.setShortcut('Ctrl+C') # 设置快捷键
        copyAct.triggered.connect(self.copyText)
        pasteAct = QAction('Paste',self)
        pasteAct.setShortcut('Ctrl+V')
        pasteAct.triggered.connect(self.pasteText)
        histotyMenu = QMenu('History', self)
        xxxAct = QAction('xxx', self)
        histotyMenu.addAction(xxxAct) # 三级菜单
        menu_edit.addAction(copyAct)
        menu_edit.addAction(pasteAct)
        menu_edit.addMenu(histotyMenu)

        self.grid = QGridLayout()
        self.display = QLineEdit('0')
        # self.display.setText("0")
        self.display.setReadOnly(True)  # 设置只读
        self.display.setFont(QtGui.QFont("arial", 20))  # 设置显示字体
        self.display.setAlignment(QtCore.Qt.AlignRight)  # 设置右对齐
        # display.setMaxLength(15)
        self.grid.addWidget(self.display, 0, 0, 1, 5)

        names = ['<—', 'CE', 'C', '±', '√',
                 '7', '8', '9', '/', '%',
                 '4', '5', '6', '*', '1/x',
                 '1', '2', '3', '-', '',
                 '', '', '.', '+', '']

        positions = [(i, j) for i in range(1, 6) for j in range(5)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.setFixedSize(QtCore.QSize(60, 30))  # 设置按钮大小
            button.clicked.connect(self.buttonClicked)
            self.grid.addWidget(button, *position)

        button_equal = QPushButton("=")
        button_equal.setFixedSize(QtCore.QSize(60, 70))  # 设置按钮大小
        button_equal.clicked.connect(self.buttonClicked)
        self.grid.addWidget(button_equal, 4, 4, 2, 1)

        button_zero = QPushButton("0")
        button_zero.setFixedHeight(30) # 设置固定高度
        button_zero.clicked.connect(self.buttonClicked)
        self.grid.addWidget(button_zero, 5, 0, 1, 2) # 参数：起始行，起始列，行数，列数

        main_frame.setLayout(self.grid)
        # self.move(300, 150)
        # 设置窗口标题
        self.setWindowTitle('Calculator')
        # 设置窗口图标
        img_path = r"C:\Users\yangwei.li\Desktop\my python scripts\calculator\calculator.jpg"
        self.setWindowIcon(QtGui.QIcon(img_path))
        self.setGeometry(200, 200, 100, 300)
        self.show()

    def buttonClicked(self):
        text = self.sender().text()
        if text == 'CE' or text == 'C':
            self.string = '0'
        elif text == "<—":
            if len(self.string) > 1:
                    self.string = self.string[0:len(self.string)-1]
            else:
                self.string = '0'
        elif text in "+-*/%":
            self.string = self.string + text
        elif text == "=":
            self.string = str(eval(self.string))
        elif text =='±':
            if int(self.string) <= 0:
                self.string = str(abs(int(self.string)))
            else:
                self.string = '-' + self.string
        elif text == '√':
            self.string = str(sqrt(int(self.string)))
        elif text == '1/x':
            if int(self.string) != 0:
                self.string = str(1 / int(self.string))
            else:
                self.string = 'error'

        else:
            self.string = self.string + text if self.string != '0' else text

        self.display.setText(self.string) # 设置显示

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.string)

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.string = clipboard.setText(clipboard.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
