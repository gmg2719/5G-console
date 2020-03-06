import sys

from PyQt5.QtGui import QStandardItemModel,  QStandardItem
from PyQt5.QtWidgets import (QApplication, QGroupBox, QHBoxLayout,  QTableView, QVBoxLayout, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
import io, csv

class ImsiList(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'IMSI List'
        self.left = 100
        self.top = 100
        self.width = 440
        self.height = 240

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.dataGroupBox = QGroupBox("IMSI From All Boards")
        self.dataView = QTableView()
        self.dataView.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.dataView.setAlternatingRowColors(True)
        self.dataView.setObjectName("dataView")
        
        self.dataView.installEventFilter(self) #copy function 在目标对象上调用installEventFilter()，注册监视对象。

        dataLayout = QHBoxLayout()
        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)
        
        self.__ColCount=4  #列数=3
        self.itemModel = QStandardItemModel(0,self.__ColCount,self)# 数据模型,10行6列
        
        self.dataView.setModel(self.itemModel)
        self.dataView.verticalHeader().setDefaultSectionSize(22)
        
        headerList=['时间', 'IMSI', 'RSSI', '来自板卡IP']      #转换为字符串列表
        self.itemModel.setHorizontalHeaderLabels(headerList)  #设置表头标题
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        self.setLayout(mainLayout)
#        for j in range(self.__ColCount):  #不含最后一列
#            strList=['Oct 20 2018, 14:05:16', '1234567890', '123', '192.168.2.53']
#            i=1
#            item=QStandardItem(strList[j])
#            self.itemModel.setItem(i-1,j,item)

        self.show()
        
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and
            event.matches(QtGui.QKeySequence.Copy)):
            self.copySelection()
            return True
        return super(QWidget, self).eventFilter(source, event)
	
    def copySelection(self):
        selection = self.dataView.selectedIndexes()
        if selection:
            rows = sorted(index.row() for index in selection)
            columns = sorted(index.column() for index in selection)
            rowcount = rows[-1] - rows[0] + 1
            colcount = columns[-1] - columns[0] + 1
            table = [[''] * colcount for _ in range(rowcount)]
            for index in selection:
                row = index.row() - rows[0]
                column = index.column() - columns[0]
                table[row][column] = index.data()
            stream = io.StringIO()
            csv.writer(stream).writerows(table)
            QApplication.clipboard().setText(stream.getvalue())
        
        


    def imsilistshow(self, strList, i):
        for j in range(self.__ColCount):  #不含最后一列
            item=QStandardItem(strList[j])
            self.itemModel.setItem(i-1,j,item)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImsiList()
    ex.initUI()
    sys.exit(app.exec_())
