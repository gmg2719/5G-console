import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow ,  QDialog
from Ui_dialog_link import Ui_Dialog
from Ui_reboot import Ui_Dialog_reboot
from Ui_mainwindow import Ui_MainWindow
from Ui_IMSI_TreeView import ImsiList
from Ui_dialog_cellcfg import Ui_Dialog_cellcfg
from Ui_dialog_workmode import Ui_Dialog_workmode

import sys
import threading
import socket
import time
import stopThreading

imsinumber=1
socket_flag=''
main_flag=''
tabindex_ip={}
tabindex_boardport={}
tabindex_boardip={}
boardip_tcpsocket={}
tcpsocket_addr={}
#tcpsocket_addr 'addr'for(ip,port)
tabindex_socket={}
#send data to tabindex
board_severthtcp={}
board_severthudp={}
#used for stop thread throung linkdialog
boardip_winsocket={}
boardip_winudpsocket={}
#单继承
class logic_main(QMainWindow):
    signal_write_msg = QtCore.pyqtSignal(str, str)
    signal_operation_msg = QtCore.pyqtSignal(str, str)
    signal_query_msg = QtCore.pyqtSignal(str, str)
    def __init__(self, parent=None):
        #global tabNumber
        super().__init__(parent)
        self._mainui=Ui_MainWindow()
        self._mainui.setupUi(self)
        self.initUI()
        self.tcp_socket = None
        self.udp_socket = None
        self.client_socket_list = list()
        self.client_udpsocket_list = list()
        self.sever_th = None
        self.sever_thudp = None

        
    def initUI(self):
        self._mainui.actionlink.triggered.connect(linkdialog.show)
        self._mainui.actionchongqi.triggered.connect(rebootdialog.show)
        self._mainui.actionIMSI.triggered.connect(imsilistframe.initUI)
        self._mainui.actionnew_tab.triggered.connect(tabadd)
        self._mainui.cellcfgquery.triggered.connect(cellcfgquery)
        self._mainui.cellstatequery.triggered.connect(cellstatequery)
        self._mainui.pwrquery.triggered.connect(pwrquery)
        self._mainui.workmodequery.triggered.connect(workmodequery)
        self._mainui.cellcfgf003.triggered.connect(cellcfgdialog.show)
        self._mainui.workmodef006.triggered.connect(workmodedialog.show)
        linkdialog._linkui.pushButton_link.clicked.connect(linkClicked)
        linkdialog._linkui.pushButton_dislink.clicked.connect(dislinkClicked)
        rebootdialog._rebootui.pushButton_reboot_ok.clicked.connect(rebootClicked)
        rebootdialog._rebootui.pushButton_reboot_cancel.clicked.connect(rebootdialog.close)
        cellcfgdialog._cellcfgui.pushButton_cellcfg_ok.clicked.connect(cellcfgClicked)
        cellcfgdialog._cellcfgui.pushButton_cellcfg_cancel.clicked.connect(cellcfgdialog.close)
        workmodedialog._workmodeui.pushButton_wl_work_ok.clicked.connect(workmodecfgClicked)
        workmodedialog._workmodeui.pushButton_wl_work_cancel.clicked.connect(workmodedialog.close)
        workmodedialog._workmodeui.pushButton_dw_work_ok.clicked.connect(workmodedwClicked)
        workmodedialog._workmodeui.pushButton_dw_work_cancel.clicked.connect(workmodedialog.close)
        self.signal_write_msg.connect(write_msg_heart)
        self.signal_operation_msg.connect(write_msg_operation)
        self.signal_query_msg.connect(write_msg_query)
        self.highlighter1 = Highlighter(self._mainui.plainTextEdit_5_tab1.document())
        self.highlighter2 = Highlighter(self._mainui.plainTextEdit_5_tab2.document())
        self.highlighter3 = Highlighter(self._mainui.plainTextEdit_5_tab3.document())
        self.highlighter21 = Highlighter(self._mainui.plainTextEdit_4_tab1.document())
        self.highlighter22 = Highlighter(self._mainui.plainTextEdit_4_tab2.document())
        self.highlighter23 = Highlighter(self._mainui.plainTextEdit_4_tab3.document())
        self.highlighter31 = Highlighter(self._mainui.plainTextEdit_3_tab1.document())
        self.highlighter32 = Highlighter(self._mainui.plainTextEdit_3_tab2.document())
        self.highlighter33 = Highlighter(self._mainui.plainTextEdit_3_tab3.document())
        
def write_msg_heart(msg , boardip):
    try:
        tabnameindex=tabindex_ip[boardip]+1
    except Exception as ret:
        pass
    else:
        tabname='tab'+str(tabnameindex)
        plainTextEdit_5 = 'plainTextEdit_5_' + tabname
        getattr(win._mainui,plainTextEdit_5).appendPlainText(msg)
        getattr(win._mainui,plainTextEdit_5).moveCursor(QtGui.QTextCursor.End)

