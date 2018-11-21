#！/usr/bin/env/python
# -*- coding:utf-8 -*-
# Board是游戏主要逻辑
from PyQt5.QtWidgets import QFrame,QAction
from PyQt5.QtGui import QPainter,QColor
from PyQt5.QtCore import Qt,QBasicTimer,pyqtSignal

class Board(QFrame):

    def __init__(self):
        super(Board, self).__init__()

    """
    画图形的函数：
    @painter:画笔
    @x,y:坐标点
    @shape:形状
    """
    def drawSquare(self, painter, x, y, shape):
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]

        color = QColor(colorTable[shape])
        painter.fillRect()

