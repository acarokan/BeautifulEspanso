import sys
import os
from shutil import copy
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox, QDialogButtonBox, QDialog, QApplication, QFileDialog, QMessageBox
from parser import Parser
from error import ErrorMessage
from db import DB
from strings import *

class Append(QDialog):
    def __init__(self,id):
        super().__init__()
        self.dr_id = id
        self.duzeltme_mi = False
        self.duzeltme_text = ""
        self.dbobject = DB("db.json")
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.accepted.connect(self.kisayol_ekle)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Espanso ekle")
        layout = QtWidgets.QFormLayout()
        self.kisayol_line = QLineEdit()
        self.karsilik_line = QLineEdit()
        self.file_button = QPushButton("Seç")
        self.file_button.clicked.connect(self.open_file)
        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.addWidget(QLabel("Kısaltma:"))
        self.row_1_layout.addWidget(self.kisayol_line)
        self.row_1_layout.addWidget(self.file_button)
        layout.addRow(self.row_1_layout)
        layout.addRow(QLabel("karşılık:"), self.karsilik_line)
        self.formGroupBox.setLayout(layout)

    def set_duzeltme_mi(self,bool):
        self.duzeltme_mi = bool

    def set_duzeltme_text(self,txt):
        self.duzeltme_text = txt

    def kisayol_kontrol(self,kisaltma):
        kisaltmalar = self.dbobject.get_kisaltma_from_id(self.dr_id)
        kisaltmalar = list(kisaltmalar.keys()) + list(self.dbobject.get_kisaltma_from_id("0"))
        if self.dr_id == "0":
            kisaltmalar = list(self.dbobject.get_all_kisaltmalar().keys())
        for i in kisaltmalar:
            if i.startswith(kisaltma) or kisaltma.startswith(i):
                return True

        return False

    def kisayol_ekle(self):
        if self.duzeltme_mi:
            self.kisayol_duzelt()
        else:
            data = {}
            self.kisayol = self.kisayol_line.text().strip().translate(lower_map).lower().split("|")
            self.karsilik = self.karsilik_line.text().strip().split("|")
            if len(self.kisayol) == len(self.karsilik):
                for i in range(0, len(self.kisayol)):
                    kontrol = self.kisayol_kontrol(self.kisayol[i].strip().translate(lower_map).lower())
                    if kontrol:
                        error = ErrorMessage(QMessageBox.Critical,"{} ile başlayan başka bir kısaltma mevcut. Lütfen yeniden deneyiniz.".format(self.kisayol[i].strip().translate(lower_map).lower()),"Hata")
                    else:
                        data.update({self.kisayol[i].strip().translate(lower_map).lower():self.karsilik[i].strip()})
                        self.dbobject.add_kisaltma_db(self.dr_id, data)
            else:
                error = ErrorMessage(QMessageBox.Critical,"Yeterli sayıda eşleşen eleman girmediniz","Hata")

    def kisayol_sil(self, kisaltma):
        del self.list[kisaltma]

    def kisayol_duzelt(self):
        self.kisayol = self.kisayol_line.text().strip().translate(lower_map).lower().split("|")
        self.karsilik = self.karsilik_line.text().strip().split("|")
        if len(self.kisayol) == len(self.karsilik):
            for i in range(0, len(self.kisayol)):
                kontrol = self.kisayol_kontrol(self.kisayol[i].strip().translate(lower_map).lower())
                if kontrol and self.duzeltme_text != self.kisayol[i].strip().translate(lower_map).lower():
                    error = ErrorMessage(QMessageBox.Critical,"{} ile başlayan başka bir kısaltma mevcut. Lütfen yeniden deneyiniz.".format(self.kisayol[i].strip().translate(lower_map).lower()),"Hata")
                else:
                    eski = self.duzeltme_text
                    eski_karsilik = self.dbobject.get_kisaltma_from_id(self.dr_id)[eski]
                    yeni_key = self.kisayol_line.text().strip().translate(lower_map).lower()
                    self.dbobject.remove_kisaltma_db(self.dr_id,eski)
                    data = {yeni_key: self.karsilik[i].strip()}
                    self.dbobject.add_kisaltma_db(self.dr_id, data)
        else:
            error = ErrorMessage(QMessageBox.Critical,"Yeterli sayıda eşleşen eleman girmediniz","Hata")

    def open_file(self):
        self.file_browser = QFileDialog()
        self.file_browser.exec_()
        files = self.file_browser.selectedFiles()
        if len(files) > 0:
            if files[0].endswith(".txt"):
                parser = Parser(files[0])
                self.kisayol_line.setText(parser.get_kisaltmalar_text())
                self.karsilik_line.setText(parser.get_karsiliklar_text())
            else:
                error = ErrorMessage(QMessageBox.Critical,"Dosya uzantısı txt olmalıdır","Hata!!!")
        else:
            pass



if __name__ == '__main__':
    l = {}
    app = QApplication(sys.argv)
    dialog = Append(l, "default_yedek.yml")
    sys.exit(dialog.exec_())
