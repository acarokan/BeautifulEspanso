from PyQt5.QtWidgets import QMessageBox

class CheckSure(QMessageBox):
    def __init__(self,parent,title,text):
        super().__init__()
        self.parent = parent
        self.title = title
        self.text = text

    def close_event(self):
        cevap = self.question(self.parent,self.title,self.text,QMessageBox.Yes, QMessageBox.No)
        return cevap
