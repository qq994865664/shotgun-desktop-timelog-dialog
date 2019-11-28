# -*- coding: utf-8 -*-

# @Time         :2019/11/28 17:39
# @Auther       :ZhongHao
# @FileName     :desktop_timelog_dialog.py
# @PackageName  :shotgun_desktop_tool
# @IDE          :PyCharm
import os
import ui_sg_desktop_timelog_dialog

from PySide2.QtCore import QPoint
from PySide2.QtWidgets import QListWidgetItem, QMenu, QAction, QMessageBox
from PySide2.QtGui import QStandardItemModel, QStandardItem, QCursor
from PySide2 import QtWidgets, QtCore

from shotgun_tool_package import sg_config
from shotgun_tool_package import sg_publish
from shotgun_tool_package import sg_base_find
import datetime
from pprint import pprint
import getpass


class DesktopTimelogDialog(QtWidgets.QWidget, ui_sg_desktop_timelog_dialog.Ui_ShotgunDesktopTimelogDialog):

    def __init__(self, project_name, parent=None):
        super(DesktopTimelogDialog, self).__init__(parent)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.treeViewAsset.expanded.connect(self.asset_expanded)
        self.treeViewShot.expanded.connect(self.shot_expanded)
        self.treeViewSequence.expanded.connect(self.sequence_expanded)
        self.treeViewAsset.clicked.connect(self.treeview_single_clicked)
        self.treeViewShot.clicked.connect(self.treeview_single_clicked)
        self.treeViewSequence.clicked.connect(self.treeview_single_clicked)
        self.treeViewMyTask.clicked.connect(self.treeview_single_clicked)
        self.timer.timeout.connect(self.disable_double_clicked)

        self.pushButtonSubmit.setEnabled(False)
        self.dateEditDate.setDate(QtCore.QDate.currentDate())

        self.project_name = project_name
        self.user_name = getpass.getuser()
        self.sg = sg_publish.ShotgunPublish()
        self.project_entity = self.sg.get_project(self.project_name)

        # init source model
        self.source_asset_model = QStandardItemModel(self.treeViewAsset)
        self.source_shot_model = QStandardItemModel(self.treeViewShot)
        self.source_sequence_model = QStandardItemModel(self.treeViewSequence)
        self.source_mytask_model = QStandardItemModel(self.treeViewMyTask)

        # init treeview ui data
        self.tab_asset_ui()
        self.tab_shot_ui()
        self.tab_sequence_ui()
        self.tab_mytask_ui()

        self._project_level_info = []

    @QtCore.Slot()
    def search_asset_slot(self):
        '''
        search asset slot function
        :return:
        '''
        search_text = self.lineEditAssetSearch.text()
        if not search_text:
            self.tab_asset_init()
        else:
            self.tab_asset_search_init()
            self.search_asset(self.source_asset_model, search_text)

    @QtCore.Slot()
    def search_shot_slot(self):
        '''
        search shot slot function
        :return:
        '''
        search_text = self.lineEditShotSearch.text()
        if not search_text:
            self.tab_shot_init()
        else:
            self.tab_shot_search_init()
            self.search_shot(self.source_shot_model, search_text)

    @QtCore.Slot()
    def search_sequence_slot(self):
        '''
        search sequence slot function
        :return:
        '''
        search_text = self.lineEditSequenceSearch.text()
        if not search_text:
            self.tab_sequence_init()
        else:
            self.tab_sequence_search_init()
            self.search_sequence(self.source_sequence_model, search_text)

    @QtCore.Slot()
    def search_mytask_slot(self):
        '''
        search mytask slot function
        :return:
        '''
        search_text = self.lineEditMyTaskSearch.text()
        if not search_text:
            self.tab_mytask_init()
        else:
            self.tab_mytask_init()
            self.search_mytask(self.source_mytask_model, search_text)

    def search_mytask(self, source_model, search_text):
        '''
        search mytask
        :param source_model: source model
        :param search_text: text
        :return:
        '''
        mytask_type_item_temp_list = []
        for mytask_type_index in range(source_model.rowCount()):
            mytask_type_item = source_model.item(mytask_type_index, 0)
            mytask_type_item_temp = QStandardItem(mytask_type_item.text())
            mytask_type_item_temp.setEditable(False)
            for mytask_name_index in range(mytask_type_item.rowCount()):
                mytask_name_item = mytask_type_item.child(mytask_name_index, 0)
                mytask_name = mytask_name_item.text()
                if search_text in mytask_name:
                    mytask_name_item_temp = mytask_name_item.clone()
                    if mytask_name_item.hasChildren():
                        mytask_step_item = mytask_name_item.child(0, 0)
                        mytask_step_item_temp = mytask_step_item.clone()
                        if mytask_step_item.hasChildren():
                            mytask_step_task_item = mytask_step_item.child(0, 0)
                            mytask_step_task_item_temp = mytask_step_task_item.clone()
                            mytask_step_item_temp.appendRow(mytask_step_task_item_temp)
                        mytask_name_item_temp.appendRow(mytask_step_item_temp)
                    mytask_name_item_temp.setEditable(False)
                    mytask_type_item_temp.appendRow(mytask_name_item_temp)
            if mytask_type_item_temp.hasChildren():
                mytask_type_item_temp_list.append(mytask_type_item_temp)
        source_model.clear()
        for item in mytask_type_item_temp_list:
            source_model.appendRow(item)

    def search_sequence(self, source_model, search_text):
        '''
        search sequence
        :param source_model: source model
        :param search_text: text
        :return:
        '''
        sequence_item_temp_list = []
        for sequence_index in range(source_model.rowCount()):
            sequence_item = source_model.item(sequence_index, 0)
            sequence_name = sequence_item.text()
            if search_text in sequence_name:
                sequence_name_item_temp = QStandardItem(sequence_name)
                retrieving = QStandardItem("Retrieving Tasks...")
                retrieving.setEditable(False)
                sequence_name_item_temp.appendRow(retrieving)
                sequence_name_item_temp.setEditable(False)
                sequence_item_temp_list.append(sequence_name_item_temp)
        source_model.clear()
        for item in sequence_item_temp_list:
            source_model.appendRow(item)

    def search_shot(self, source_model, search_text):
        '''
        search shot
        :param source_model: source model
        :param search_text: text
        :return:
        '''
        sequence_item_temp_list = []
        for sequence_index in range(source_model.rowCount()):
            sequence_item = source_model.item(sequence_index, 0)
            sequence_item_temp = QStandardItem(sequence_item.text())
            sequence_item_temp.setEditable(False)
            for shot_name_index in range(sequence_item.rowCount()):
                shot_name_item = sequence_item.child(shot_name_index, 0)
                shot_name = shot_name_item.text()
                if search_text in shot_name:
                    shot_name_item_temp = shot_name_item.clone()
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    shot_name_item_temp.appendRow(retrieving)
                    shot_name_item_temp.setEditable(False)
                    sequence_item_temp.appendRow(shot_name_item_temp)
            if sequence_item_temp.hasChildren():
                sequence_item_temp_list.append(sequence_item_temp)
        source_model.clear()
        for item in sequence_item_temp_list:
            source_model.appendRow(item)

    def search_asset(self, source_model, search_text):
        '''
        search asset
        :param source_model: source model
        :param search_text: text
        :return:
        '''
        asset_type_item_temp_list = []
        for asset_type_index in range(source_model.rowCount()):
            asset_type_item = source_model.item(asset_type_index, 0)
            asset_type_item_temp = QStandardItem(asset_type_item.text())
            asset_type_item_temp.setEditable(False)
            for asset_name_index in range(asset_type_item.rowCount()):
                asset_name_item = asset_type_item.child(asset_name_index, 0)
                asset_name = asset_name_item.text()
                if search_text in asset_name:
                    asset_name_item_temp = asset_name_item.clone()
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    asset_name_item_temp.appendRow(retrieving)
                    asset_name_item_temp.setEditable(False)
                    asset_type_item_temp.appendRow(asset_name_item_temp)
            if asset_type_item_temp.hasChildren():
                asset_type_item_temp_list.append(asset_type_item_temp)
        source_model.clear()
        for item in asset_type_item_temp_list:
            source_model.appendRow(item)

    def tab_asset_ui(self):
        '''
        tab asset ui
        :return:
        '''
        self.tab_asset_init()
        self.treeViewAsset.setModel(self.source_asset_model)
        self.treeViewAsset.setHeaderHidden(True)

    def tab_shot_ui(self):
        '''
        tab shot ui
        :return:
        '''
        self.tab_shot_init()
        self.treeViewShot.setModel(self.source_shot_model)
        self.treeViewShot.setHeaderHidden(True)

    def tab_sequence_ui(self):
        '''
        tab sequence ui
        :return:
        '''
        self.tab_sequence_init()
        self.treeViewSequence.setModel(self.source_sequence_model)
        self.treeViewSequence.setHeaderHidden(True)

    def tab_mytask_ui(self):
        '''
        tab mytask ui
        :return:
        '''
        self.tab_mytask_init()
        self.treeViewMyTask.setModel(self.source_mytask_model)
        self.treeViewMyTask.setHeaderHidden(True)

    def tab_asset_init(self):
        '''
        init asset list in treeView
        :return:
        '''
        self.source_asset_model.clear()

        asset_type_list = ['Chr',
                           'Env',
                           'Prp',
                           'Flg',
                           'Crd',
                           'Scn',
                           'Uif',
                           'Asb']

        for asset_type in asset_type_list:
            asset_type_item = QStandardItem(asset_type)
            asset_type_item.setEditable(False)
            # append the next level item
            retrieving = QStandardItem("Retrieving Tasks...")
            retrieving.setEditable(False)
            asset_type_item.appendRow(retrieving)

            self.source_asset_model.appendRow(asset_type_item)

    def tab_shot_init(self):
        '''
        init shot list in treeView
        :return:
        '''
        self.source_shot_model.clear()
        sequence_entity_list = self.sg.get_sequence_list(self.project_name)
        if sequence_entity_list:
            for sequence_entity in sequence_entity_list:
                sequence_name = sequence_entity['code']
                sequence_name_item = QStandardItem(sequence_name)
                sequence_name_item.setEditable(False)

                retrieving = QStandardItem("Retrieving Tasks...")
                retrieving.setEditable(False)
                sequence_name_item.appendRow(retrieving)

                self.source_shot_model.appendRow(sequence_name_item)

    def tab_sequence_init(self):
        '''
        init sequence list in treeView
        :return:
        '''
        self.source_sequence_model.clear()
        sequence_entity_list = self.sg.get_sequence_list(self.project_name)
        if sequence_entity_list:
            for sequence_entity in sequence_entity_list:
                sequence_name = sequence_entity['code']
                sequence_name_item = QStandardItem(sequence_name)
                sequence_name_item.setEditable(False)
                # append the next level item
                retrieving = QStandardItem("Retrieving Tasks...")
                retrieving.setEditable(False)
                sequence_name_item.appendRow(retrieving)
                self.source_sequence_model.appendRow(sequence_name_item)

    def tab_mytask_init(self):
        '''
        init mytask list in treeView
        :return:
        '''
        self.source_mytask_model.clear()
        mytask_entity_list = self.sg.get_mytask_list(self.project_name, self.user_name)
        mytask_type_sequence_item = QStandardItem("Sequence")
        mytask_type_asset_item = QStandardItem("Asset")
        mytask_type_shot_item = QStandardItem("Shot")
        mytask_type_sequence_item.setEditable(False)
        mytask_type_asset_item.setEditable(False)
        mytask_type_shot_item.setEditable(False)

        mytask_link_type_list_item = [mytask_type_sequence_item, mytask_type_asset_item, mytask_type_shot_item]

        if mytask_entity_list:
            for mytask_entity in mytask_entity_list:
                mytask_name = mytask_entity['content']
                mytask_link_name = mytask_entity['entity']['name']
                mytask_link_type = mytask_entity['entity']['type']
                mytask_step_name = mytask_entity['step']['name']

                mytask_name_item = QStandardItem(mytask_name)
                mytask_name_item.setEditable(False)
                mytask_step_name_item = QStandardItem(mytask_step_name)
                mytask_step_name_item.setEditable(False)
                mytask_step_name_item.appendRow(mytask_name_item)
                mytask_link_name_item = QStandardItem(mytask_link_name)
                mytask_link_name_item.setEditable(False)
                mytask_link_name_item.appendRow(mytask_step_name_item)
                for mytask_link_type_item in mytask_link_type_list_item:
                    if mytask_link_type_item.text() == mytask_link_type:
                        mytask_link_type_item.appendRow(mytask_link_name_item)
            self.source_mytask_model.appendColumn(mytask_link_type_list_item)

    def tab_asset_search_init(self):
        '''
        init asset list in treeView(Only for search!)
        :return:
        '''
        self.source_asset_model.clear()

        asset_type_list = ['Chr',
                           'Env',
                           'Prp',
                           'Flg',
                           'Crd',
                           'Scn',
                           'Uif',
                           'Asb']

        for asset_type in asset_type_list:
            asset_type_item = QStandardItem(asset_type)
            asset_type_item.setEditable(False)

            asset_entity_list = self.sg.get_asset_list(self.project_name, asset_type)
            if asset_entity_list:
                for asset_entity in asset_entity_list:
                    asset_name = asset_entity['code']
                    asset_name_chinesename = asset_entity['sg_chinesename']
                    if asset_name_chinesename:
                        asset_name = asset_name + "|" + asset_name_chinesename
                    asset_name_item = QStandardItem(asset_name)
                    asset_name_item.setEditable(False)

                    # append the next level item
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    asset_name_item.appendRow(retrieving)

                    asset_type_item.appendRow(asset_name_item)

            self.source_asset_model.appendRow(asset_type_item)

    def tab_shot_search_init(self):
        '''
        init shot list in treeView(Only for search!)
        :return:
        '''
        self.source_shot_model.clear()
        sequence_entity_list = self.sg.get_sequence_list(self.project_name)
        if sequence_entity_list:
            for sequence_entity in sequence_entity_list:
                sequence_name = sequence_entity['code']
                sequence_name_item = QStandardItem(sequence_name)
                sequence_name_item.setEditable(False)

                # find the shot below sequence
                shot_entity_list = self.sg.get_sequence_shot_list(self.project_name, sequence_name)
                if shot_entity_list:
                    for shot_entity in shot_entity_list:
                        shot_name = shot_entity['code']
                        shot_name_item = QStandardItem(shot_name)
                        shot_name_item.setEditable(False)

                        # append the next level item
                        retrieving = QStandardItem("Retrieving Tasks...")
                        retrieving.setEditable(False)
                        shot_name_item.appendRow(retrieving)

                        sequence_name_item.appendRow(shot_name_item)

                self.source_shot_model.appendRow(sequence_name_item)

    def tab_sequence_search_init(self):
        '''
        init sequence list in treeView(Only for search!)
        :return:
        '''
        self.source_sequence_model.clear()
        sequence_entity_list = self.sg.get_sequence_list(self.project_name)
        if sequence_entity_list:
            for sequence_entity in sequence_entity_list:
                sequence_name = sequence_entity['code']
                sequence_name_item = QStandardItem(sequence_name)
                sequence_name_item.setEditable(False)
                self.source_sequence_model.appendRow(sequence_name_item)

    @QtCore.Slot(int)
    def asset_expanded(self, index):
        '''
        asset treeView expanded
        :param index: index of the model
        :return:
        '''
        item = self.source_asset_model.itemFromIndex(index)
        asset_level_struct_item = []
        self.get_upper_level_item(self.source_asset_model, asset_level_struct_item, index)

        item_level = len(asset_level_struct_item)

        if item_level == 1:
            search_text = self.lineEditAssetSearch.text()
            if search_text:
                return
            item.removeRows(0, item.rowCount())
            # this is the top level
            _asset_type = asset_level_struct_item[0]
            asset_entity_list = self.sg.get_asset_list(self.project_name, _asset_type)
            if asset_entity_list:
                for asset_entity in asset_entity_list:
                    asset_name = asset_entity['code']
                    asset_name_chinesename = asset_entity['sg_chinesename']
                    if asset_name_chinesename:
                        asset_name = asset_name + "|" + asset_name_chinesename
                    asset_name_item = QStandardItem(asset_name)
                    asset_name_item.setEditable(False)

                    # append the next level item
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    asset_name_item.appendRow(retrieving)

                    item.appendRow(asset_name_item)
            else:
                # if this level not item then show Retrieving Task...
                retrieving = QStandardItem("Retrieving Tasks...")
                retrieving.setEditable(False)
                item.appendRow(retrieving)

        elif item_level == 2:
            item.removeRows(0, item.rowCount())
            asset_name = asset_level_struct_item[1]
            asset_task_list = self.sg.get_asset_task_list(self.project_name, asset_name)
            asset_step_name_set = set()
            if asset_task_list:
                for asset_task in asset_task_list:
                    asset_task_step = asset_task['step']
                    if asset_task_step:
                        asset_task_step_name = asset_task_step['name']
                        # remove all duplicate name in step by using set()
                        asset_step_name_set.add(asset_task_step_name)
                for step_name in asset_step_name_set:
                    asset_task_step_name_item = QStandardItem(step_name)
                    asset_task_step_name_item.setEditable(False)

                    # append the next level item
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    asset_task_step_name_item.appendRow(retrieving)

                    item.appendRow(asset_task_step_name_item)
                    asset_level_struct_item.append(step_name)

        elif item_level == 3:
            item.removeRows(0, item.rowCount())
            asset_name = asset_level_struct_item[1]
            asset_step_name = asset_level_struct_item[2]
            asset_task_list = self.sg.get_asset_task_list(self.project_name, asset_name, asset_step_name)
            if asset_task_list:
                for asset_task in asset_task_list:
                    asset_task_name = asset_task['content']
                    asset_task_name_item = QStandardItem(asset_task_name)
                    asset_task_name_item.setEditable(False)

                    item.appendRow(asset_task_name_item)

    @QtCore.Slot(int)
    def shot_expanded(self, index):
        '''
        shot treeView expanded
        :param index: index of the model
        :return:
        '''
        # dynamic load data from shotgun server database
        item = self.source_shot_model.itemFromIndex(index)
        shot_level_struct_item = []
        self.get_upper_level_item(self.source_shot_model, shot_level_struct_item, index)
        item_level = len(shot_level_struct_item)
        # search item from shotgun server
        if item_level == 1:
            search_text = self.lineEditShotSearch.text()
            if search_text:
                return
            item.removeRows(0, item.rowCount())
            # this is the top level
            sequence_name = shot_level_struct_item[0]
            # find the shot below sequence
            shot_entity_list = self.sg.get_sequence_shot_list(self.project_name, sequence_name)
            if shot_entity_list:
                for shot_entity in shot_entity_list:
                    shot_name = shot_entity['code']
                    shot_name_item = QStandardItem(shot_name)
                    shot_name_item.setEditable(False)

                    # append the next level item
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    shot_name_item.appendRow(retrieving)

                    item.appendRow(shot_name_item)
            else:
                # if this level not item then show Retrieving Task...
                retrieving = QStandardItem("Retrieving Tasks...")
                retrieving.setEditable(False)
                item.appendRow(retrieving)

        elif item_level == 2:
            item.removeRows(0, item.rowCount())
            sequence_name = shot_level_struct_item[0]
            shot_name = shot_level_struct_item[1]
            shot_task_list = self.sg.get_sequence_shot_task_list(self.project_name, sequence_name, shot_name)
            shot_step_name_set = set()
            if shot_task_list:
                for shot_task in shot_task_list:
                    shot_task_step = shot_task['step']
                    if shot_task_step:
                        shot_task_step_name = shot_task_step['name']
                        # remove all duplicate name in step by using set()
                        shot_step_name_set.add(shot_task_step_name)
                for step_name in shot_step_name_set:
                    shot_task_step_name_item = QStandardItem(step_name)
                    shot_task_step_name_item.setEditable(False)

                    # append the next level item
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    shot_task_step_name_item.appendRow(retrieving)

                    item.appendRow(shot_task_step_name_item)
                    shot_level_struct_item.append(step_name)

        elif item_level == 3:
            item.removeRows(0, item.rowCount())
            sequence_name = shot_level_struct_item[0]
            shot_name = shot_level_struct_item[1]
            shot_step_name = shot_level_struct_item[2]
            shot_task_list = self.sg.get_sequence_shot_task_list(self.project_name, sequence_name, shot_name,
                                                                 shot_step_name)
            if shot_task_list:
                for shot_task in shot_task_list:
                    shot_task_name = shot_task['content']
                    shot_task_name_item = QStandardItem(shot_task_name)
                    shot_task_name_item.setEditable(False)

                    item.appendRow(shot_task_name_item)

    @QtCore.Slot(int)
    def sequence_expanded(self, index):
        '''
        sequence treeView expanded
        :param index: index of the model
        :return:
        '''
        # dynamic load data from shotgun server database
        item = self.source_sequence_model.itemFromIndex(index)
        item.removeRows(0, item.rowCount())
        sequence_level_struct_item = []
        self.get_upper_level_item(self.source_sequence_model, sequence_level_struct_item, index)
        item_level = len(sequence_level_struct_item)
        # search item from shotgun server
        if item_level == 1:
            # this is the top level
            sequence_name = sequence_level_struct_item[0]
            # find the step below sequence
            sequence_task_list = self.sg.get_sequence_task_list(self.project_name, sequence_name)
            sequence_step_name_set = set()
            if sequence_task_list:
                for sequence_task in sequence_task_list:
                    sequence_task_step = sequence_task['step']
                    if sequence_task_step:
                        sequence_task_step_name = sequence_task_step['name']
                        # remove all duplicate name in step by using set()
                        sequence_step_name_set.add(sequence_task_step_name)
                for step_name in sequence_step_name_set:
                    sequence_task_step_name_item = QStandardItem(step_name)
                    sequence_task_step_name_item.setEditable(False)

                    # append the next level item
                    retrieving = QStandardItem("Retrieving Tasks...")
                    retrieving.setEditable(False)
                    sequence_task_step_name_item.appendRow(retrieving)

                    item.appendRow(sequence_task_step_name_item)
                    sequence_level_struct_item.append(step_name)

        elif item_level == 2:
            sequence_name = sequence_level_struct_item[0]
            sequence_step_name = sequence_level_struct_item[1]
            sequence_task_list = self.sg.get_sequence_task_list(self.project_name, sequence_name, sequence_step_name)
            if sequence_task_list:
                for sequence_task in sequence_task_list:
                    sequence_task_name = sequence_task['content']
                    sequence_task_name_item = QStandardItem(sequence_task_name)
                    sequence_task_name_item.setEditable(False)

                    item.appendRow(sequence_task_name_item)

    def treeview_single_clicked(self, index):
        '''
        treeView single clicked
        :param index: index of model
        :return:
        '''
        if not self.timer.isActive():
            self.timer.start(500)
            self.listwidget_show_item_info(index)

    @QtCore.Slot()
    def disable_double_clicked(self):
        '''
        disable double clicked
        :return:
        '''
        self.timer.stop()

    @QtCore.Slot()
    def listwidget_show_item_info(self, index):
        '''
        this function process the published file to show in listWidget
        :param index: index of model
        :return:
        '''
        tab_index = self.tabWidgetList.currentIndex()
        project_level_info = None
        self._project_level_info = []
        if tab_index == 0:
            # mytask table
            project_level_info = self.get_mytask_level_info(self.source_mytask_model, index)

        elif tab_index == 1:
            # asset table
            project_level_info = self.get_asset_level_info(self.source_asset_model, index)

        elif tab_index == 2:
            # shot table
            project_level_info = self.get_shot_level_info(self.source_shot_model, index)

        elif tab_index == 3:
            # sequence table
            project_level_info = self.get_sequence_level_info(self.source_sequence_model, index)

        if project_level_info:
            self._project_level_info = project_level_info
            self.pushButtonSubmit.setEnabled(True)
        else:
            self.pushButtonSubmit.setEnabled(False)
        # self.show_published_files_info(project_level_info)

    def get_sequence_level_info(self, source_model, index):
        '''
        get the sequence published file from shotgun
        :param source_model: the source model
        :param index: the index of source model
        :return: file info list
        '''
        project_level_struct_item = []
        published_file_info_list = None
        project_level_info = []
        self.get_upper_level_item(source_model, project_level_struct_item, index)
        item_level = len(project_level_struct_item)
        if item_level >= 3:
            # it is 3 level in the treeview widget
            _sequence_name = project_level_struct_item[0]
            _sequence_step_name = project_level_struct_item[1]
            _sequence_step_task_name = project_level_struct_item[2]
            project_level_info = project_level_struct_item

            # dict_data = sg_base_find.create_project_struct(self.project_name, self.user_name,
            #                                                "sequence",
            #                                                sequence_name=_sequence_name,
            #                                                sequence_step_name=_sequence_step_name,
            #                                                sequence_step_task_name=_sequence_step_task_name)
            # published_file_info_list = self.sg.get_published_file_list(dict_data)
        # return published_file_info_list
        return project_level_info

    def get_shot_level_info(self, source_model, index):
        '''
        get the shot published file from shotgun
        :param source_model: the source model
        :param index: the index of source model
        :return: file info list
        '''
        project_level_struct_item = []
        project_level_info = []
        published_file_info_list = None
        self.get_upper_level_item(source_model, project_level_struct_item, index)
        item_level = len(project_level_struct_item)
        if item_level >= 4:
            # it is 4 level in the treeview widget
            _sequence_name = project_level_struct_item[0]
            _sequence_shot_name = project_level_struct_item[1]
            _sequence_shot_step_name = project_level_struct_item[2]
            _sequence_shot_step_task_name = project_level_struct_item[3]
            project_level_info = project_level_struct_item

        #     dict_data = sg_base_find.create_project_struct(self.project_name, self.user_name, "shot",
        #                                                    sequence_name=_sequence_name,
        #                                                    sequence_shot_name=_sequence_shot_name,
        #                                                    sequence_shot_step_name=_sequence_shot_step_name,
        #                                                    sequence_shot_step_task_name=_sequence_shot_step_task_name)
        #     published_file_info_list = self.sg.get_published_file_list(dict_data)
        # return published_file_info_list
        return project_level_info

    def get_asset_level_info(self, source_model, index):
        '''
        get the asset published file from shotgun
        :param source_model: the source model
        :param index: the index of source model
        :return: file info list
        '''
        project_level_struct_item = []
        project_level_info = []
        published_file_info_list = None
        self.get_upper_level_item(source_model, project_level_struct_item, index)
        item_level = len(project_level_struct_item)
        if item_level >= 4:
            # it is 4 level in the treeview widget
            _asset_name = project_level_struct_item[1]
            _asset_step_name = project_level_struct_item[2]
            _asset_step_task_name = project_level_struct_item[3]
            project_level_info = project_level_struct_item

        #     dict_data = sg_base_find.create_project_struct(self.project_name, self.user_name, "asset",
        #                                                    asset_name=_asset_name, asset_step_name=_asset_step_name,
        #                                                    asset_step_task_name=_asset_step_task_name)
        #     published_file_info_list = self.sg.get_published_file_list(dict_data)
        # return published_file_info_list
        return project_level_info

    def get_mytask_level_info(self, source_model, index):
        '''
        get the mytask published file from shotgun
        :param source_model: the source model
        :param index: the index of source model
        :return: file info list
        '''
        project_level_struct_item = []
        project_level_info = []
        published_file_info_list = None
        self.get_upper_level_item(source_model, project_level_struct_item, index)
        item_level = len(project_level_struct_item)
        if item_level >= 4:
            # it is 4 level in the treeview widget
            mytask_type = project_level_struct_item[0]
            mytask_name = project_level_struct_item[1]
            mytask_step_name = project_level_struct_item[2]
            mytask_step_task_name = project_level_struct_item[3]
            project_level_info = project_level_struct_item

        #     if mytask_type == 'Asset':
        #         dict_data = sg_base_find.create_project_struct(self.project_name, self.user_name, "asset",
        #                                                        asset_name=mytask_name,
        #                                                        asset_step_name=mytask_step_name,
        #                                                        asset_step_task_name=mytask_step_task_name)
        #         published_file_info_list = self.sg.get_published_file_list(dict_data)
        #     elif mytask_type == 'Shot':
        #         sequence_name = mytask_name.split("_")[0]
        #         dict_data = sg_base_find.create_project_struct(self.project_name, self.user_name, "shot",
        #                                                        sequence_name=sequence_name,
        #                                                        sequence_shot_name=mytask_name,
        #                                                        sequence_shot_step_name=mytask_step_name,
        #                                                        sequence_shot_step_task_name=mytask_step_task_name)
        #         published_file_info_list = self.sg.get_published_file_list(dict_data)
        #     elif mytask_type == 'Sequence':
        #         dict_data = sg_base_find.create_project_struct(self.project_name, self.user_name,
        #                                                        "sequence",
        #                                                        sequence_name=mytask_name,
        #                                                        sequence_step_name=mytask_step_name,
        #                                                        sequence_step_task_name=mytask_step_task_name)
        #         published_file_info_list = self.sg.get_published_file_list(dict_data)
        # return published_file_info_list
        return project_level_info

    # get item list for treeView***
    def get_upper_level_item(self, source_model, level_struct_item, index):
        '''
        get the upper item name from treeView
        :param source_model: the source model
        :param level_struct_item: item list
        :param index: the index of source model
        '''
        item = source_model.itemFromIndex(index)
        if item.parent():
            self.get_upper_level_item(source_model, level_struct_item, item.parent().index())
        text = item.text()
        # strip chinese name if source_model is asset
        text = text.split("|")[0]
        level_struct_item.append(text)

    @QtCore.Slot()
    def submit_slot(self):
        date = self.dateEditDate.date().toString(QtCore.Qt.ISODate)
        print date


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = DesktopTimelogDialog("XCM_Test")
    win.show()
    sys.exit(app.exec_())
