# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_files\error_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorWindow(object):
    def setupUi(self, errorWindow):
        errorWindow.setObjectName("errorWindow")
        errorWindow.resize(365, 132)
        self.gridLayout_2 = QtWidgets.QGridLayout(errorWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(errorWindow)
        self.label.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(errorWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(errorWindow)
        QtCore.QMetaObject.connectSlotsByName(errorWindow)

    def retranslateUi(self, errorWindow):
        _translate = QtCore.QCoreApplication.translate
        errorWindow.setWindowTitle(_translate("errorWindow", "????????????????????????!"))
        self.label.setText(_translate("errorWindow", "TextLabel"))
        self.pushButton.setText(_translate("errorWindow", "????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    errorWindow = QtWidgets.QDialog()
    ui = Ui_errorWindow()
    ui.setupUi(errorWindow)
    errorWindow.show()
    sys.exit(app.exec_())