def write_msg_operation(msg, boardip):
    try:
        tabnameindex=tabindex_ip[boardip]+1
    except Exception as ret:
        pass
    else:
        tabname='tab'+str(tabnameindex)
        plainTextEdit_4 = 'plainTextEdit_4_' + tabname
        getattr(win._mainui,plainTextEdit_4).appendPlainText(msg)
        getattr(win._mainui,plainTextEdit_4).moveCursor(QtGui.QTextCursor.End)

def write_msg_query(msg, boardip):
    try:
        tabnameindex=tabindex_ip[boardip]+1
    except Exception as ret:
        pass
    else:
        tabname='tab'+str(tabnameindex)
        plainTextEdit_3 = 'plainTextEdit_3_' + tabname
        getattr(win._mainui,plainTextEdit_3).appendPlainText(msg)
        getattr(win._mainui,plainTextEdit_3).moveCursor(QtGui.QTextCursor.End)


#定义连接按钮clicked槽函数
def linkClicked_TCP(boardip, pcport):
    win.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 取消主动断开连接四次握手后的TIME_WAIT状态
    win.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 设定套接字为非阻塞式
    win.tcp_socket.setblocking(False)
    try:
        win.tcp_socket.bind(('', int(pcport)))
        boardip_winsocket[boardip]=win.tcp_socket
    except Exception as ret:
        msg = '请检查端口号\n'
        win.signal_write_msg.emit(msg, boardip)
    else:
        win.tcp_socket.listen()
        win.sever_th = threading.Thread(target=tcp_server_concurrency)
        win.sever_th.start()
        #把进程与tabindex绑定，关闭socket时候使用
        board_severthtcp[boardip]=win.sever_th
        msg = 'TCP服务端正在监听端口:%s\n' % str(pcport)
        win.signal_write_msg.emit(msg, boardip)

def tcp_server_concurrency():
        while True:
            bufferstr=''
            try:
                client_socket, client_address = win.tcp_socket.accept()
                boardip=client_address[0]
            except Exception as ret:
                pass
            else:
                client_socket.setblocking(False)
                tabindex_socket[win._mainui.tabWidget.currentIndex()]=client_socket
                boardip_tcpsocket[client_address[0]]=client_socket
                tcpsocket_addr[client_socket]=client_address
                win.client_socket_list.append((client_socket, client_address))
                msg = 'TCP服务端已连接IP:%s端口:%s\n' % client_address
                win.signal_write_msg.emit(msg, boardip)
                #linkdialog.hide(), lead to crush
            for client, address in win.client_socket_list:
                boardip=address[0]
                try:
                    recv_msg = client.recv(4096)
                except Exception as ret:
                    pass
                else:
                    if recv_msg:
                        msg = recv_msg.hex()
                        #print(msg)
                        while bufferstr != '' or msg != '':
                            bufferstr=bufferstr+msg
                            msg=''
                            if bufferstr[0:8] == 'aaaa5555':
                                msglength = bufferstr[14]+bufferstr[15]+bufferstr[12]+bufferstr[13]
                                msglength = int(msglength,16)
                                if msglength*2 <= len(bufferstr):
                                    msg_analyze = bufferstr[0:msglength*2]
                                    analyze(msg_analyze, boardip)
                                    bufferstr=bufferstr[msglength*2:]
                                else:
                                    pass
                    else:
                        client.close()
                        win.client_socket_list.remove((client, address))

def linkClicked_UDP(pcip, pcport,boardip):
    win.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        win.udp_socket.bind((pcip, int(pcport)))
        boardip_winudpsocket[boardip]=win.udp_socket
        tabindex_socket[win._mainui.tabWidget.currentIndex()]=win.udp_socket
    except Exception as ret:
        msg = '请检查端口号\n'
        win.signal_write_msg.emit(msg, boardip)
    else:
        win.sever_thudp = threading.Thread(target=udp_server_concurrency, args=(boardip,))
        win.sever_thudp.start()
        board_severthudp[boardip]=win.sever_thudp
        msg = 'UDP服务端正在监听端口:%s\n' % str(pcport)
        win.signal_write_msg.emit(msg, boardip)

def udp_server_concurrency(boardip):
    while True:
        try:
            udpsocket=boardip_winudpsocket[boardip]
            recv_msg, recv_addr = udpsocket.recvfrom(1024)
            boardip=recv_addr[0]
        except Exception as ret:
            pass
        else:
            if recv_msg:
                msg = recv_msg.hex()
                if msg[0:8] == 'aaaa5555':
                    msglength = msg[14]+msg[15]+msg[12]+msg[13]
                    msglength = int(msglength,16)
                    msg_analyze = msg[0:msglength*2]
                    analyze(msg_analyze, boardip)


