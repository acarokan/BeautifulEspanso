from db import DB
from strings import dbfile, drdbfile
from PyQt5.QtWidgets import QTreeWidgetItem

class Dr(QTreeWidgetItem):
    def __init__(self,id,isim,kisaltmalar):
        super().__init__()
        self.id = id
        self.isim = isim
        self.setText(0,isim)
        self.kisaltmalar = kisaltmalar
        self.db = DB(dbfile)

    def get_id(self):
        return self.id

    def get_isim(self):
        return self.isim

    def get_kisaltmalar(self):
        return self.kisaltmalar

    def kisaltma_ekle(self,data):

        self.kisaltmalar.update(data)
        self.db.add_kisaltma_db(self.id, data)

    def kisaltma_sil(self,kisaltma):

        self.kisaltmalar.pop(kisaltma)
        self.db.remove_kisaltma_db(self.id,data)
