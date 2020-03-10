# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\ericWorkspace\5G console\dialog_cellnum.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_cellnum(object):
    def setupUi(self, Dialog_cellnum):
        Dialog_cellnum.setObjectName("Dialog_cellnum")
        Dialog_cellnum.resize(288, 143)
        Dialog_cellnum.setSizeGripEnabled(True)
        self.pushButton_cellnum = QtWidgets.QPushButton(Dialog_cellnum)
        self.pushButton_cellnum.setGeometry(QtCore.QRect(100, 110, 75, 23))
        self.pushButton_cellnum.setObjectName("pushButton_cellnum")
        self.layoutWidget = QtWidgets.QWidget(Dialog_cellnum)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 20, 221, 76))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox_dunum = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_dunum.setObjectName("comboBox_dunum")
        self.comboBox_dunum.addItem("")
        self.comboBox_dunum.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_dunum)
        self.comboBox_cell1num = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_cell1num.setObjectName("comboBox_cell1num")
        self.comboBox_cell1num.addItem("")
        self.comboBox_cell1num.addItem("")
        self.comboBox_cell1num.addItem("")
        self.comboBox_cell1num.addItem("")
        self.comboBox_cell1num.addItem("")
        self.comboBox_cell1num.addItem("")
        self.comboBox_cell1num.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_cell1num)
        self.comboBox_cell2num = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_cell2num.setObjectName("comboBox_cell2num")
        self.comboBox_cell2num.addItem("")
        self.comboBox_cell2num.addItem("")
        self.comboBox_cell2num.addItem("")
        self.comboBox_cell2num.addItem("")
        self.comboBox_cell2num.addItem("")
        self.comboBox_cell2num.addItem("")
        self.comboBox_cell2num.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox_cell2num)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.comboBox_dunum.currentTextChanged.connect(self.selectchange)

        self.retranslateUi(Dialog_cellnum)
        QtCore.QMetaObject.connectSlotsByName(Dialog_cellnum)

    def retranslateUi(self, Dialog_cellnum):
        _translate = QtCore.QCoreApplication.translate
        Dialog_cellnum.setWindowTitle(_translate("Dialog_cellnum", "添加小区"))
        self.pushButton_cellnum.setText(_translate("Dialog_cellnum", "确定"))
        self.label.setText(_translate("Dialog_cellnum", "DU数量"))
        self.label_2.setText(_translate("Dialog_cellnum", "DU1 Cell 数量"))
        self.label_3.setText(_translate("Dialog_cellnum", "DU2 Cell 数量"))
        self.comboBox_dunum.setItemText(0, _translate("Dialog_cellnum", "1"))
        self.comboBox_dunum.setItemText(1, _translate("Dialog_cellnum", "2"))
        self.comboBox_cell1num.setItemText(0, _translate("Dialog_cellnum", "0"))
        self.comboBox_cell1num.setItemText(1, _translate("Dialog_cellnum", "1"))
        self.comboBox_cell1num.setItemText(2, _translate("Dialog_cellnum", "2"))
        self.comboBox_cell1num.setItemText(3, _translate("Dialog_cellnum", "3"))
        self.comboBox_cell1num.setItemText(4, _translate("Dialog_cellnum", "4"))
        self.comboBox_cell1num.setItemText(5, _translate("Dialog_cellnum", "5"))
        self.comboBox_cell1num.setItemText(6, _translate("Dialog_cellnum", "6"))
        self.comboBox_cell2num.setItemText(0, _translate("Dialog_cellnum", "0"))

    def selectchange(self):
        _translate = QtCore.QCoreApplication.translate
        if self.comboBox_dunum.currentText() == '1':
            self.comboBox_cell1num.setItemText(0, _translate("Dialog_cellnum", "0"))
            self.comboBox_cell1num.setItemText(1, _translate("Dialog_cellnum", "1"))
            self.comboBox_cell1num.setItemText(2, _translate("Dialog_cellnum", "2"))
            self.comboBox_cell1num.setItemText(3, _translate("Dialog_cellnum", "3"))
            self.comboBox_cell1num.setItemText(4, _translate("Dialog_cellnum", "4"))
            self.comboBox_cell1num.setItemText(5, _translate("Dialog_cellnum", "5"))
            self.comboBox_cell1num.setItemText(6, _translate("Dialog_cellnum", "6"))
            self.comboBox_cell2num.setItemText(0, _translate("Dialog_cellnum", "0"))
            self.comboBox_cell2num.setItemText(1, _translate("Dialog_cellnum", ""))
            self.comboBox_cell2num.setItemText(2, _translate("Dialog_cellnum", ""))
            self.comboBox_cell2num.setItemText(3, _translate("Dialog_cellnum", ""))
            self.comboBox_cell2num.setItemText(4, _translate("Dialog_cellnum", ""))
            self.comboBox_cell2num.setItemText(5, _translate("Dialog_cellnum", ""))
            self.comboBox_cell2num.setItemText(6, _translate("Dialog_cellnum", ""))
        elif self.comboBox_dunum.currentText() == '2':
            self.comboBox_cell1num.setItemText(0, _translate("Dialog_cellnum", "0"))
            self.comboBox_cell1num.setItemText(1, _translate("Dialog_cellnum", "1"))
            self.comboBox_cell1num.setItemText(2, _translate("Dialog_cellnum", "2"))
            self.comboBox_cell1num.setItemText(3, _translate("Dialog_cellnum", "3"))
            self.comboBox_cell1num.setItemText(4, _translate("Dialog_cellnum", "4"))
            self.comboBox_cell1num.setItemText(5, _translate("Dialog_cellnum", "5"))
            self.comboBox_cell1num.setItemText(6, _translate("Dialog_cellnum", "6"))
            self.comboBox_cell2num.setItemText(0, _translate("Dialog_cellnum", "0"))
            self.comboBox_cell2num.setItemText(1, _translate("Dialog_cellnum", "1"))
            self.comboBox_cell2num.setItemText(2, _translate("Dialog_cellnum", "2"))
            self.comboBox_cell2num.setItemText(3, _translate("Dialog_cellnum", "3"))
            self.comboBox_cell2num.setItemText(4, _translate("Dialog_cellnum", "4"))
            self.comboBox_cell2num.setItemText(5, _translate("Dialog_cellnum", "5"))
            self.comboBox_cell2num.setItemText(6, _translate("Dialog_cellnum", "6"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_cellnum = QtWidgets.QDialog()
    ui = Ui_Dialog_cellnum()
    ui.setupUi(Dialog_cellnum)
    Dialog_cellnum.show()
    sys.exit(app.exec_())
