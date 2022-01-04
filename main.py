#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox
from tasarim import Ui_MainWindow
from parser import Parser
from append import Append
from db import DB
from strings import *

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.dbobject = DB("db.json", "drdb.json")
        self.parser_list = []
        self.db, self.drdb = self.dbobject.refresh_db()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_list_item()
        self.ui.dr_tree.itemClicked.connect(self.activeItem)
        self.ui.ekle_button.clicked.connect(self.kisaltma_ekle)
        self.ui.sil_button.clicked.connect(self.kisaltma_sil)
        self.ui.search_line_2.textChanged.connect(self.search_kisaltma)

    def add_list_item(self):

        for i in self.db.keys():
            tw = QTreeWidgetItem([self.drdb[i]])
            self.ui.dr_tree.addTopLevelItem(tw)
            for j in self.db[i][0].keys():
                tc = tw.addChild(QTreeWidgetItem([j]))


    def refresh_list(self, liste=[]):

        self.db, self.drdb = self.dbobject.refresh_db()

        for i in self.ui.dr_tree.findItems("",QtCore.Qt.MatchContains):

            self.ui.dr_tree.clear()

        for i in self.db.keys():
            tw = QTreeWidgetItem([self.drdb[i]])
            self.ui.dr_tree.addTopLevelItem(tw)
            for j in self.db[i][0].keys():
                tc = tw.addChild(QTreeWidgetItem([j]))


    def activeItem(self,item):

        self.selected_item = item
        if item.childCount() == 0:
            self.selected_dr = item.parent()
            drid = str(self.ui.dr_tree.indexOfTopLevelItem(item.parent())+1)
            self.ui.karsilik.setText(self.db[drid][0][item.text(0)])
        else:
            self.selected_dr = item
            drid = str(self.ui.dr_tree.indexOfTopLevelItem(item)+1)
            self.ui.karsilik.setText(self.drdb[drid])

    def kisaltma_ekle(self):

        try:
            self.append = Append(self.parser_list, anadosya)
            self.append.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            self.append.hocaid = str(self.ui.dr_tree.indexOfTopLevelItem(self.selected_dr) + 1)
            self.append.exec_()
            del self.append
            self.refresh_list()

        except AttributeError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen ekleme yapmak istediğiniz doktor adını seçiniz!")
            msg.setWindowTitle("Dikkat!!!")
            msg.exec_()

    def kisaltma_sil(self):

        try:
            hocaid = str(self.ui.dr_tree.indexOfTopLevelItem(self.selected_dr) + 1)
            self.dbobject.del_db_hoca_alti(hocaid,self.selected_item.text(0))
            self.refresh_list()

        except AttributeError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen silmek istediğiniz kısaltmayı seçiniz!")
            msg.setWindowTitle("Dikkat!!!")
            msg.exec_()

    def search_kisaltma(self, arama):
        items = self.ui.kisaltmalar.findItems(arama,QtCore.Qt.MatchContains)
        self.refresh_list(items)



if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec_()
