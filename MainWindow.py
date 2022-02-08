# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime


class Ui_Main(QtWidgets.QMainWindow):
    def openresultinfo(self):
        from search.resultinfo import Ui_resultinfoWindow
        self.resultinfoWindow = Ui_resultinfoWindow()
        self.resultinfoWindow.setupUi(self.resultinfoWindow)
        self.resultinfoWindow.setFixedSize(self.resultinfoWindow.width(), self.resultinfoWindow.height())
        self.resultinfoWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.resultinfoWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resultinfoWindow.show()
    def openstudentinfo(self):
        from search.studentinfo import Ui_studentinfoWindow
        self.studentinfoWindow = Ui_studentinfoWindow()
        self.studentinfoWindow.setupUi(self.studentinfoWindow)
        self.studentinfoWindow.setFixedSize(self.studentinfoWindow.width(), self.studentinfoWindow.height())
        self.studentinfoWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.studentinfoWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.studentinfoWindow.show()
    def openstudent(self):
        # 基本信息管理
        from baseinfo.student import Ui_studentWindow
        self.studentWindow = Ui_studentWindow()
        self.studentWindow.setupUi(self.studentWindow)
        self.studentWindow.setFixedSize(self.studentWindow.width(), self.studentWindow.height())
        self.studentWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.studentWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.studentWindow.show()
    def openresult(self):
        from baseinfo.result import Ui_resultWindow
        self.resultWindow = Ui_resultWindow()
        self.resultWindow.setupUi(self.resultWindow)
        self.resultWindow.setFixedSize(self.resultWindow.width(), self.resultWindow.height())
        self.resultWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.resultWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.resultWindow.show()
    def openuser(self):
        from user import Ui_UserWindow
        self.userWindow = Ui_UserWindow()
        self.userWindow.setupUi(self.userWindow)
        self.userWindow.setFixedSize(self.userWindow.width(), self.userWindow.height())
        self.userWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.userWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.userWindow.show()
    def opensubject(self):
        from settings.subject import Ui_subject
        self.subjectWindow = Ui_subject()
        self.subjectWindow.setupUi(self.subjectWindow)
        self.subjectWindow.setFixedSize(self.subjectWindow.width(), self.subjectWindow.height())
        # 阻塞父窗口
        self.subjectWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.subjectWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.subjectWindow.show()
    def opengrade(self):
        from settings.grade import Ui_grade
        self.gradeWindow = Ui_grade()
        self.gradeWindow.setupUi(self.gradeWindow)
        self.gradeWindow.setFixedSize(self.gradeWindow.width(), self.gradeWindow.height())
        # 阻塞父窗口
        self.gradeWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.gradeWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gradeWindow.show()
    def openexamkinds(self):
        from settings.examkinds import Ui_examkinds
        self.examkindsWindow = Ui_examkinds()
        self.examkindsWindow.setupUi(self.examkindsWindow)
        self.examkindsWindow.setFixedSize(self.examkindsWindow.width(), self.examkindsWindow.height())
        # 阻塞父窗口
        self.examkindsWindow.setWindowFlags(
            QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.examkindsWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.examkindsWindow.show()
    def openclasses(self):
        from settings.classes import Ui_classes
        self.classWindow = Ui_classes()
        self.classWindow.setupUi(self.classWindow)
        self.classWindow.setFixedSize(self.classWindow.width(), self.classWindow.height())
        # 阻塞父窗口
        self.classWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.classWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        self.classWindow.show()
    def __init__(self, user):
        super().__init__()
        self.user = user
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 583)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/images/appstu.ICO"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-image: url(:/jpg/images/main.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 792, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_9 = QtWidgets.QAction(MainWindow)
        self.action_9.setObjectName("action_9")
        self.action_10 = QtWidgets.QAction(MainWindow)
        self.action_10.setObjectName("action_10")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_3.addAction(self.action_7)
        self.menu_3.addAction(self.action_8)
        self.menu_4.addAction(self.action_9)
        self.menu_4.addAction(self.action_10)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        label = QtWidgets.QLabel()
        label.setText(f"当前用户：{self.user}")
        self.statusbar.addWidget(label)
        label2 = QtWidgets.QLabel()
        nowtime = datetime.datetime.now()
        label2.setText(f"登陆时间：{nowtime.strftime('%Y-%m-%d %H:%M:%S')}")
        self.statusbar.addWidget(label2)
        label3 = QtWidgets.QLabel()
        label3.setText("COMPOSED by VLSMB")
        self.statusbar.addWidget(label3)

        self.retranslateUi(MainWindow)
        self.action.triggered.connect(self.opengrade)
        self.action_2.triggered.connect(self.openclasses)
        self.action_3.triggered.connect(self.opensubject)
        self.action_4.triggered.connect(self.openexamkinds)
        self.action_5.triggered.connect(self.openstudent)
        self.action_6.triggered.connect(self.openresult)
        self.action_7.triggered.connect(self.openstudentinfo)
        self.action_8.triggered.connect(self.openresultinfo)
        self.action_9.triggered.connect(self.openuser)
        self.action_10.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "学生成绩管理系统"))
        self.menu.setTitle(_translate("MainWindow", "基础设置"))
        self.menu_2.setTitle(_translate("MainWindow", "基本信息管理"))
        self.menu_3.setTitle(_translate("MainWindow", "系统查询"))
        self.menu_4.setTitle(_translate("MainWindow", "系统管理"))
        self.action.setText(_translate("MainWindow", "年级信息设置"))
        self.action_2.setText(_translate("MainWindow", "班级设置"))
        self.action_3.setText(_translate("MainWindow", "考试科目设置"))
        self.action_4.setText(_translate("MainWindow", "考试类别设置"))
        self.action_5.setText(_translate("MainWindow", "学生信息管理"))
        self.action_6.setText(_translate("MainWindow", "成绩管理"))
        self.action_7.setText(_translate("MainWindow", "学生信息查询"))
        self.action_8.setText(_translate("MainWindow", "学生成绩查询"))
        self.action_9.setText(_translate("MainWindow", "用户信息维护"))
        self.action_10.setText(_translate("MainWindow", "退出"))
import rc_rc

if __name__ == "__main__":
    # 调试程序
    import sys
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 适应分辨率
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())  # 禁止窗口拉伸
    UI = Ui_Main("汐奈酱")
    UI.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())