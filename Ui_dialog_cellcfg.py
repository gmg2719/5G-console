# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqt work\mainwindow_dialog\dialog_cellcfg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5 import Qt


class Ui_Dialog_cellcfg(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(350, 434)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_cellcfg_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cellcfg_ok.setObjectName("pushButton_cellcfg_ok")
        self.horizontalLayout.addWidget(self.pushButton_cellcfg_ok)
        self.pushButton_cellcfg_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cellcfg_cancel.setObjectName("pushButton_cellcfg_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cellcfg_cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.combox = QtWidgets.QComboBox()
        self.combox.addItem('5')
        self.combox.addItem('10')
        self.combox.addItem('15')
        self.combox.addItem('20')
        self.tableWidget.setCellWidget(3, 1, self.combox)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  #设置单元格宽度随内容自动改变
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "小区参数配置"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "对象"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "值"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "注释"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "上行频点"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Dialog", "255"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "TDD:255 FDD:正常填写"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Dialog", "下行频点"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Dialog", "38950"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Dialog", "PLMN"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Dialog", "46000"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Dialog", "带宽"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("Dialog", "TDD不支持15M"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("Dialog", "BAND"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("Dialog", "40"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("Dialog", "实际频点，同Band对应"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("Dialog", "PCI"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("Dialog", "500"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("Dialog", "0~503"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("Dialog", "TAC"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("Dialog", "23154"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("Dialog", "0~65535"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("Dialog", "CellID"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("Dialog", "90005922"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("Dialog", "0x00000000~0x0FFFFFFF"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("Dialog", "UePmax"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("Dialog", "23"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("Dialog", "0~ 23dBm，默认值为23"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("Dialog", "参考信号功率"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("Dialog", "20"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("Dialog", "0~20 dBm"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_cellcfg_ok.setText(_translate("Dialog", "配置"))
        self.pushButton_cellcfg_cancel.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_cellcfg()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
