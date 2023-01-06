# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'case_record_file.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CardFile(object):
    def setupUi(self, CardFile):
        CardFile.setObjectName("CardFile")
        CardFile.resize(760, 839)
        self.centralwidget = QtWidgets.QWidget(CardFile)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9_3.setFont(font)
        self.label_9_3.setObjectName("label_9_3")
        self.horizontalLayout_2.addWidget(self.label_9_3)
        self.pat_name_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pat_name_3.setFont(font)
        self.pat_name_3.setText("")
        self.pat_name_3.setObjectName("pat_name_3")
        self.horizontalLayout_2.addWidget(self.pat_name_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(150, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3_3.setFont(font)
        self.label_3_3.setObjectName("label_3_3")
        self.horizontalLayout.addWidget(self.label_3_3)
        self.house_number_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.house_number_3.setMinimumSize(QtCore.QSize(1, 0))
        self.house_number_3.setMaximumSize(QtCore.QSize(30, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.house_number_3.setFont(font)
        self.house_number_3.setObjectName("house_number_3")
        self.horizontalLayout.addWidget(self.house_number_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4_3.setFont(font)
        self.label_4_3.setObjectName("label_4_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4_3)
        self.affiliation_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.affiliation_3.setFont(font)
        self.affiliation_3.setObjectName("affiliation_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.affiliation_3)
        self.gridLayout_2.addLayout(self.formLayout_2, 1, 1, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5_3.setFont(font)
        self.label_5_3.setObjectName("label_5_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5_3)
        self.manager_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.manager_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.manager_3.setFont(font)
        self.manager_3.setObjectName("manager_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.manager_3)
        self.gridLayout_2.addLayout(self.formLayout, 2, 1, 1, 2)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.add_to_diag_Button_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.add_to_diag_Button_3.setFont(font)
        self.add_to_diag_Button_3.setObjectName("add_to_diag_Button_3")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.add_to_diag_Button_3)
        self.tableWidget_diag_file = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget_diag_file.setFont(font)
        self.tableWidget_diag_file.setObjectName("tableWidget_diag_file")
        self.tableWidget_diag_file.setColumnCount(4)
        self.tableWidget_diag_file.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_diag_file.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_diag_file.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_diag_file.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_diag_file.setHorizontalHeaderItem(3, item)
        self.tableWidget_diag_file.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget_diag_file.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_diag_file.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_diag_file.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_diag_file.verticalHeader().setMinimumSectionSize(24)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.tableWidget_diag_file)
        self.gridLayout_2.addLayout(self.formLayout_4, 4, 0, 1, 3)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.comboBox_streets_3 = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_streets_3.setFont(font)
        self.comboBox_streets_3.setObjectName("comboBox_streets_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.comboBox_streets_3)
        self.street_name_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.street_name_3.setFont(font)
        self.street_name_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.street_name_3.setMouseTracking(True)
        self.street_name_3.setText("")
        self.street_name_3.setObjectName("street_name_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.street_name_3)
        self.gridLayout_2.addLayout(self.formLayout_3, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.add_to_cardButton = QtWidgets.QPushButton(self.centralwidget)
        self.add_to_cardButton.setMinimumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_to_cardButton.setFont(font)
        self.add_to_cardButton.setObjectName("add_to_cardButton")
        self.gridLayout_3.addWidget(self.add_to_cardButton, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 1, 1, 1)
        self.curd_numberBox = QtWidgets.QSpinBox(self.centralwidget)
        self.curd_numberBox.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.curd_numberBox.setFont(font)
        self.curd_numberBox.setMinimum(1)
        self.curd_numberBox.setMaximum(10000)
        self.curd_numberBox.setObjectName("curd_numberBox")
        self.gridLayout_3.addWidget(self.curd_numberBox, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 2, 3, 1, 1)
        self.error = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.error.setFont(font)
        self.error.setStyleSheet("color: rgb(255, 0, 0);")
        self.error.setObjectName("error")
        self.gridLayout_3.addWidget(self.error, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 7, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.mobile_2_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mobile_2_3.setFont(font)
        self.mobile_2_3.setObjectName("mobile_2_3")
        self.gridLayout.addWidget(self.mobile_2_3, 1, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.label_8_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8_3.setFont(font)
        self.label_8_3.setObjectName("label_8_3")
        self.gridLayout.addWidget(self.label_8_3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 1, 1, 1)
        self.label_6_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6_3.setFont(font)
        self.label_6_3.setObjectName("label_6_3")
        self.gridLayout.addWidget(self.label_6_3, 0, 3, 1, 1)
        self.mobile_1_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.mobile_1_3.setFont(font)
        self.mobile_1_3.setText("")
        self.mobile_1_3.setObjectName("mobile_1_3")
        self.gridLayout.addWidget(self.mobile_1_3, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        self.label_7_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7_3.setFont(font)
        self.label_7_3.setObjectName("label_7_3")
        self.gridLayout.addWidget(self.label_7_3, 0, 5, 1, 1)
        self.home_phone_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.home_phone_3.setFont(font)
        self.home_phone_3.setObjectName("home_phone_3")
        self.gridLayout.addWidget(self.home_phone_3, 1, 6, 1, 1)
        self.work_phone_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.work_phone_3.setFont(font)
        self.work_phone_3.setText("")
        self.work_phone_3.setObjectName("work_phone_3")
        self.gridLayout.addWidget(self.work_phone_3, 0, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_2_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2_3.setFont(font)
        self.label_2_3.setStyleSheet("background-color: rgb(234, 255, 205);")
        self.label_2_3.setObjectName("label_2_3")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_8.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.verticalLayout.addLayout(self.formLayout_8)
        self.general_chatacteristics_3 = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.general_chatacteristics_3.setFont(font)
        self.general_chatacteristics_3.setMouseTracking(False)
        self.general_chatacteristics_3.setObjectName("general_chatacteristics_3")
        self.verticalLayout.addWidget(self.general_chatacteristics_3)
        self.gridLayout_2.addLayout(self.verticalLayout, 3, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 6, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 7, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 5, 1, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setHorizontalSpacing(28)
        self.formLayout_6.setObjectName("formLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_6.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout_6.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem11)
        self.saveButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton_3.setMinimumSize(QtCore.QSize(200, 30))
        self.saveButton_3.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveButton_3.setFont(font)
        self.saveButton_3.setObjectName("saveButton_3")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.saveButton_3)
        self.gridLayout_2.addLayout(self.formLayout_6, 7, 2, 1, 1)
        CardFile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CardFile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 21))
        self.menubar.setObjectName("menubar")
        CardFile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CardFile)
        self.statusbar.setObjectName("statusbar")
        CardFile.setStatusBar(self.statusbar)

        self.retranslateUi(CardFile)
        QtCore.QMetaObject.connectSlotsByName(CardFile)

    def retranslateUi(self, CardFile):
        _translate = QtCore.QCoreApplication.translate
        CardFile.setWindowTitle(_translate("CardFile", "MainWindow"))
        self.label_9_3.setText(_translate("CardFile", "Пацієнт"))
        self.label_3_3.setText(_translate("CardFile", "Будинок №"))
        self.label_4_3.setText(_translate("CardFile", "Приналежність"))
        self.label_5_3.setText(_translate("CardFile", "Керівник"))
        self.add_to_diag_Button_3.setText(_translate("CardFile", "+"))
        item = self.tableWidget_diag_file.horizontalHeaderItem(0)
        item.setText(_translate("CardFile", "Дата"))
        item = self.tableWidget_diag_file.horizontalHeaderItem(1)
        item.setText(_translate("CardFile", "кв."))
        item = self.tableWidget_diag_file.horizontalHeaderItem(2)
        item.setText(_translate("CardFile", "Паціент"))
        item = self.tableWidget_diag_file.horizontalHeaderItem(3)
        item.setText(_translate("CardFile", "Діагноз"))
        self.add_to_cardButton.setText(_translate("CardFile", "Дадати до картки"))
        self.label_10.setText(_translate("CardFile", "№"))
        self.error.setText(_translate("CardFile", "TextLabel"))
        self.label_8_3.setText(_translate("CardFile", "Д.М."))
        self.label_6_3.setText(_translate("CardFile", "моб."))
        self.label_7_3.setText(_translate("CardFile", "Р.Т."))
        self.label_2_3.setText(_translate("CardFile", "Загальна характеристика"))
        self.general_chatacteristics_3.setHtml(_translate("CardFile", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.saveButton_3.setText(_translate("CardFile", "Зберегти у картотеку"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardFile = QtWidgets.QMainWindow()
    ui = Ui_CardFile()
    ui.setupUi(CardFile)
    CardFile.show()
    sys.exit(app.exec_())