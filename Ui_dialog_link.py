# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\ericWorkspace\mainwindow_dialog\dialog_link.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(349, 128)
        Dialog.setSizeGripEnabled(True)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 20, 77, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_link = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_link.setObjectName("pushButton_link")
        self.verticalLayout_3.addWidget(self.pushButton_link)
        self.pushButton_dislink = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_dislink.setObjectName("pushButton_dislink")
        self.verticalLayout_3.addWidget(self.pushButton_dislink)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_pcip = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_pcip.setObjectName("lineEdit_pcip")
        self.verticalLayout.addWidget(self.lineEdit_pcip)
        self.lineEdit_port = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.verticalLayout.addWidget(self.lineEdit_port)
        self.lineEdit_boardip = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_boardip.setObjectName("lineEdit_boardip")
        self.verticalLayout.addWidget(self.lineEdit_boardip)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(12, 90, 168, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.comboBox_main = QtWidgets.QComboBox(self.widget1)
        self.comboBox_main.setObjectName("comboBox_main")
        self.comboBox_main.addItem("")
        self.comboBox_main.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_main)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "连接设置"))
        self.pushButton_link.setText(_translate("Dialog", "连接"))
        self.pushButton_dislink.setText(_translate("Dialog", "断开"))
        self.label.setText(_translate("Dialog", "主机IP"))
        self.label_2.setText(_translate("Dialog", "端口号"))
        self.label_3.setText(_translate("Dialog", "板卡IP"))
        self.lineEdit_pcip.setText(_translate("Dialog", "192.168.2.11"))
        self.lineEdit_port.setText(_translate("Dialog", "3345"))
        self.lineEdit_boardip.setText(_translate("Dialog", "192.168.2.53"))
        self.label_4.setText(_translate("Dialog", "模式"))
        self.comboBox.setItemText(1, _translate("Dialog", "TCP"))
        self.comboBox.setItemText(0, _translate("Dialog", "UDP"))
        self.comboBox_main.setItemText(0, _translate("Dialog", "主控模式"))
        self.comboBox_main.setItemText(1, _translate("Dialog", "非主控模式"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
