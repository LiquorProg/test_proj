# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnosis_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_view_diag(object):
    def setupUi(self, Dialog_view_diag):
        Dialog_view_diag.setObjectName("Dialog_view_diag")
        Dialog_view_diag.resize(499, 259)
        Dialog_view_diag.setMinimumSize(QtCore.QSize(0, 0))
        self.formLayout_2 = QtWidgets.QFormLayout(Dialog_view_diag)
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.apart_view_diag = QtWidgets.QLineEdit(Dialog_view_diag)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.apart_view_diag.setFont(font)
        self.apart_view_diag.setObjectName("apart_view_diag")
        self.gridLayout.addWidget(self.apart_view_diag, 1, 1, 1, 1)
        self.label_10_view = QtWidgets.QLabel(Dialog_view_diag)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10_view.setFont(font)
        self.label_10_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10_view.setStyleSheet("")
        self.label_10_view.setTextFormat(QtCore.Qt.PlainText)
        self.label_10_view.setObjectName("label_10_view")
        self.gridLayout.addWidget(self.label_10_view, 0, 0, 1, 1)
        self.label_12_view = QtWidgets.QLabel(Dialog_view_diag)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12_view.setFont(font)
        self.label_12_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12_view.setTextFormat(QtCore.Qt.PlainText)
        self.label_12_view.setObjectName("label_12_view")
        self.gridLayout.addWidget(self.label_12_view, 2, 0, 1, 1)
        self.patient_view_diag = QtWidgets.QLineEdit(Dialog_view_diag)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.patient_view_diag.setFont(font)
        self.patient_view_diag.setObjectName("patient_view_diag")
        self.gridLayout.addWidget(self.patient_view_diag, 2, 1, 1, 1)
        self.dateEdit_view_diag = QtWidgets.QDateEdit(Dialog_view_diag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_view_diag.sizePolicy().hasHeightForWidth())
        self.dateEdit_view_diag.setSizePolicy(sizePolicy)
        self.dateEdit_view_diag.setMinimumSize(QtCore.QSize(142, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_view_diag.setFont(font)
        self.dateEdit_view_diag.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit_view_diag.setObjectName("dateEdit_view_diag")
        self.gridLayout.addWidget(self.dateEdit_view_diag, 0, 1, 1, 1)
        self.label_11_view = QtWidgets.QLabel(Dialog_view_diag)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11_view.setFont(font)
        self.label_11_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11_view.setTextFormat(QtCore.Qt.PlainText)
        self.label_11_view.setObjectName("label_11_view")
        self.gridLayout.addWidget(self.label_11_view, 1, 0, 1, 1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.gridLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_13_view = QtWidgets.QLabel(Dialog_view_diag)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13_view.setFont(font)
        self.label_13_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13_view.setTextFormat(QtCore.Qt.PlainText)
        self.label_13_view.setObjectName("label_13_view")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13_view)
        self.diagnosis_view_diag = QtWidgets.QTextEdit(Dialog_view_diag)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.diagnosis_view_diag.setFont(font)
        self.diagnosis_view_diag.setObjectName("diagnosis_view_diag")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.diagnosis_view_diag)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.editButton_view = QtWidgets.QPushButton(Dialog_view_diag)
        self.editButton_view.setMinimumSize(QtCore.QSize(100, 0))
        self.editButton_view.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.editButton_view.setFont(font)
        self.editButton_view.setObjectName("editButton_view")
        self.horizontalLayout.addWidget(self.editButton_view)
        self.saveButton_view = QtWidgets.QPushButton(Dialog_view_diag)
        self.saveButton_view.setMinimumSize(QtCore.QSize(100, 0))
        self.saveButton_view.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.saveButton_view.setFont(font)
        self.saveButton_view.setObjectName("saveButton_view")
        self.horizontalLayout.addWidget(self.saveButton_view)
        self.formLayout_2.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(Dialog_view_diag)
        QtCore.QMetaObject.connectSlotsByName(Dialog_view_diag)

    def retranslateUi(self, Dialog_view_diag):
        _translate = QtCore.QCoreApplication.translate
        Dialog_view_diag.setWindowTitle(_translate("Dialog_view_diag", "Dialog"))
        self.label_10_view.setText(_translate("Dialog_view_diag", "Дата"))
        self.label_12_view.setText(_translate("Dialog_view_diag", "Пацієнт"))
        self.label_11_view.setText(_translate("Dialog_view_diag", "кв."))
        self.label_13_view.setText(_translate("Dialog_view_diag", "Діагноз"))
        self.editButton_view.setText(_translate("Dialog_view_diag", "Редагувати"))
        self.saveButton_view.setText(_translate("Dialog_view_diag", "Зберегти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_view_diag = QtWidgets.QDialog()
    ui = Ui_Dialog_view_diag()
    ui.setupUi(Dialog_view_diag)
    Dialog_view_diag.show()
    sys.exit(app.exec_())
