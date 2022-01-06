import sys
import os
from shutil import copy
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QGroupBox, QDialogButtonBox, QVBoxLayout, QDialog, QApplication
from db import DB
from strings import *

lower_map = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
    ord(u'Ö'): u'ö',
    ord(u'ö'): u'ö',
    ord(u'Ü'): u'ü',
    ord(u'ü'): u'ü',
    ord(u'Ç'): u'ç',
    ord(u'ç'): u'ç',
    ord(u'Ş'): u'ş',
    ord(u'ş'): u'ş',
    ord(u'Ğ'): u'ğ',
    ord(u'ğ'): u'ğ',
    }


class Append(QDialog):
    def __init__(self,id):
        super().__init__()
        self.dr_id = id
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
        self.exec_()

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Espanso ekle")
        layout = QtWidgets.QFormLayout()
        self.kisayol_line = QLineEdit()
        self.karsilik_line = QLineEdit()
        layout.addRow(QLabel("Kısaltma:"), self.kisayol_line)
        layout.addRow(QLabel("karşılık:"), self.karsilik_line)
        self.formGroupBox.setLayout(layout)

    def kisayol_ekle(self):
        self.kisayol = self.kisayol_line.text().strip().translate(lower_map).lower()
        self.karsilik = self.karsilik_line.text().strip()
        data = {self.kisayol: self.karsilik}
        self.dbobject.add_kisaltma_db(self.dr_id, data)

    def kisayol_sil(self, kisaltma):
        del self.list[kisaltma]


"""
    def define_files(self):
        if self.file == "default":
            self.path = os.path.join(os.environ['HOMEPATH'],"AppData","Roaming","espanso")
            self.path_yedek = os.path.join(os.environ['USERPROFILE'],"OneDrive","Masaüstü")
            self.anadosya = os.path.join(self.path, "default.yml")
            self.yedekdosya = os.path.join(self.path_yedek, "default_yedek.yml")
        else:
            self.anadosya = self.file
            self.yedekdosya = "yedek.yml"

    def kisayol_ekle(self):
        self.yedekAl()
        self.kisayol = self.kisayol_line.text()
        self.karsilik = self.karsilik_line.text()
        fr = open(self.anadosya, "r", encoding = "utf-8")
        icerik = fr.read().rstrip("\n")
        fr.close()
        f = open(self.anadosya, "w", encoding = "utf-8")
        ekle_icerik = icerik + ekle.format(self.kisayol.strip().translate(lower_map).lower(),self.karsilik.strip())
        f.write(ekle_icerik)
        f.close()

    def kisayol_sil(self, kisaltma, aciklama):
        self.yedekAl()
        with open(self.anadosya, "r", encoding = "utf-8") as f:
            lines = f.readlines()
        with open(self.anadosya, "w", encoding = "utf-8") as f:
            for line in lines:

                if line == '  - trigger: ":{}"\n'.format(kisaltma):
                    continue
                if line == '    replace: "{}"\n'.format(aciklama) or line == '    replace: "{}"'.format(aciklama):
                    continue
                f.write(line)

    def yedekAl(self):
        copy(self.anadosya, self.yedekdosya)
"""

if __name__ == '__main__':
    l = {}
    app = QApplication(sys.argv)
    dialog = Append(l, "default_yedek.yml")
    sys.exit(dialog.exec_())
