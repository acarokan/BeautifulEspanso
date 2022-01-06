from PyQt5.QtWidgets import QMessageBox

class ErrorMessage(QMessageBox):
    def __init__(self, tip, mesaj, baslik):
        super().__init__(tip, mesaj, baslik)
        self.tip = tip
        self.mesaj = mesaj
        self.baslik = baslik
        self.setup()

    def setup(self):
        self.setIcon(self.tip)
        self.setText(self.mesaj)
        self.setWindowTitle(self.baslik)
        self.exec_()
