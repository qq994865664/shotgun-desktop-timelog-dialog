# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sg_desktop_timelog_login.ui'
#
# Created: Tue Dec  3 16:01:28 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TimelogLogin(object):
    def setupUi(self, TimelogLogin):
        TimelogLogin.setObjectName("TimelogLogin")
        TimelogLogin.resize(456, 279)
        self.layoutWidget = QtWidgets.QWidget(TimelogLogin)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 80, 261, 105))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxProjectName = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxProjectName.setObjectName("comboBoxProjectName")
        self.gridLayout.addWidget(self.comboBoxProjectName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditUserName = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.gridLayout.addWidget(self.lineEditUserName, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditPassWd = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditPassWd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassWd.setObjectName("lineEditPassWd")
        self.gridLayout.addWidget(self.lineEditPassWd, 2, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLogin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonCancel = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)

        self.retranslateUi(TimelogLogin)
        QtCore.QObject.connect(self.pushButtonLogin, QtCore.SIGNAL("clicked()"), TimelogLogin.login)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL("clicked()"), TimelogLogin.reject)
        QtCore.QMetaObject.connectSlotsByName(TimelogLogin)

    def retranslateUi(self, TimelogLogin):
        TimelogLogin.setWindowTitle(QtWidgets.QApplication.translate("TimelogLogin", "TimeLog Login", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("TimelogLogin", "项目选择：", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("TimelogLogin", "用户名：", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("TimelogLogin", "密码：", None, -1))
        self.pushButtonLogin.setText(QtWidgets.QApplication.translate("TimelogLogin", "登录", None, -1))
        self.pushButtonCancel.setText(QtWidgets.QApplication.translate("TimelogLogin", "取消", None, -1))

