import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import steg
import szyfr


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("gui.ui", self)
        self.btn_plik_ukr.clicked.connect(self.browsefiles)
        self.btn_ukr.clicked.connect(self.ukryj)
        self.btn_plik_odcz.clicked.connect(self.browsefiles2)
        self.btn_odcz.clicked.connect(self.odczytaj)

    def browsefiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:\pictures', 'Images (*.png *.jpg)')
        self.lbl_inf_ukr.setText(fname[0])

    def browsefiles2(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'J:\PROGRAMOWANIE\Python_all\Steganography',
                                            'Images (*.png *.jpg)')
        self.lbl_inf_ukr.setText(fname[0])

    def ukryj(self):
        taken_text = self.tb_ukr.text()
        check = self.cb_alg_ukr.isChecked()
        if check:
            text_to_hide = szyfr.szyfr(taken_text)
        else:
            text_to_hide = taken_text
        fname = self.lbl_inf_ukr.text()
        steg.Encode(fname, text_to_hide, "encoded.png")
        self.lbl_inf_ukr.setText("Ukryto wiadomość")

    def odczytaj(self):
        fname = self.lbl_inf_ukr.text()
        decoded = steg.Decode(fname)
        self.lbl_inf_ukr.setText("Odkryto wiadomość")
        self.txt_browser.setText(decoded)


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(822)
widget.setFixedHeight(299)
widget.show()

if __name__ == '__main__':
    widget.show()
    sys.exit(app.exec_())
