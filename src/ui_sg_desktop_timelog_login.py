# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sg_desktop_timelog_login.ui'
#
# Created: Mon Dec  2 11:45:31 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_TimelogLogin(object):
    def setupUi(self, TimelogLogin):
        TimelogLogin.setObjectName("TimelogLogin")
        TimelogLogin.resize(462, 304)
        self.widget = QtWidgets.QWidget(TimelogLogin)
        self.widget.setGeometry(QtCore.QRect(80, 50, 301, 181))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxProjectName = QtWidgets.QComboBox(self.widget)
        self.comboBoxProjectName.setObjectName("comboBoxProjectName")
        self.gridLayout.addWidget(self.comboBoxProjectName, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditUserName = QtWidgets.QLineEdit(self.widget)
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.gridLayout.addWidget(self.lineEditUserName, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditPassWd = QtWidgets.QLineEdit(self.widget)
        self.lineEditPassWd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassWd.setObjectName("lineEditPassWd")
        self.gridLayout.addWidget(self.lineEditPassWd, 2, 1, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(TimelogLogin)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), TimelogLogin.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), TimelogLogin.reject)
        QtCore.QMetaObject.connectSlotsByName(TimelogLogin)

    def retranslateUi(self, TimelogLogin):
        TimelogLogin.setWindowTitle(QtWidgets.QApplication.translate("TimelogLogin", "TimeLog Login", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("TimelogLogin", "项目选择：", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("TimelogLogin", "用户名：", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("TimelogLogin", "密码：", None, -1))