def data_send(datastr,client_socket,boardip,boardport):
    global socket_flag
    if socket_flag == 'UDP':
        try:
            send_msg = bytes.fromhex(datastr)
            client_socket.sendto(send_msg,(boardip,int(boardport)))
        except Exception as ret:
            pass
    elif socket_flag == 'TCP':
        try:
            send_msg = bytes.fromhex(datastr)
            client_socket.send(send_msg)
        except Exception as ret:
            pass


def linkClicked():
    global socket_flag
    global main_flag
    main_flag = linkdialog._linkui.comboBox_main.currentText()
    boardip=linkdialog._linkui.lineEdit_boardip.text()
    boardport=linkdialog._linkui.lineEdit_port.text()
    pcip=linkdialog._linkui.lineEdit_pcip.text()
    port=linkdialog._linkui.lineEdit_port.text()
    win._mainui.tabWidget.setTabText(win._mainui.tabWidget.currentIndex(),boardip+' '+port)
    tabindex_ip[boardip]=win._mainui.tabWidget.currentIndex()
    tabindex_boardip[win._mainui.tabWidget.currentIndex()]=boardip
    tabindex_boardport[win._mainui.tabWidget.currentIndex()]=boardport
    if linkdialog._linkui.comboBox.currentText() == 'TCP':
        socket_flag='TCP'
        linkClicked_TCP(boardip,port)
    elif linkdialog._linkui.comboBox.currentText() == 'UDP':
        socket_flag='UDP'
        linkClicked_UDP(pcip, port, boardip)


def dislinkClicked():
    if linkdialog._linkui.comboBox.currentText() == 'TCP':
        boardip=linkdialog._linkui.lineEdit_boardip.text()
        try:
            client_socket=boardip_tcpsocket[boardip]
            win_socket=boardip_winsocket[boardip]
        except Exception as ret:
            pass
        try:
            dislinkClicked_TCP(client_socket, win_socket,boardip)
        except Exception as ret:
            pass
    elif linkdialog._linkui.comboBox.currentText() == 'UDP':
        boardip=linkdialog._linkui.lineEdit_boardip.text()
        try:
            win_socket=boardip_winudpsocket[boardip]
        except Exception as ret:
            pass
        dislinkClicked_UDP(win_socket, boardip)


def dislinkClicked_UDP(winsocket, boardip):
    try:
        winsocket.close()
        boardip_winudpsocket.pop(boardip)
        msg = '已断开网络\n'
        win.signal_write_msg.emit(msg,boardip)
    except Exception as ret:
        pass
    try:
        sever_th=board_severthudp[boardip]
        stopThreading.stop_thread(sever_th)
        board_severthudp.pop(boardip)
    except Exception:
        pass
        

def dislinkClicked_TCP(tcpsocket, winsocket, boardip):
    try:
        winsocket.close()
        boardip_winsocket.pop(boardip)
        tcpsocket.shutdown(2)
        tcpsocket.close()
        boardip_tcpsocket.pop(boardip)
        client_address=tcpsocket_addr[tcpsocket]
        win.client_socket_list.remove((tcpsocket, client_address))
        tcpsocket_addr.pop(tcpsocket)
        msg = '已断开网络\n'
        win.signal_write_msg.emit(msg, boardip)
        tabindex_ip.pop(boardip)
    except Exception as ret:
        pass
    try:
        sever_th=board_severthtcp[boardip]
        stopThreading.stop_thread(sever_th)
        board_severthtcp.pop(boardip)
    except Exception as ret:
        pass

def rebootClicked():
    msgtype='0bf0'
    if main_flag == '非主控模式':
        msgframe ='ffffffff3132333435363738393031323334353637383900'
    elif main_flag =='主控模式':
        msgframe='ffffffff'
    boardport=tabindex_boardport[win._mainui.tabWidget.currentIndex()]
    boardip=tabindex_boardip[win._mainui.tabWidget.currentIndex()]
    client_socket=tabindex_socket[win._mainui.tabWidget.currentIndex()]
    if rebootdialog._rebootui.combox.currentText() == '重启后小区空闲':
        rebootstr='01000000'
    elif rebootdialog._rebootui.combox.currentText() == '重启后小区自激活':
        rebootstr='00000000'
    msglen=(len(('aaaa5555'+msgtype+msgframe+rebootstr))+4)//2
    msglen=msglenfunc(msglen)
    data='aaaa5555'+msgtype+msglen+msgframe+rebootstr
    data_send(data,client_socket, boardip, boardport)

