# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sg_desktop_timelog_dialog.ui'
#
# Created: Thu Nov 21 11:44:26 2019
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ShotgunDesktopVersionDialog(object):
    def setupUi(self, ShotgunDesktopVersionDialog):
        ShotgunDesktopVersionDialog.setObjectName("ShotgunDesktopVersionDialog")
        ShotgunDesktopVersionDialog.resize(722, 585)
        self.gridLayout_4 = QtWidgets.QGridLayout(ShotgunDesktopVersionDialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidgetList = QtWidgets.QTabWidget(ShotgunDesktopVersionDialog)
        self.tabWidgetList.setObjectName("tabWidgetList")
        self.tabMyTask = QtWidgets.QWidget()
        self.tabMyTask.setObjectName("tabMyTask")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabMyTask)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutMyTask = QtWidgets.QGridLayout()
        self.gridLayoutMyTask.setObjectName("gridLayoutMyTask")
        self.lineEditMyTaskSearch = QtWidgets.QLineEdit(self.tabMyTask)
        self.lineEditMyTaskSearch.setObjectName("lineEditMyTaskSearch")
        self.gridLayoutMyTask.addWidget(self.lineEditMyTaskSearch, 0, 0, 1, 1)
        self.treeViewMyTask = QtWidgets.QTreeView(self.tabMyTask)
        self.treeViewMyTask.setObjectName("treeViewMyTask")
        self.gridLayoutMyTask.addWidget(self.treeViewMyTask, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayoutMyTask, 0, 0, 1, 1)
        self.tabWidgetList.addTab(self.tabMyTask, "")
        self.tabAsset = QtWidgets.QWidget()
        self.tabAsset.setObjectName("tabAsset")
        self.gridLayout = QtWidgets.QGridLayout(self.tabAsset)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutAsset = QtWidgets.QGridLayout()
        self.gridLayoutAsset.setObjectName("gridLayoutAsset")
        self.lineEditAssetSearch = QtWidgets.QLineEdit(self.tabAsset)
        self.lineEditAssetSearch.setObjectName("lineEditAssetSearch")
        self.gridLayoutAsset.addWidget(self.lineEditAssetSearch, 0, 0, 1, 1)
        self.treeViewAsset = QtWidgets.QTreeView(self.tabAsset)
        self.treeViewAsset.setObjectName("treeViewAsset")
        self.gridLayoutAsset.addWidget(self.treeViewAsset, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayoutAsset, 0, 0, 1, 1)
        self.tabWidgetList.addTab(self.tabAsset, "")
        self.tabShot = QtWidgets.QWidget()
        self.tabShot.setObjectName("tabShot")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabShot)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayoutShot = QtWidgets.QGridLayout()
        self.gridLayoutShot.setObjectName("gridLayoutShot")
        self.treeViewShot = QtWidgets.QTreeView(self.tabShot)
        self.treeViewShot.setObjectName("treeViewShot")
        self.gridLayoutShot.addWidget(self.treeViewShot, 1, 0, 1, 1)
        self.lineEditShotSearch = QtWidgets.QLineEdit(self.tabShot)
        self.lineEditShotSearch.setObjectName("lineEditShotSearch")
        self.gridLayoutShot.addWidget(self.lineEditShotSearch, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayoutShot)
        self.tabWidgetList.addTab(self.tabShot, "")
        self.tabSequence = QtWidgets.QWidget()
        self.tabSequence.setObjectName("tabSequence")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabSequence)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayoutSequence = QtWidgets.QGridLayout()
        self.gridLayoutSequence.setObjectName("gridLayoutSequence")
        self.treeViewSequence = QtWidgets.QTreeView(self.tabSequence)
        self.treeViewSequence.setObjectName("treeViewSequence")
        self.gridLayoutSequence.addWidget(self.treeViewSequence, 1, 0, 1, 1)
        self.lineEditSequenceSearch = QtWidgets.QLineEdit(self.tabSequence)
        self.lineEditSequenceSearch.setObjectName("lineEditSequenceSearch")
        self.gridLayoutSequence.addWidget(self.lineEditSequenceSearch, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayoutSequence, 0, 0, 1, 1)
        self.tabWidgetList.addTab(self.tabSequence, "")
        self.gridLayout_3.addWidget(self.tabWidgetList, 0, 0, 1, 1)
        self.pushButtonPublish = QtWidgets.QPushButton(ShotgunDesktopVersionDialog)
        self.pushButtonPublish.setObjectName("pushButtonPublish")
        self.gridLayout_3.addWidget(self.pushButtonPublish, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(ShotgunDesktopVersionDialog)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.labelVersion = QtWidgets.QLabel(self.splitter)
        self.labelVersion.setObjectName("labelVersion")
        self.listWidgetVersion = QtWidgets.QListWidget(self.splitter)
        self.listWidgetVersion.setObjectName("listWidgetVersion")
        self.lineEditDescription = QtWidgets.QLineEdit(self.splitter)
        self.lineEditDescription.setInputMask("")
        self.lineEditDescription.setText("")
        self.lineEditDescription.setMaxLength(32767)
        self.lineEditDescription.setObjectName("lineEditDescription")
        self.labelAttachment = QtWidgets.QLabel(self.splitter)
        self.labelAttachment.setObjectName("labelAttachment")
        self.listWidgetAttachment = QtWidgets.QListWidget(self.splitter)
        self.listWidgetAttachment.setObjectName("listWidgetAttachment")
        self.gridLayout_3.addWidget(self.splitter, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 3)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi(ShotgunDesktopVersionDialog)
        self.tabWidgetList.setCurrentIndex(0)
        QtCore.QObject.connect(self.lineEditAssetSearch, QtCore.SIGNAL("returnPressed()"), ShotgunDesktopVersionDialog.search_asset_slot)
        QtCore.QObject.connect(self.lineEditShotSearch, QtCore.SIGNAL("returnPressed()"), ShotgunDesktopVersionDialog.search_shot_slot)
        QtCore.QObject.connect(self.lineEditSequenceSearch, QtCore.SIGNAL("returnPressed()"), ShotgunDesktopVersionDialog.search_sequence_slot)
        QtCore.QObject.connect(self.lineEditMyTaskSearch, QtCore.SIGNAL("returnPressed()"), ShotgunDesktopVersionDialog.search_mytask_slot)
        # QtCore.QObject.connect(self.pushButtonPublish, QtCore.SIGNAL("clicked()"), ShotgunDesktopVersionDialog.publish_slot)
        QtCore.QMetaObject.connectSlotsByName(ShotgunDesktopVersionDialog)

    def retranslateUi(self, ShotgunDesktopVersionDialog):
        ShotgunDesktopVersionDialog.setWindowTitle(QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "ShotgunVersionDesktop", None, -1))
        self.tabWidgetList.setTabText(self.tabWidgetList.indexOf(self.tabMyTask), QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "MyTasks", None, -1))
        self.tabWidgetList.setTabText(self.tabWidgetList.indexOf(self.tabAsset), QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "Assets", None, -1))
        self.tabWidgetList.setTabText(self.tabWidgetList.indexOf(self.tabShot), QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "Shots", None, -1))
        self.tabWidgetList.setTabText(self.tabWidgetList.indexOf(self.tabSequence), QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "Sequences", None, -1))
        self.pushButtonPublish.setText(QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "Publish", None, -1))
        self.labelVersion.setText(QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "Version", None, -1))
        self.lineEditDescription.setPlaceholderText(QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "Version Description", None, -1))
        self.labelAttachment.setText(QtWidgets.QApplication.translate("ShotgunDesktopVersionDialog", "Attachment", None, -1))
