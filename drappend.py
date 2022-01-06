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


class DrAppend(QDialog):
    def __init__(self,id):
        super().__init__()
        self.id = id
        self.dr_isim = ""
        self.dbobject = DB("db.json")
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.accepted.connect(self.dr_ekle)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Espanso ekle")
        layout = QtWidgets.QFormLayout()
        self.dr_isim_line = QLineEdit()
        self.karsilik_line = QLineEdit()
        layout.addRow(QLabel("Dr İsmi:"), self.dr_isim_line)
        self.formGroupBox.setLayout(layout)

    def dr_ekle(self):
        self.dr_isim = self.dr_isim_line.text().strip().translate(lower_map).lower()
        data = {"isim": self.dr_isim,
                "kisaltmalar": {}}
        self.dbobject.add_dr_db(data)

    def kisayol_sil(self, kisaltma):
        del self.list[kisaltma]