def cellcfgClicked():
    msgtype = '03f0'
    if main_flag == '非主控模式':
        msgframe = 'ffffffff3132333435363738393031323334353637383900'
    elif main_flag == '主控模式':
        msgframe = 'ffffffff'
    boardport = tabindex_boardport[win._mainui.tabWidget.currentIndex()]
    boardip = tabindex_boardip[win._mainui.tabWidget.currentIndex()]
    client_socket = tabindex_socket[win._mainui.tabWidget.currentIndex()]
    ulearfcnstr = cellcfgdialog._cellcfgui.tableWidget.item(0, 1).text()
    dlearfcnstr = cellcfgdialog._cellcfgui.tableWidget.item(1, 1).text()
    ulearfcn=decstrtohexstr(ulearfcnstr,'u32')
    dlearfcn=decstrtohexstr(dlearfcnstr,'u32')
    plmnstr = cellcfgdialog._cellcfgui.tableWidget.item(2, 1).text()
    plmn = strtohexasc(plmnstr)+'0000'
    bandwithstr = cellcfgdialog._cellcfgui.combox.currentText()
    bandwith = str((int(bandwithstr))*5)
    bandwith = decstrtohexstr(bandwith,'u8')
    bandstr = cellcfgdialog._cellcfgui.tableWidget.item(4, 1).text()
    band = decstrtohexstr(bandstr,'u32')
    pcistr = cellcfgdialog._cellcfgui.tableWidget.item(5, 1).text()
    pci = decstrtohexstr(pcistr,'u16')
    tacstr = cellcfgdialog._cellcfgui.tableWidget.item(6, 1).text()
    tac = decstrtohexstr(tacstr,'u16')
    cellidstr = cellcfgdialog._cellcfgui.tableWidget.item(7, 1).text()
    cellid = decstrtohexstr(cellidstr,'u32')
    uepmaxstr = cellcfgdialog._cellcfgui.tableWidget.item(8, 1).text()
    uepmax = decstrtohexstr(uepmaxstr,'u16')
    enbpmaxstr = cellcfgdialog._cellcfgui.tableWidget.item(9, 1).text()
    enbpmax = decstrtohexstr(enbpmaxstr, 'u16')
    cellcfginfo = ulearfcn+dlearfcn+plmn+bandwith+band+pci+tac+cellid+uepmax+enbpmax
    msglen = (len('aaaa5555' + msgtype + msgframe + cellcfginfo)) // 2
    msglen = msglenfunc(msglen)
    data = 'aaaa5555' + msgtype + msglen + msgframe + cellcfginfo
    data_send(data, client_socket, boardip, boardport)

def workmodecfgClicked():
    msgtype = '06f0'
    if main_flag == '非主控模式':
        msgframe = 'ffffffff3132333435363738393031323334353637383900'
    elif main_flag == '主控模式':
        msgframe = 'ffffffff'
    boardport = tabindex_boardport[win._mainui.tabWidget.currentIndex()]
    boardip = tabindex_boardip[win._mainui.tabWidget.currentIndex()]
    client_socket = tabindex_socket[win._mainui.tabWidget.currentIndex()]
    u8WorkMode = workmodedialog._workmodeui.combox_wlworkmode.currentText()
    u8RedirectSubMode = workmodedialog._workmodeui.combox_redirectsub.currentText()
    u16CapturePeriod = workmodedialog._workmodeui.tableWidget_wl.item(2, 1).text()
    u8ControlSubMode = workmodedialog._workmodeui.combox_controlsub.currentText()
    workmodedic = {'持续侦码模式':'0','周期侦码模式':'1','管控模式':'3','重定向模式':'4'}
    workmode= decstrtohexstr(workmodedic[u8WorkMode],'u8')
    redirectsubdic = {'名单中的用户执行重定向；名单外的全部踢回公网':'0','名单中的用户踢回公网；名单外的全部重定向':'1',
                      '名单中的用户执行重定向；名单外的全部吸附在本站':'2','名单中的用户吸附在本站;名单外的全部重定向':'3',
                        '所有目标重定向':'4'}
    redirectsub = decstrtohexstr(redirectsubdic[u8RedirectSubMode],'u8')
    captureperiod = decstrtohexstr(u16CapturePeriod,'u16')
    controlsubdic = {'黑名单子模式':'0','白名单子模式':'1','全黑子模式':'2'}
    controlsub = decstrtohexstr(controlsubdic[u8ControlSubMode],'u8')
    workmodeinfo = workmode+redirectsub+captureperiod+controlsub
    msglen = (len('aaaa5555' + msgtype + msgframe + workmodeinfo)) // 2
    msglen = msglenfunc(msglen)
    data = 'aaaa5555' + msgtype + msglen + msgframe + workmodeinfo
    data_send(data, client_socket, boardip, boardport)

