#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QMessageBox
from tasarim import Ui_MainWindow
from parser import Parser
from append import Append
from db import DB
from error import ErrorMessage
from checksure import CheckSure
from dr import Dr
from drappend import DrAppend
from strings import *

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.dbobject = DB("db.json")
        self.db = self.dbobject.get_db()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_list_dr_list_item()
        self.add_list_dr_tree_item()
        self.ui.dr_ekle_button.clicked.connect(self.dr_ekle)
        self.ui.dr_sadece_sec_button.clicked.connect(self.dr_sadece_sec)
        self.ui.dr_sec_ayarla_button.clicked.connect(self.dr_sec_ayarla)
        self.ui.dr_sil_button.clicked.connect(self.dr_sil)
        self.ui.dr_tree.itemClicked.connect(self.activeItem)
        self.ui.ekle_button.clicked.connect(self.kisaltma_ekle)
        self.ui.duzelt_button.clicked.connect(self.kisaltma_duzelt)
        self.ui.sil_button.clicked.connect(self.kisaltma_sil)
        self.ui.search_line_2.textEdited.connect(self.search_kisaltma)

    def update(self):
        self.db = self.dbobject.get_db()
        self.ui.dr_tree.clear()
        self.ui.dr_list.clear()
        self.add_list_dr_list_item()
        self.add_list_dr_tree_item()

    def add_list_dr_tree_item(self):

        for i in self.db.keys():
            tw = Dr(i,self.db[i]["isim"],self.db[i]["kisaltmalar"])
            self.ui.dr_tree.addTopLevelItem(tw)
            try:
                for j in self.db[i]["kisaltmalar"].keys():
                    tc = tw.addChild(QTreeWidgetItem([j]))
            except IndexError:
                pass

    def add_list_dr_list_item(self):

        for i in self.db.keys():
            tw = Dr(i,self.db[i]["isim"],self.db[i]["kisaltmalar"])
            self.ui.dr_list.addTopLevelItem(tw)

    def dr_sadece_sec(self):
        dr = self.ui.dr_list.currentItem()
        if dr:
            item = self.ui.dr_list.currentItem()
            for i in self.ui.dr_tree.findItems("",QtCore.Qt.MatchContains):
                if i.get_id() == item.get_id():
                    i.setHidden(False)
                else:
                    i.setHidden(True)
        else:
            err = ErrorMessage(QMessageBox.Warning,"L??tfen bir doktor se??iniz.",error_message_baslik_dikkat)

    def dr_sec_ayarla(self):
        dr = self.ui.dr_list.currentItem()
        if dr:
            content = ""
            dr = self.ui.dr_list.currentItem()
            kisaltmalar = dr.get_kisaltmalar()
            genel_kisaltmalar = self.dbobject.get_kisaltma_from_id("0")
            for i in genel_kisaltmalar.keys():
                content += ekle.format(i,genel_kisaltmalar[i])
            for i in kisaltmalar.keys():
                content += ekle.format(i,kisaltmalar[i])
            with open(espanso_file,"w", encoding="utf-8") as f:
                f.write(giris + content)
        else:
            err = ErrorMessage(QMessageBox.Warning,"L??tfen bir doktor se??iniz.",error_message_baslik_dikkat)

    def dr_ekle(self):
        drapp = DrAppend(id)
        drapp.exec_()
        self.update()

    def dr_sil(self):
        dr = self.ui.dr_list.currentItem()
        if dr:
            cs = CheckSure(self.ui.centralwidget,csbaslik,csmesaj)
            cevap = cs.close_event()
            if cevap == QMessageBox.Yes:
                self.dbobject.remove_dr_db(dr.get_id())
                self.update()
            else:
                pass
        else:
            err = ErrorMessage(QMessageBox.Warning,dr_sil_error_mesage,error_message_baslik_dikkat)

    def kisaltma_ekle(self):
        dr = self.ui.dr_tree.currentItem()
        if isinstance(dr, Dr):
            self.append = Append(dr.get_id())
            self.append.exec_()
            self.update()
        else:
            err = ErrorMessage(QMessageBox.Warning,err_wrong_id,error_message_baslik_dikkat)

    def kisaltma_duzelt(self):
        item = self.ui.dr_tree.currentItem()
        if isinstance(item, Dr):
            err = ErrorMessage(QMessageBox.Warning,err_wrong_id_kisaltma,error_message_baslik_dikkat)
        else:
            drid = item.parent().get_id()
            karsiliklar = item.parent().get_kisaltmalar()
            self.append = Append(drid)
            self.append.set_duzeltme_mi(True)
            self.append.set_duzeltme_text(item.text(0))
            self.append.kisayol_line.setText(item.text(0))
            self.append.karsilik_line.setText(karsiliklar[item.text(0)])
            self.append.exec_()
            self.update()

    def kisaltma_sil(self):
        item = self.ui.dr_tree.currentItem()
        if isinstance(item, Dr):
            err = ErrorMessage(QMessageBox.Warning,err_wrong_id_kisaltma,error_message_baslik_dikkat)
        else:
            drid = item.parent().get_id()
            cs = CheckSure(self.ui.centralwidget,csbaslik,csmesajkisaltma)
            cevap = cs.close_event()
            if cevap == QMessageBox.Yes:
                self.dbobject.remove_kisaltma_db(drid,item.text(0))
                self.update()
            else:
                pass

    def activeItem(self,item):

        self.selected_item = item
        if isinstance(self.selected_item, Dr):
            self.selected_dr = item
            drid = item.get_id()
            self.ui.karsilik.setText(self.db[drid]["isim"])
        else:
            self.selected_dr = item.parent()
            drid = self.selected_dr.get_id()
            self.ui.karsilik.setText(self.db[drid]["kisaltmalar"][item.text(0)])


    def search_kisaltma(self, arama):
        for i in self.ui.dr_tree.findItems("",QtCore.Qt.MatchContains):
            kisaltmalar = i.get_kisaltmalar_ids()
            child_count = len(kisaltmalar)
            if child_count == 0:
                continue
            else:
                i.setHidden(True)
            for j in range(0,child_count):
                if kisaltmalar[j].find(arama) == -1:
                    i.child(j).setHidden(True)
                else:
                    i.child(j).setHidden(False)
                    i.setHidden(False)




if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec_()
