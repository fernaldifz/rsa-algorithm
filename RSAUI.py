from pydoc import plain
import time
import sys
import RSA
from os import curdir, environ
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QTabWidget, QWidget, QMessageBox, QPushButton, QFileDialog, QVBoxLayout

class RSAEnc(QDialog):
    def __init__(self):
        super(RSAEnc, self).__init__()
        loadUi("RSAEnc.ui", self)
        self.decrypt.clicked.connect(self.gotoRSADec)
        self.encrypt.clicked.connect(self.encrypting)
        self.savecipher.clicked.connect(self.saveCipher)
        self.selectfile.clicked.connect(self.openFileToEncrypt)

    def encrypting(self):
        self.file.setText("")
        plaintext = self.plaintext.toPlainText()
        key = self.key.toPlainText()
        if self.key.toPlainText() != "":
            cipher = RSA.encryptFile()
        self.ciphertext.setText(cipher)

    def gotoRSADec(self):
        RSADec = RSADec()
        widget.addWidget(RSADec)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def saveCipher(self):
        if len(self.ciphertext.toPlainText()) != 0:
            option=QFileDialog.Options()
            option|=QFileDialog.DontUseNativeDialog

            file=QFileDialog.getSaveFileName(widget,"Save File Window Title","default.txt","All Files (*)",options=option)
            file = open(file[0], "w",encoding="utf-8")
            file.write(self.ciphertext.toPlainText())
            file.close()

    def openFileToEncrypt(self):
        if len(self.key.toPlainText()) != 0:
            self.warning.setText("")
            option=QFileDialog.Options()
            file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File","All Files(*)",options=option)
            path = file[0]
            data = RC4Modified.encryptFiles(self.key.toPlainText(), path)
            file=QFileDialog.getSaveFileName(widget,"Save File Window Title","default.txt","All Files (*)",options=option)
            file = open(file[0], "wb")
            file.write(data)
            file.close()
            self.file.setText("file \n has been \n encrypted!")
            
        else:
            self.warning.setText("decide the \nkey first!")
       

class RSADec(QDialog):
    def __init__(self):
        super(RSADec, self).__init__()
        loadUi("RSADec.ui", self)
        self.encrypt.clicked.connect(self.gotoRSAEnc)
        self.decrypt.clicked.connect(self.decrypting)
        self.selectfile.clicked.connect(self.openFileToDecrypt)

    def gotoRSAEnc(self):
        RSAEnc = RSAEnc()
        widget.addWidget(RSAEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def decrypting(self):
        self.file.setText("")
        ciphertext = self.ciphertext.toPlainText()
        key = self.key.toPlainText()
        plaintext = RC4Modified.decrypt(key, ciphertext)
        self.plaintext.setText(plaintext)

    def openFileToDecrypt(self):
        if len(self.key.toPlainText()) != 0:
            self.warning.setText("")
            option=QFileDialog.Options()
            file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File","All Files(*)",options=option)
            path = file[0]
            data = RC4Modified.decryptFiles(self.key.toPlainText(), path)
            file=QFileDialog.getSaveFileName(widget,"Save File Window Title","default.txt","All Files (*)",options=option)
            file = open(file[0], "wb")
            file.write(data)
            file.close()
            self.file.setText("file \n has been \n decrypted!")
            
        else:
            self.warning.setText("decide the \nkey first!")

class RSAGenKey(QDialog):
    def __init__(self):
        super(RSAGenKey, self).__init__()
        loadUi("RSAGenKey.ui", self)
        self.encrypt.clicked.connect(self.gotoRSAEnc)
        self.decrypt.clicked.connect(self.gotoRSADec)
        self.genKey.clicked.connect(self.genKeyPair)


    def genKeyPair(self):
        pubKey, privKey = RSA.generatePairKey()
        e,N = pubKey
        d,N = privKey

        self.e.setText("   " + str(e))
        self.d.setText("   " + str(d))
        self.N.setText("   " + str(N))

    def gotoRSAEnc(self):
        RSAEnc = RSAEnc()
        widget.addWidget(RSAEnc)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoRSADec(self):
        RSADec = RSADec()
        widget.addWidget(RSADec)
        widget.setCurrentIndex(widget.currentIndex()+1)

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def run():
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")

suppress_qt_warnings()
app = QApplication(sys.argv)
menu = RSAGenKey()
widget = QtWidgets.QStackedWidget()
widget.addWidget(menu)
widget.setFixedHeight(512)
widget.setFixedWidth(720)

run()