def workmodedwClicked():
    pass


def cellcfgquery():
    msgtype='27f0'
    if main_flag == '非主控模式':
        msgframe ='ffffffff3132333435363738393031323334353637383900'
    elif main_flag =='主控模式':
        msgframe='ffffffff'
    boardport=tabindex_boardport[win._mainui.tabWidget.currentIndex()]
    boardip=tabindex_boardip[win._mainui.tabWidget.currentIndex()]
    client_socket=tabindex_socket[win._mainui.tabWidget.currentIndex()]
    msglen=(len(('aaaa5555'+msgtype+msgframe))+4)//2
    msglen=msglenfunc(msglen)
    data='aaaa5555'+msgtype+msglen+msgframe
    data_send(data,client_socket, boardip, boardport)
    
def cellstatequery():
    msgtype='2ff0'
    if main_flag == '非主控模式':
        msgframe ='ffffffff3132333435363738393031323334353637383900'
    elif main_flag =='主控模式':
        msgframe='ffffffff'
    boardport=tabindex_boardport[win._mainui.tabWidget.currentIndex()]
    boardip=tabindex_boardip[win._mainui.tabWidget.currentIndex()]
    client_socket=tabindex_socket[win._mainui.tabWidget.currentIndex()]
    msglen=(len(('aaaa5555'+msgtype+msgframe))+4)//2
    msglen=msglenfunc(msglen)
    data='aaaa5555'+msgtype+msglen+msgframe
    data_send(data,client_socket, boardip, boardport)

def pwrquery():
    msgtype='31f0'
    if main_flag == '非主控模式':
        msgframe ='ffffffff3132333435363738393031323334353637383900'
    elif main_flag =='主控模式':
        msgframe='ffffffff'
    boardport=tabindex_boardport[win._mainui.tabWidget.currentIndex()]
    boardip=tabindex_boardip[win._mainui.tabWidget.currentIndex()]
    client_socket=tabindex_socket[win._mainui.tabWidget.currentIndex()]
    msglen=(len(('aaaa5555'+msgtype+msgframe))+4)//2
    msglen=msglenfunc(msglen)
    data='aaaa5555'+msgtype+msglen+msgframe
    data_send(data,client_socket, boardip, boardport)
    
def workmodequery():
    msgtype='3df0'
    if main_flag == '非主控模式':
        msgframe ='ffffffff3132333435363738393031323334353637383900'
    elif main_flag =='主控模式':
        msgframe='ffffffff'
    boardport=tabindex_boardport[win._mainui.tabWidget.currentIndex()]
    boardip=tabindex_boardip[win._mainui.tabWidget.currentIndex()]
    client_socket=tabindex_socket[win._mainui.tabWidget.currentIndex()]
    msglen=(len(('aaaa5555'+msgtype+msgframe))+4)//2
    msglen=msglenfunc(msglen)
    data='aaaa5555'+msgtype+msglen+msgframe
    data_send(data,client_socket, boardip, boardport)


def tabadd():
    tabNumber=win._mainui.tabWidget.count()+1
    tabName = 'tab' + str(tabNumber)
    gridLayout_6 = 'gridLayout_6_' + tabName
    groupBox_3 = 'groupBox_3_' + tabName
    gridLayout_3 = 'gridLayout_3_' + tabName
    plainTextEdit_3 = 'plainTextEdit_3_' + tabName
    groupBox_4 = 'groupBox_4_' + tabName
    gridLayout_4 = 'gridLayout_4_' + tabName
    plainTextEdit_4 = 'plainTextEdit_4_' + tabName
    groupBox_5 = 'groupBox_5_' + tabName
    gridLayout_5 = 'gridLayout_5_' + tabName
    plainTextEdit_5 = 'plainTextEdit_5_' + tabName
    getattr(win._mainui,tabName).setObjectName(tabName)
    getattr(win._mainui,gridLayout_6).setObjectName(gridLayout_6)
    getattr(win._mainui,groupBox_3).setObjectName(groupBox_3)
    getattr(win._mainui,gridLayout_3).setObjectName(gridLayout_3)
    getattr(win._mainui,plainTextEdit_3).setObjectName(plainTextEdit_3)
    getattr(win._mainui,gridLayout_3).addWidget(getattr(win._mainui,plainTextEdit_3),0,0,1,1)
    getattr(win._mainui,gridLayout_6).addWidget(getattr(win._mainui,groupBox_3),0,0,1,4)
    getattr(win._mainui,groupBox_5).setObjectName(groupBox_5)
    getattr(win._mainui,gridLayout_5).setObjectName(gridLayout_5)
    getattr(win._mainui,plainTextEdit_5).setObjectName(plainTextEdit_5)
    getattr(win._mainui,gridLayout_5).addWidget(getattr(win._mainui,plainTextEdit_5),0,0,1,1)
    getattr(win._mainui,gridLayout_6).addWidget(getattr(win._mainui,groupBox_5),1,2,1,2)
    getattr(win._mainui,groupBox_4).setObjectName(groupBox_4)
    getattr(win._mainui,gridLayout_4).setObjectName(gridLayout_4)
    getattr(win._mainui,plainTextEdit_4).setObjectName(plainTextEdit_4)
    getattr(win._mainui,gridLayout_4).addWidget(getattr(win._mainui,plainTextEdit_4),0,0,1,1)
    getattr(win._mainui,gridLayout_6).addWidget(getattr(win._mainui,groupBox_4),1,0,1,2)
    win._mainui.tabWidget.addTab(getattr(win._mainui,tabName),"")
    win._mainui.tabWidget.addTab(getattr(win._mainui,tabName), "新建连接")
    getattr(win._mainui,groupBox_3).setTitle("查询信息")
    getattr(win._mainui,groupBox_5).setTitle("心跳")
    getattr(win._mainui,groupBox_4).setTitle("操作日志")

