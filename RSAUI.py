from pydoc import plain
import time
import sys, os

import RSA
from os import curdir, environ
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QTabWidget, QWidget, QMessageBox, QPushButton, QFileDialog, QVBoxLayout

class RSAEnc(QDialog):
    e,N = 0,0
    
    def __init__(self):
        super(RSAEnc, self).__init__()
        loadUi("RSAEnc.ui", self)
        self.decrypt.clicked.connect(self.gotoRSADec)
        self.genKey.clicked.connect(self.gotoGenKey)
        self.selectencrypt.clicked.connect(self.encrypting)
        self.selectkey.clicked.connect(self.selectPubKey)
        self.savecipher.clicked.connect(self.saveCipher)

    def gotoGenKey(self):
        genKeyPair = RSAGenKey()
        widget.addWidget(genKeyPair)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def selectPubKey(self):
            self.warn_red.setText("")
            self.warn_green.setText("")
            option=QFileDialog.Options()
            file = QFileDialog.getOpenFileName(widget,"Open Public Key","Default File","*.pub",options=option)
            
            if file[0] != '':
                tuples = open(file[0],'r')
                publicKey = tuples.read()
                tuples.close()

                e,N = RSA.unpackKeyTuples(publicKey)
                
                self.e = e
                self.N = N
                
            self.key.setWordWrap(True)
            self.key.setText(file[0])

    def encrypting(self):
        if self.key.text() != "":
            self.warn_red.setText("")
            self.warn_green.setText("")
            option=QFileDialog.Options()
            file = QFileDialog.getOpenFileName(widget,"Open file to encrypt","Default File","All Files (*)",options=option)
            if file[0] != '':
                cipher, etime = RSA.encryptFile(file[0],self.N,self.e)
                
                cipherHex = RSA.toHex(cipher)
                self.file.setText(cipherHex)
                self.time.setWordWrap(True)
                self.time.setText(str(round(etime,4))+" S")
                self.size.setWordWrap(True)
                self.size.setText(str(RSA.showFileSize("encrypted")) + " B")
        else:
            self.warn_red.setText("Select public key First!")
    
    def gotoRSADec(self):
        RSADecr = RSADec()
        widget.addWidget(RSADecr)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def saveCipher(self):
        if len(self.file.toPlainText()) != 0:
            self.warn_red.setText("")
            option=QFileDialog.Options()
            option|=QFileDialog.DontUseNativeDialog

            file=QFileDialog.getSaveFileName(widget,"Save Encryption","cipherResult.txt","All Files (*)",options=option)
            
            if file[0] != '':
                file1 = open(file[0], "w",encoding="utf-8")
                file2 = open("encrypted","r",encoding="utf-8")
                cipher = file2.read()
                file1.write(cipher)
                file1.close()
                file2.close()
                self.warn_green.setText("File has been saved !")
        else:
            self.warn_red.setText("Select file first !")

       

