# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqt work\mainwindow_dialog\reboot.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView


class Ui_Dialog_reboot(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 157)
        Dialog.setMaximumSize(QtCore.QSize(538, 500))
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(320, 110))
        self.groupBox.setMaximumSize(QtCore.QSize(540, 120))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
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
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_reboot_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_reboot_ok.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_reboot_ok.setObjectName("pushButton_reboot_ok")
        self.horizontalLayout.addWidget(self.pushButton_reboot_ok)
        self.pushButton_reboot_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_reboot_cancel.setMaximumSize(QtCore.QSize(40, 30))
        self.pushButton_reboot_cancel.setObjectName("pushButton_reboot_cancel")
        self.horizontalLayout.addWidget(self.pushButton_reboot_cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.combox = QtWidgets.QComboBox()
        self.combox.addItem('重启后小区空闲')
        self.combox.addItem('重启后小区自激活')
        self.tableWidget.setCellWidget(0, 1, self.combox)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  #设置不可调整大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  #设置单元格宽度随内容自动改变

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "重启后小区状态设置"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "对象"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "值"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "注释"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Dialog", "重启后小区状态设置"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Dialog", "只对定位版本生效"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_reboot_ok.setText(_translate("Dialog", "配置"))
        self.pushButton_reboot_cancel.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_reboot()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