class logic_linkdialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self._linkui=Ui_Dialog()
        self._linkui.setupUi(self)

class logic_rebootdialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self._rebootui=Ui_Dialog_reboot()
        self._rebootui.setupUi(self)

class logic_cellcfgdialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self._cellcfgui=Ui_Dialog_cellcfg()
        self._cellcfgui.setupUi(self)
        
class logic_workmodedialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self._workmodeui=Ui_Dialog_workmode()
        self._workmodeui.setupUi(self)

#linkdialog=logic_linkdialog()  放到主函数入口中实例化才可以，
#数据分析部分
def analyze(data, ip):
    global imsinumber
    board_ip=ip
    msglength = data[14]+data[15]+data[12]+data[13]
    msglength = int(msglength,16)
    msgtype=data[10]+data[11]+data[8]+data[9]
    msgvalue=data[64:msglength*2]
    localtime =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if msgtype == '0001':
        gnbId=getU32int(msgvalue)
        pos=8
        msgvalue=msgvalue[pos:]
        cuInfoPres=getU8int(msgvalue)
        pos=2
        msgvalue=msgvalue[pos:]
        duInfoListPres=getU8int(msgvalue)
        pos=6
        showmsg='Receive '+localtime+' HeartBeat'+' GnbId：'+str(gnbId)
        win.signal_write_msg.emit(showmsg, board_ip)
        
        if cuInfoPres == 1:
            msgvalue=msgvalue[pos:]
            cuStatus=getU8int(msgvalue)
            pos=8
            showmsg='CuStatus：'+str(cuStatus)
            win.signal_write_msg.emit(showmsg, board_ip)
        
        if duInfoListPres == 1:
            msgvalue=msgvalue[pos:]
            duNum=getU8int(msgvalue)
            pos=8
            showmsg='DuNum：'+str(duNum)
            win.signal_write_msg.emit(showmsg, board_ip)
            duNum_i = 1
            print(duNum_i)
            while duNum_i <=duNum:
                showmsg=' No. '+str(duNum_i)+' DU: '
                win.signal_write_msg.emit(showmsg, board_ip)
                msgvalue = msgvalue[pos:]
                duSn = msgvalue[0:40]
                duSn = strhexASCtostr(duSn) 
                pos = 40
                msgvalue=msgvalue[pos:]
                duStatus=getU8int(msgvalue)
                pos=6
                showmsg='  DuSn：'+str(duSn)+' DuStatus: '+str(duStatus)
                win.signal_write_msg.emit(showmsg, board_ip)
                msgvalue=msgvalue[pos:]
                cellNum=getU8int(msgvalue)
                pos=2
                showmsg=' CellNum：'+str(cellNum)
                win.signal_write_msg.emit(showmsg, board_ip)
                cellNum_i =1
                while cellNum_i<= cellNum:
                    showmsg='  No. '+str(cellNum_i)+' Cell: '
                    win.signal_write_msg.emit(showmsg, board_ip)
                    msgvalue=msgvalue[pos:]
                    cellId=getU16int(msgvalue)
                    pos=4
                    msgvalue=msgvalue[pos:]
                    cellStatusind=getU8int(msgvalue)
                    pos=2
                    cellstatuslist=['小区IDLE态', '小区建立中', '小区已激活', '小区重配中', '小区去激活中']
                    cellstatus =cellstatuslist[cellStatusind]
                    msgvalue=msgvalue[pos:]
                    cellIdx=getU8int(msgvalue)
                    pos=2
                    showmsg='  cellId：'+str(cellId)+' 小区状态: '+str(cellstatus)+' cellIdx '+str(cellIdx)
                    win.signal_write_msg.emit(showmsg, board_ip)
                    cellNum_i +=1
                duNum_i  +=1
                
    elif msgtype == 'f005':
        UeIdType=getU32int(msgvalue)
        pos=8
        msgvalue=msgvalue[pos:]
        imsi=msgvalue[0:30]
        imsi=strhexASCtostr(imsi)
        pos=34
        msgvalue=msgvalue[pos:]
        imei=msgvalue[0:30]
        imei=strhexASCtostr(imei)
        pos=34
        msgvalue=msgvalue[pos:]
        rssi=getU8int(msgvalue)
        strList=[localtime, imsi, str(rssi), board_ip]
        try:
            imsilistframe.imsilistshow(strList,imsinumber)
            imsinumber+=1
        except Exception as ret:
            pass
    elif msgtype in ['f00c','f004','f007']:
        cfgresult=getU32int(msgvalue)
        cfgresultstr=''
        if cfgresult== 0:
            cfgresultstr='配置成功'
        elif cfgresult != 0:
            cfgresultstr='配置失败'
        showmsg='Receive:'+msgtype+cfgresultstr
        win.signal_operation_msg.emit(showmsg, board_ip)
    elif msgtype == 'f019':
        cellstateind = getU32int(msgvalue)
        cellstatelist = ['空口同步成功','空口同步失败','GPS同步成功','GPS同步失败','扫频成功','扫频失败','小区激活成功'
            ,'小区激活失败','小区去激活','空口同步中','GPS同步中','扫频中','小区激活中','小区去激活中','无效状态']
        cellstate = 'Receive:'+cellstatelist[cellstateind]
        win.signal_query_msg.emit(cellstate, board_ip)
    elif msgtype == 'f030':
        cellstateind = getU32int(msgvalue)
        cellstatelist = ['小区空闲','扫频中','小区激活中','小区激活成功','小区去激活中','同步中']
        cellstate = 'Receive:'+cellstatelist[cellstateind] + '\n'
        win.signal_query_msg.emit(cellstate, board_ip)
    elif msgtype == 'f028':
        ul_earfcn = getU32int(msgvalue)
        pos = 8
        msgvalue = msgvalue[pos:]
        dl_earfcn = getU32int(msgvalue)
        pos = 8
        msgvalue = msgvalue[pos:]
        plmn = msgvalue[0:10]
        plmn = strhexASCtostr(plmn)
        pos = 14
        msgvalue = msgvalue[pos:]
        bandwith = getU8int(msgvalue)
        pos = 2
        msgvalue = msgvalue[pos:]
        band = getU32int(msgvalue)
        pos = 8
        msgvalue = msgvalue[pos:]
        pci = getU16int(msgvalue)
        pos = 4
        msgvalue = msgvalue[pos:]
        tac = getU16int(msgvalue)
        pos = 4
        msgvalue = msgvalue[pos:]
        cellid = getU32int(msgvalue)
        pos = 8
        msgvalue = msgvalue[pos:]
        uepmax = getU16int(msgvalue)
        pos = 4
        msgvalue = msgvalue[pos:]
        enbpmax = getU16int(msgvalue)
        cellcfg = 'Receive: 小区参数查询\n' + '上行频点: ' + str(ul_earfcn) + '\n' \
                    + '下行频点: ' + str(dl_earfcn) + '\n' \
                    + 'PLMN: ' + plmn + '\n' \
                    + '小区带宽: ' + str(bandwith) + '\n' \
                    + '频段: ' + str(band) + '\n' \
                    + 'PCI: ' + str(pci) + '\n' \
                    + 'TAC: ' + str(tac) + '\n' \
                    + 'CellId: ' + str(cellid) + '\n' \
                    + 'UePmax: ' + str(uepmax) + '\n' \
                    + 'eNBPmax: ' + str(enbpmax) + '\n'
        win.signal_query_msg.emit(cellcfg, board_ip)
    elif msgtype == 'f032':
        u8RxGainValueFromReg = getU8int(msgvalue)
        pos = 2
        msgvalue = msgvalue[pos:]
        u8RxGainValueFromMib = getU8int(msgvalue)
        pos = 2
        msgvalue = msgvalue[pos:]
        u8PowerDereaseValueFromReg = getU8int(msgvalue)
        pos = 2
        msgvalue = msgvalue[pos:]
        u8PowerDereaseValueFromMib = getU8int(msgvalue)
        pwr = 'Receive: 小区衰减及增益查询\n' + '寄存器中接收增益: ' + str(u8RxGainValueFromReg) + '\n' \
                    + 'Mib中接收增益: ' + str(u8RxGainValueFromMib) + '\n' \
                    + '寄存器中衰减: ' + str(u8PowerDereaseValueFromReg) + '\n' \
                    + 'Mib中衰减: ' + str(u8PowerDereaseValueFromMib) + '\n'
        win.signal_query_msg.emit(pwr, board_ip)
    elif msgtype == 'f03e':
        valuelength = len(msgvalue)
        if valuelength == 16:
            u8WorkMode = getU8int(msgvalue)
            workmodelist = ['持续侦码模式','周期侦码模式','保留','管控模式','重定向模式']
            workmode = workmodelist[u8WorkMode]
            pos = 2
            msgvalue = msgvalue[pos:]
            u8RedirectSubMode = getU8int(msgvalue)
            directsublist = ['名单中的用户执行重定向；名单外的全部踢回公网', '名单中的用户踢回公网；名单外的全部重定向',  \
                             '名单中的用户执行重定向；名单外的全部吸附在本站', '名单中的用户吸附在本站;名单外的全部重定向',  \
                             '所有目标重定向']
            directsub = directsublist[u8RedirectSubMode]
            pos = 2
            msgvalue = msgvalue[pos:]
            u16CapturePeriod = getU16int(msgvalue)
            pos = 4
            msgvalue = msgvalue[pos:]
            u8ControlSubMode = getU8int(msgvalue)
            controlsublist = ['黑名单子模式','白名单子模式','全黑子模式']
            controlsub = controlsublist[u8ControlSubMode]
            wkmode = 'Receive: 工作模式查询\n' + '工作模式: ' + workmode + '\n' \
                    + '重定向子模式(仅在重定向模式下有效): ' + directsub + '\n' \
                    + '周期模式采集周期(仅在周期模式下有效): ' + str(u16CapturePeriod) + '\n' \
                    + '管控子模式(仅在管控模式下有效): ' +controlsub  + '\n'
            win.signal_query_msg.emit(wkmode, board_ip)