class RSADec(QDialog):
    d,N = 0,0

    def __init__(self):
        super(RSADec, self).__init__()
        loadUi("RSADec.ui", self)
        self.encrypt.clicked.connect(self.gotoRSAEnc)
        self.selectfile.clicked.connect(self.decrypting)
        self.genKey.clicked.connect(self.gotoGenKey)
        self.selectkey.clicked.connect(self.selectPriKey)
        self.saveplain.clicked.connect(self.savePlain)

    def savePlain(self):
        if len(self.file.toPlainText()) != 0:
            self.warn_red.setText("")
            option=QFileDialog.Options()
            option|=QFileDialog.DontUseNativeDialog

            file=QFileDialog.getSaveFileName(widget,"Save Result","plainResult.txt","All Files (*)",options=option)
            
            if file[0] != '':
                if file[0].endswith('.txt'):
                    file1 = open(file[0], "w",encoding="utf-8")
                    file2 = open("decrypted","r",encoding="utf-8")
                    cipher = file2.read()
                    file1.write(cipher)
                    file1.close()
                    file2.close()
                else:
                    file1 = open(file[0], "wb")
                    file2 = open("decrypted","rb")
                    cipher = file2.read()
                    file1.write(cipher)
                    file1.close()
                    file2.close()
                self.warn_green.setText("File has been saved !")
        else:
            self.warn_red.setText("Select file first !")

    def selectPriKey(self):
            self.warn_red.setText("")
            self.warn_green.setText("")
            option=QFileDialog.Options()
            file = QFileDialog.getOpenFileName(widget,"Open Private Key","Default File","*.pri",options=option)
            
            if file[0] != '':
                tuples = open(file[0],'r')
                privateKey = tuples.read()
                tuples.close()

                d,N = RSA.unpackKeyTuples(privateKey)
                
                
                self.d = d
                self.N = N
                print(self.d,self.N)

            self.key.setWordWrap(True)
            self.key.setText(file[0])

    def gotoRSAEnc(self):
        RSAEncr = RSAEnc()
        widget.addWidget(RSAEncr)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def decrypting(self):
        if self.key.text() != "":
            self.warn_red.setText("")
            self.warn_green.setText("")
            option=QFileDialog.Options()
            file = QFileDialog.getOpenFileName(widget,"Open file to encrypt","Default File","All Files (*)",options=option)
            if file[0] != '':
                if file[0].endswith('.txt'):
                    plain, dtime = RSA.decryptFile(file[0],self.d,self.N)
                    # print(file[0])
                    text = ''
                    for idx in plain:
                        text += idx

                    self.file.setText(text)
                    self.time.setWordWrap(True)
                    self.time.setText(str(round(dtime,4))+" S")
                    self.size.setWordWrap(True)
                    self.size.setText(str(RSA.showFileSize("encrypted")) + " B")
                else:
                    plain, dtime = RSA.decryptFile(file[0],self.d,self.N)
                    text = ''
                    for idx in plain:
                        text += idx
                    self.file.setText(text)
                    for i, value in enumerate(plain):
                        plain[i] = ord(value)
                    byteplain = bytearray(plain)
                    file = open("decrypted",'wb')
                    file.write(byteplain)
                    file.close()
                    self.time.setWordWrap(True)
                    self.time.setText(str(round(dtime,4))+" S")
                    self.size.setWordWrap(True)
                    self.size.setText(str(RSA.showFileSize("encrypted")) + " B")          
        else:
            self.warn_red.setText("Select private key First!")
    
    def gotoGenKey(self):
        genKeyPair = RSAGenKey()
        widget.addWidget(genKeyPair)
        widget.setCurrentIndex(widget.currentIndex()+1)

    

class RSAGenKey(QDialog):
    def __init__(self):
        super(RSAGenKey, self).__init__()
        loadUi("RSAGenKey.ui", self)
        self.encrypt.clicked.connect(self.gotoRSAEnc)
        self.decrypt.clicked.connect(self.gotoRSADec)
        self.genKey.clicked.connect(self.genKeyPair)
        self.savePri.clicked.connect(self.savePriKey)
        self.savePub.clicked.connect(self.savePubKey)

    def savePubKey(self):
        if len(self.N.text()) != 0:
            option=QFileDialog.Options()
            option|=QFileDialog.DontUseNativeDialog

            file=QFileDialog.getSaveFileName(widget,"Save File Window Title","publicKey.pub","*.pub",options=option)
            
            if file[0] != '':
                file = open(file[0], "w",encoding="utf-8")
                file.write('(' + self.e.text() + ',' + self.N.text() + ')')
                file.close()

    def savePriKey(self):
        if len(self.N.text()) != 0:
            option=QFileDialog.Options()
            option|=QFileDialog.DontUseNativeDialog

            file=QFileDialog.getSaveFileName(widget,"Save File Window Title","privateKey.pri","*.pri",options=option)
            if file[0] != '':
                file = open(file[0], "w",encoding="utf-8")
                file.write('(' + self.d.text() + ',' + self.N.text() + ')')
                file.close()

    def genKeyPair(self):
        pubKey, privKey = RSA.generatePairKey()
        e,N = pubKey
        d,N = privKey 

        self.e.setText(str(e))
        self.d.setText(str(d))
        self.N.setText(str(N))

    def gotoRSAEnc(self):
        RSAEncr = RSAEnc()
        widget.addWidget(RSAEncr) 
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotoRSADec(self):
        RSADecr = RSADec()
        widget.addWidget(RSADecr)
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