# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pyqt work\mainwindow_dialog\dialog_workmode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,  Qt
from PyQt5.QtWidgets import QHeaderView


class Ui_Dialog_workmode(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 489)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_workmode = QtWidgets.QTabWidget(Dialog)
        self.tabWidget_workmode.setObjectName("tabWidget_workmode")
        
        self.tab_wl = QtWidgets.QWidget()
        self.tab_wl.setObjectName("tab_wl")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_wl)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_wl = QtWidgets.QTableWidget(self.tab_wl)
        self.tableWidget_wl.setObjectName("tableWidget_wl")
        self.tableWidget_wl.setColumnCount(3)
        self.tableWidget_wl.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_wl.setItem(3, 2, item)
        self.gridLayout_2.addWidget(self.tableWidget_wl, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_wl_work_ok = QtWidgets.QPushButton(self.tab_wl)
        self.pushButton_wl_work_ok.setObjectName("pushButton_wl_work_ok")
        self.horizontalLayout.addWidget(self.pushButton_wl_work_ok)
        self.pushButton_wl_work_cancel = QtWidgets.QPushButton(self.tab_wl)
        self.pushButton_wl_work_cancel.setObjectName("pushButton_wl_work_cancel")
        self.horizontalLayout.addWidget(self.pushButton_wl_work_cancel)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.tabWidget_workmode.addTab(self.tab_wl, "")
        self.combox_wlworkmode = QtWidgets.QComboBox()
        self.combox_wlworkmode.addItem('持续侦码模式')
        self.combox_wlworkmode.addItem('周期侦码模式')
        self.combox_wlworkmode.addItem('管控模式')
        self.combox_wlworkmode.addItem('重定向模式')
        self.tableWidget_wl.setCellWidget(0, 1, self.combox_wlworkmode)
        
        self.combox_redirectsub = QtWidgets.QComboBox()
        self.combox_redirectsub.addItem('名单中的用户执行重定向；名单外的全部踢回公网')
        self.combox_redirectsub.addItem('名单中的用户踢回公网；名单外的全部重定向')
        self.combox_redirectsub.addItem('名单中的用户执行重定向；名单外的全部吸附在本站')
        self.combox_redirectsub.addItem('名单中的用户吸附在本站;名单外的全部重定向')
        self.combox_redirectsub.addItem('所有目标重定向')
        self.tableWidget_wl.setCellWidget(1, 1, self.combox_redirectsub)
        
        self.combox_controlsub = QtWidgets.QComboBox()
        self.combox_controlsub.addItem('黑名单子模式')
        self.combox_controlsub.addItem('白名单子模式')
        self.combox_controlsub.addItem('全黑子模式')
        self.tableWidget_wl.setCellWidget(3, 1, self.combox_controlsub)
        self.tableWidget_wl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  #设置单元格宽度随内容自动改变
        self.tableWidget_wl.horizontalHeader().setVisible(True)
        self.tableWidget_wl.verticalHeader().setVisible(False)
        
        
        self.tab_dw = QtWidgets.QWidget()
        self.tab_dw.setObjectName("tab_dw")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_dw)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableWidget_dw = QtWidgets.QTableWidget(self.tab_dw)
        self.tableWidget_dw.setObjectName("tableWidget_dw")
        self.tableWidget_dw.setColumnCount(3)
        self.tableWidget_dw.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_dw.setItem(6, 1, item)
        self.gridLayout_3.addWidget(self.tableWidget_dw, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_dw_work_ok = QtWidgets.QPushButton(self.tab_dw)
        self.pushButton_dw_work_ok.setObjectName("pushButton_dw_work_ok")
        self.horizontalLayout_2.addWidget(self.pushButton_dw_work_ok)
        self.pushButton_dw_work_cancel = QtWidgets.QPushButton(self.tab_dw)
        self.pushButton_dw_work_cancel.setObjectName("pushButton_dw_work_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_dw_work_cancel)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.tabWidget_workmode.addTab(self.tab_dw, "")
        
        self.combox_dwworkmode = QtWidgets.QComboBox()
        self.combox_dwworkmode.addItem('持续侦码模式')
        self.combox_dwworkmode.addItem('周期侦码模式')
        self.combox_dwworkmode.addItem('管控模式')
        self.combox_dwworkmode.addItem('重定向模式')
        self.tableWidget_dw.setCellWidget(0, 1, self.combox_dwworkmode)
        
        self.combox_dwredirectsub = QtWidgets.QComboBox()
        self.combox_dwredirectsub.addItem('名单中的用户执行重定向；名单外的全部踢回公网')
        self.combox_dwredirectsub.addItem('名单中的用户踢回公网；名单外的全部重定向')
        self.combox_dwredirectsub.addItem('名单中的用户执行重定向；名单外的全部吸附在本站')
        self.combox_dwredirectsub.addItem('名单中的用户吸附在本站;名单外的全部重定向')
        self.combox_dwredirectsub.addItem('所有目标重定向')
        self.tableWidget_dw.setCellWidget(1, 1, self.combox_dwredirectsub)
        
        self.combox_dwcontrolsub = QtWidgets.QComboBox()
        self.combox_dwcontrolsub.addItem('黑名单子模式')
        self.combox_dwcontrolsub.addItem('白名单子模式')
        self.combox_dwcontrolsub.addItem('全黑子模式')
        self.tableWidget_dw.setCellWidget(10, 1, self.combox_dwcontrolsub)
        
        self.combox_dwreport = QtWidgets.QComboBox()
        self.combox_dwreport.addItem('120ms')
        self.combox_dwreport.addItem('240ms')
        self.combox_dwreport.addItem('480ms')
        self.combox_dwreport.addItem('640ms')
        self.combox_dwreport.addItem('1024ms')
        self.combox_dwreport.addItem('2048ms')
        self.tableWidget_dw.setCellWidget(4, 1, self.combox_dwreport)
        
        self.combox_dwuepmax = QtWidgets.QComboBox()
        self.combox_dwuepmax.addItem('打开')
        self.combox_dwuepmax.addItem('关闭')
        self.tableWidget_dw.setCellWidget(5, 1, self.combox_dwuepmax)
        
        self.combox_dwprb = QtWidgets.QComboBox()
        self.combox_dwprb.addItem('打开')
        self.combox_dwprb.addItem('关闭')
        self.tableWidget_dw.setCellWidget(7, 1, self.combox_dwprb)
        
        self.combox_dwcampon = QtWidgets.QComboBox()
        self.combox_dwcampon.addItem('打开')
        self.combox_dwcampon.addItem('关闭')
        self.tableWidget_dw.setCellWidget(8, 1, self.combox_dwcampon)
        
        self.combox_dwsrs = QtWidgets.QComboBox()
        self.combox_dwsrs.addItem('打开')
        self.combox_dwsrs.addItem('关闭')
        self.tableWidget_dw.setCellWidget(9, 1, self.combox_dwsrs)
        
        self.tableWidget_dw.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)  #设置单元格宽度随内容自动改变
        self.tableWidget_dw.horizontalHeader().setVisible(True)
        self.tableWidget_dw.verticalHeader().setVisible(False)
        
        self.gridLayout.addWidget(self.tabWidget_workmode, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget_workmode.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget_wl.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_wl.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_wl.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget_wl.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget_wl.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "对象"))
        item = self.tableWidget_wl.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "值"))
        item = self.tableWidget_wl.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "注释"))
        __sortingEnabled = self.tableWidget_wl.isSortingEnabled()
        self.tableWidget_wl.setSortingEnabled(False)
        item = self.tableWidget_wl.item(0, 0)
        item.setText(_translate("Dialog", "工作模式"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_wl.item(1, 0)
        item.setText(_translate("Dialog", "重定向子模式"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        
        item = self.tableWidget_wl.item(2, 1)
        item.setText(_translate("Dialog", "60"))
        
        item = self.tableWidget_wl.item(1, 2)
        item.setText(_translate("Dialog", "只在重定向模式下生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_wl.item(2, 0)
        item.setText(_translate("Dialog", "周期模式采集周期"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_wl.item(2, 2)
        item.setText(_translate("Dialog", "只在周期模式下生效，单位分钟1~65535"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_wl.item(3, 0)
        item.setText(_translate("Dialog", "管控子模式"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_wl.item(3, 2)
        item.setText(_translate("Dialog", "只在管控模式下生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        self.tableWidget_wl.setSortingEnabled(__sortingEnabled)
        self.pushButton_wl_work_ok.setText(_translate("Dialog", "配置"))
        self.pushButton_wl_work_cancel.setText(_translate("Dialog", "取消"))
        self.tabWidget_workmode.setTabText(self.tabWidget_workmode.indexOf(self.tab_wl), _translate("Dialog", "围栏工作模式配置"))
        item = self.tableWidget_dw.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1"))
        item = self.tableWidget_dw.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_dw.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget_dw.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget_dw.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget_dw.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget_dw.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7"))
        item = self.tableWidget_dw.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8"))
        item = self.tableWidget_dw.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9"))
        item = self.tableWidget_dw.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10"))
        item = self.tableWidget_dw.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "11"))
        item = self.tableWidget_dw.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "对象"))
        item = self.tableWidget_dw.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "值"))
        item = self.tableWidget_dw.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "注释"))
        __sortingEnabled = self.tableWidget_dw.isSortingEnabled()
        self.tableWidget_dw.setSortingEnabled(False)
        item = self.tableWidget_dw.item(0, 0)
        item.setText(_translate("Dialog", "工作模式"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(1, 0)
        item.setText(_translate("Dialog", "重定向子模式"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(1, 2)
        item.setText(_translate("Dialog", "只在重定向模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(2, 0)
        item.setText(_translate("Dialog", "周期模式采集周期"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(2, 2)
        item.setText(_translate("Dialog", "只在周期模式生效，单位分钟1~65535"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(3, 0)
        item.setText(_translate("Dialog", "定位IMSI"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(3, 2)
        item.setText(_translate("Dialog", "只在定位模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(4, 0)
        item.setText(_translate("Dialog", "定位值上报周期"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(4, 2)
        item.setText(_translate("Dialog", "只在定位模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(5, 0)
        item.setText(_translate("Dialog", "终端最大发射功率开关"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(5, 2)
        item.setText(_translate("Dialog", "只在定位模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(6, 0)
        item.setText(_translate("Dialog", "终端允许的最大发射功率"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(6, 2)
        item.setText(_translate("Dialog", "只在定位模式生效，单位dBm 0~23"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(7, 0)
        item.setText(_translate("Dialog", "固定PRB开关"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(7, 2)
        item.setText(_translate("Dialog", "只在定位模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(8, 0)
        item.setText(_translate("Dialog", "非定位终端驻留开关"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(8, 2)
        item.setText(_translate("Dialog", "只在定位模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(9, 0)
        item.setText(_translate("Dialog", "SRS开关"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(9, 2)
        item.setText(_translate("Dialog", "只在定位模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(10, 0)
        item.setText(_translate("Dialog", "管控模式"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(10, 2)
        item.setText(_translate("Dialog", "只在管控模式生效"))
        item.setFlags(QtCore.Qt.ItemIsEditable)
        item = self.tableWidget_dw.item(2, 1)
        item.setText(_translate("Dialog", "60"))
        item = self.tableWidget_dw.item(3, 1)
        item.setText(_translate("Dialog", "460001111111111"))
        item = self.tableWidget_dw.item(6, 1)
        item.setText(_translate("Dialog", "23"))
        self.tableWidget_dw.setSortingEnabled(__sortingEnabled)
        self.pushButton_dw_work_ok.setText(_translate("Dialog", "配置"))
        self.pushButton_dw_work_cancel.setText(_translate("Dialog", "取消"))
        self.tabWidget_workmode.setTabText(self.tabWidget_workmode.indexOf(self.tab_dw), _translate("Dialog", "定位工作模式配置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_workmode()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
