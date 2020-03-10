# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\ericWorkspace\5G console\emptyerr.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_emptyerr(object):
    def setupUi(self, emptyerr):
        emptyerr.setObjectName("emptyerr")
        emptyerr.resize(237, 42)
        self.label = QtWidgets.QLabel(emptyerr)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(100)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(emptyerr)
        QtCore.QMetaObject.connectSlotsByName(emptyerr)

    def retranslateUi(self, emptyerr):
        _translate = QtCore.QCoreApplication.translate
        emptyerr.setWindowTitle(_translate("emptyerr", "错误"))
        self.label.setText(_translate("emptyerr", "错误:参数不能为空!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    emptyerr = QtWidgets.QWidget()
    ui = Ui_emptyerr()
    ui.setupUi(emptyerr)
    emptyerr.show()
    sys.exit(app.exec_())
