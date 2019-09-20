from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3

class Ui_Form1(object):
    def generation(self):
        connection = sqlite3.connect("miniproject.db")
        classNm = self.comboBox_reportclass.currentText()
        Subject = self.textEdit_reportsubject.toPlainText()
        Months = self.comboBox_reportmonth.currentText()
        query="select s.StuRollNo,s.firstNm,s.lastNm,s.classNm,n1.Sub_Name,n2.Months,n2.TotalLectures,n2.AttendedLectures from StudentsEntry s Join NewClassEntry n1 on n1.classNm = s.classNm Join NewAttendance n2 on n2.classNm = n1.classNm where n2.classNm ='"+classNm+"' AND n1.Sub_Name ='"+Subject+"' AND n2.Months = '"+Months+"' "

        result = connection.execute(query)
        self.tableWidget_report.setRowCount(0)

        for row_number,row_data in enumerate(result):
            self.tableWidget_report.insertRow(row_number)
            for colum_number,data in enumerate(row_data):
                self.tableWidget_report.setItem(row_number,colum_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1023, 770)
        self.pushButton_reportsearch = QtWidgets.QPushButton(Form)
        self.pushButton_reportsearch.setGeometry(QtCore.QRect(790, 110, 151, 41))
        self.pushButton_reportsearch.setObjectName("pushButton_reportsearch")

        self.pushButton_reportsearch.clicked.connect(self.generation)

        self.comboBox_reportclass = QtWidgets.QComboBox(Form)
        self.comboBox_reportclass.setGeometry(QtCore.QRect(70, 110, 141, 41))
        self.comboBox_reportclass.setObjectName("comboBox_reportclass")
        self.comboBox_reportclass.addItem("")
        self.comboBox_reportclass.addItem("")
        self.comboBox_reportclass.addItem("")
        self.comboBox_reportclass.addItem("")
        self.label_reportclass = QtWidgets.QLabel(Form)
        self.label_reportclass.setGeometry(QtCore.QRect(10, 120, 51, 17))
        self.label_reportclass.setObjectName("label_reportclass")
        self.label_reportsubject = QtWidgets.QLabel(Form)
        self.label_reportsubject.setGeometry(QtCore.QRect(220, 120, 67, 17))
        self.label_reportsubject.setObjectName("label_reportsubject")
        self.textEdit_reportsubject = QtWidgets.QTextEdit(Form)
        self.textEdit_reportsubject.setGeometry(QtCore.QRect(290, 110, 181, 41))
        self.textEdit_reportsubject.setObjectName("textEdit_reportsubject")
        self.label_reportmonth = QtWidgets.QLabel(Form)
        self.label_reportmonth.setGeometry(QtCore.QRect(510, 120, 67, 17))
        self.label_reportmonth.setObjectName("label_reportmonth")
        self.comboBox_reportmonth = QtWidgets.QComboBox(Form)
        self.comboBox_reportmonth.setGeometry(QtCore.QRect(590, 110, 141, 41))
        self.comboBox_reportmonth.setObjectName("comboBox_reportmonth")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.comboBox_reportmonth.addItem("")
        self.label_reporttitle = QtWidgets.QLabel(Form)
        self.label_reporttitle.setGeometry(QtCore.QRect(330, 16, 301, 61))
        self.label_reporttitle.setObjectName("label_reporttitle")
        self.tableWidget_report = QtWidgets.QTableWidget(Form)
        self.tableWidget_report.setGeometry(QtCore.QRect(10, 210, 941, 461))
        self.tableWidget_report.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: rgb(0, 0, 0);")
        self.tableWidget_report.setRowCount(5)
        self.tableWidget_report.setColumnCount(8)
        self.tableWidget_report.setObjectName("tableWidget_report")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_reportsearch.setText(_translate("Form", "Search"))
        self.comboBox_reportclass.setItemText(0, _translate("Form", "Fy"))
        self.comboBox_reportclass.setItemText(1, _translate("Form", "Sy"))
        self.comboBox_reportclass.setItemText(2, _translate("Form", "Ty"))
        self.comboBox_reportclass.setItemText(3, _translate("Form", "BE"))
        self.label_reportclass.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Class</span></p></body></html>"))
        self.label_reportsubject.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Subject</span></p></body></html>"))
        self.label_reportmonth.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Month</span></p></body></html>"))
        self.comboBox_reportmonth.setItemText(0, _translate("Form", "January"))
        self.comboBox_reportmonth.setItemText(1, _translate("Form", "February"))
        self.comboBox_reportmonth.setItemText(2, _translate("Form", "March"))
        self.comboBox_reportmonth.setItemText(3, _translate("Form", "April"))
        self.comboBox_reportmonth.setItemText(4, _translate("Form", "May"))
        self.comboBox_reportmonth.setItemText(5, _translate("Form", "June"))
        self.comboBox_reportmonth.setItemText(6, _translate("Form", "July"))
        self.comboBox_reportmonth.setItemText(7, _translate("Form", "August"))
        self.comboBox_reportmonth.setItemText(8, _translate("Form", "September"))
        self.comboBox_reportmonth.setItemText(9, _translate("Form", "November"))
        self.comboBox_reportmonth.setItemText(10, _translate("Form", "December"))
        self.label_reporttitle.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ef2929;\">Report Generation</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