def getU8int(data):
    data_u8=data[0]+data[1]
    data_u8_int=int(data_u8, 16)
    return data_u8_int

def getU16int(data):
    data_u16=data[2]+data[3]+data[0]+data[1]
    data_u16_int=int(data_u16, 16)
    return data_u16_int

def getU32int(data):
    data_u32=data[6]+data[7]+data[4]+data[5]+data[2]+data[3]+data[0]+data[1]
    data_u32_int=int(data_u32, 16)
    return data_u32_int

def strhexASCtostr(data):
    count=len(data)//2
    i=0
    hexasctostr=''
    for j in range(count):
        hexasctostr += chr(int(data[i:i+2],16))
        i+=2
    return hexasctostr

def msglenfunc(lenintdec):
    lenhexstr=hex(lenintdec)[2:]
    addzero=4-len(lenhexstr)
    msglenraw=addzero*'0'+lenhexstr
    msglen=msglenraw[2:]+msglenraw[0:2]
    return msglen
    
def decstrtohexstr(data,hextype):
    data=int(data)
    datahex=hex(data)[2:]
    if hextype == 'u32':
        addzero=8-len(datahex)
        datahexraw=addzero*'0'+datahex
        datasend=datahexraw[6:8]+datahexraw[4:6]+datahexraw[2:4]+datahexraw[0:2]
        return datasend
    elif hextype == 'u16':
        addzero=4-len(datahex)
        datahexraw=addzero*'0'+datahex
        datasend=datahexraw[2:]+datahexraw[0:2]
        return datasend
    elif hextype == 'u8':
        addzero=2-len(datahex)
        datahexraw=addzero*'0'+datahex
        datasend=datahexraw[0:2]
        return datasend

def strtohexasc(decstr):
    hexascstr=''
    for i in decstr:
        i=hex(ord(i))[2:]
        hexascstr+=i
    return hexascstr

#定义一个文本格式化类，用于格式化文本，其中highlightBlock好像会自动调用
class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent):
        super(Highlighter, self).__init__(parent)
        self.recvFormat = QtGui.QTextCharFormat()
        self.recvFormat.setForeground(QtCore.Qt.red)

        
    def highlightBlock(self, text):
        # uncomment this line for Python2
        # text = unicode(text)
        if text.startswith('Receive'):
            self.setFormat(0, len(text), self.recvFormat)
        elif text.startswith('Send'):
            self.setFormat(0, len(text), self.errorFormat)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    linkdialog=logic_linkdialog()
    rebootdialog=logic_rebootdialog()
    cellcfgdialog=logic_cellcfgdialog()
    workmodedialog=logic_workmodedialog()
    imsilistframe=ImsiList()
    win = logic_main()
    win.show()
    sys.exit(app.exec_())
