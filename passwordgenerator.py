# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
import pyperclip
import os

uppercase_letters = ("A", "B", "C", "D", "E", "F", "G", "H",
                     "I", "J", "K", "L", "M", "N", "O", "P",
                     "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")

lowercase_letters = ("a", "b", "c", "d", "e", "f", "g", "h",
                     "i", "j", "k", "l", "m", "n", "o", "p",
                     "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
special_characters = ("!", "@", "#", "$", "%", "^", "&", "*", "?")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(331, 196)
        MainWindow.setMinimumSize(QtCore.QSize(331, 196))
        MainWindow.setMaximumSize(QtCore.QSize(331, 196))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(9.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.letters_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.letters_checkbox.setEnabled(True)
        self.letters_checkbox.setGeometry(QtCore.QRect(100, 10, 61, 16))
        self.letters_checkbox.setObjectName("letters_checkbox")
        self.letters_checkbox.toggled.connect(self.enableOptions)
        self.numbers_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.numbers_checkbox.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.numbers_checkbox.setObjectName("numbers_checkbox")
        self.numbers_checkbox.list = numbers
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(160, 10, 120, 61))
        self.groupBox.setObjectName("groupBox")
        self.uppercase_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.uppercase_checkbox.setEnabled(False)
        self.uppercase_checkbox.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.uppercase_checkbox.setObjectName("uppercase_checkbox")
        self.uppercase_checkbox.list = uppercase_letters
        self.lowercase_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.lowercase_checkbox.setEnabled(False)
        self.lowercase_checkbox.setGeometry(QtCore.QRect(20, 40, 81, 17))
        self.lowercase_checkbox.setObjectName("lowercase_checkbox")
        self.lowercase_checkbox.list = lowercase_letters
        self.specialch_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.specialch_checkbox.setGeometry(QtCore.QRect(20, 40, 111, 17))
        self.specialch_checkbox.setObjectName("specialch_checkbox")
        self.specialch_checkbox.list = special_characters
        self.len_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.len_spinbox.setGeometry(QtCore.QRect(110, 70, 41, 21))
        self.len_spinbox.setSpecialValueText("")
        self.len_spinbox.setMinimum(1)
        self.len_spinbox.setMaximum(20)
        self.len_spinbox.setObjectName("len_spinbox")
        self.passlen_label = QtWidgets.QLabel(self.centralwidget)
        self.passlen_label.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.passlen_label.setObjectName("passlen_label")
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setGeometry(QtCore.QRect(180, 80, 141, 31))
        self.generate_button.setObjectName("generate_button")
        self.generate_button.clicked.connect(self.generatePassword)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 140, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.copyButton = QtWidgets.QPushButton(self.centralwidget)
        self.copyButton.setGeometry(QtCore.QRect(20, 110, 111, 23))
        self.copyButton.setCheckable(False)
        self.copyButton.setObjectName("copyButton")
        self.copyButton.clicked.connect(self.clipCopy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.checks = [self.uppercase_checkbox, self.lowercase_checkbox,
                       self.numbers_checkbox, self.specialch_checkbox]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Password Generator"))
        self.letters_checkbox.setText(_translate("MainWindow", "Letters"))
        self.numbers_checkbox.setText(_translate("MainWindow", "Numbers"))
        self.groupBox.setTitle(_translate("MainWindow", "Letters Options"))
        self.uppercase_checkbox.setText(_translate("MainWindow", "Uppercase"))
        self.lowercase_checkbox.setText(_translate("MainWindow", "Lowercase"))
        self.specialch_checkbox.setText(
            _translate("MainWindow", "Special characters"))
        self.passlen_label.setText(_translate(
            "MainWindow", "Password Length:"))
        self.generate_button.setText(
            _translate("MainWindow", "Generate Password"))
        self.lineEdit.setText(_translate("MainWindow", "PASSWORD"))
        self.copyButton.setText(_translate("MainWindow", "Copy to clipboard"))

    def enableOptions(self, MainWindow):
        if self.letters_checkbox.isChecked():
            self.uppercase_checkbox.setEnabled(True)
            self.lowercase_checkbox.setEnabled(True)
        else:
            self.uppercase_checkbox.setEnabled(False)
            self.lowercase_checkbox.setEnabled(False)
            self.uppercase_checkbox.setChecked(False)
            self.lowercase_checkbox.setChecked(False)

    def generatePassword(self, MainWindow):
        global txt
        txt = ""
        truetypes = []
        if (self.uppercase_checkbox.isChecked() == False and self.lowercase_checkbox.isChecked() == False and self.numbers_checkbox.isChecked() == False and self.specialch_checkbox.isChecked() == False):
            QtWidgets.QMessageBox.about(
                self.MainWindow, "Warning", "You need to choose at least one character type!")
        else:
            for chartype in self.checks:
                if chartype.isChecked():
                    truetypes.append(chartype.list)
            for _ in range(self.len_spinbox.value()):
                txt += random.choice(random.choice(truetypes))
            self.lineEdit.setText(txt)

    def clipCopy(self, MainWindow):
        if self.lineEdit.text() == "PASSWORD":
            pyperclip.copy("")
        else:
            pyperclip.copy(txt)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
