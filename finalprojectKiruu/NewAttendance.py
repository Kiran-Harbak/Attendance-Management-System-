from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_newattendance(object):

    def attendenceentryadddetails(self):
        ClassName = self.comboBox.currentText()
        RollNo = self.textEdit.toPlainText()
        Months = self.comboBox_3.currentText()
        TotalLec = self.textEdit_totalLectures.toPlainText()
        AttenLec = self.textEdit_Atteentedlect.toPlainText()

        connection = sqlite3.connect("miniproject.db")
        try:
            sql = """CREATE TABLE IF NOT EXISTS NewAttendance( classNm TEXT,StuRollno INT NOT NULL, Months TEXT NOT NULL, TotalLectures INT NOT NULL, AttendedLectures INT NOT NULL )"""
            connection.execute(sql)
            connection.execute("INSERT INTO NewAttendance VALUES(?,?,?,?,?)", (ClassName, RollNo, Months, TotalLec, AttenLec))
            connection.commit()
            print("New Attendance Added Successfully !")
        except Exception:

            print("Error in AttendenceEntryAddDetails")
        connection.close()

    def setupUi(self, newattendance):
        newattendance.setObjectName("newattendance")
        newattendance.resize(712, 689)
        self.centralwidget = QtWidgets.QWidget(newattendance)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 130, 131, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.frame_newattendance = QtWidgets.QFrame(self.centralwidget)
        self.frame_newattendance.setGeometry(QtCore.QRect(-10, 0, 1261, 1001))
        self.frame_newattendance.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.frame_newattendance.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_newattendance.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_newattendance.setObjectName("frame_newattendance")
        self.comboBox = QtWidgets.QComboBox(self.frame_newattendance)
        self.comboBox.setGeometry(QtCore.QRect(360, 100, 201, 51))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lbl_class = QtWidgets.QLabel(self.frame_newattendance)
        self.lbl_class.setGeometry(QtCore.QRect(70, 100, 191, 41))
        self.lbl_class.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_class.setObjectName("lbl_class")
        self.lbl_Rollno = QtWidgets.QLabel(self.frame_newattendance)
        self.lbl_Rollno.setGeometry(QtCore.QRect(90, 170, 151, 41))
        self.lbl_Rollno.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Rollno.setObjectName("lbl_Rollno")
        self.label_month = QtWidgets.QLabel(self.frame_newattendance)
        self.label_month.setGeometry(QtCore.QRect(120, 240, 91, 41))
        self.label_month.setAlignment(QtCore.Qt.AlignCenter)
        self.label_month.setObjectName("label_month")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_newattendance)
        self.comboBox_3.setGeometry(QtCore.QRect(360, 240, 201, 51))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_Totallec = QtWidgets.QLabel(self.frame_newattendance)
        self.label_Totallec.setGeometry(QtCore.QRect(100, 320, 161, 41))
        self.label_Totallec.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Totallec.setObjectName("label_Totallec")
        self.label_attentedlecture = QtWidgets.QLabel(self.frame_newattendance)
        self.label_attentedlecture.setGeometry(QtCore.QRect(100, 390, 181, 41))
        self.label_attentedlecture.setAlignment(QtCore.Qt.AlignCenter)
        self.label_attentedlecture.setObjectName("label_attentedlecture")
        self.pushButton = QtWidgets.QPushButton(self.frame_newattendance)
        self.pushButton.setGeometry(QtCore.QRect(290, 480, 151, 51))
        self.pushButton.setStyleSheet("font: 75 11pt \"Serif\";\n"
"font: 15pt \"Ubuntu\";")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.frame_newattendance)
        self.textEdit.setGeometry(QtCore.QRect(360, 170, 201, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_totalLectures = QtWidgets.QTextEdit(self.frame_newattendance)
        self.textEdit_totalLectures.setGeometry(QtCore.QRect(360, 310, 201, 51))
        self.textEdit_totalLectures.setObjectName("textEdit_totalLectures")
        self.textEdit_Atteentedlect = QtWidgets.QTextEdit(self.frame_newattendance)
        self.textEdit_Atteentedlect.setGeometry(QtCore.QRect(360, 380, 201, 61))
        self.textEdit_Atteentedlect.setObjectName("textEdit_Atteentedlect")
        self.label_newattendancetitle = QtWidgets.QLabel(self.frame_newattendance)
        self.label_newattendancetitle.setGeometry(QtCore.QRect(200, 30, 291, 41))
        self.label_newattendancetitle.setStyleSheet("font: 75 15pt \"Serif\";\n"
"selection-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.label_newattendancetitle.setObjectName("label_newattendancetitle")
        newattendance.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(newattendance)
        self.statusbar.setObjectName("statusbar")
        newattendance.setStatusBar(self.statusbar)

        self.retranslateUi(newattendance)
        QtCore.QMetaObject.connectSlotsByName(newattendance)

    def retranslateUi(self, newattendance):
        _translate = QtCore.QCoreApplication.translate
        newattendance.setWindowTitle(_translate("newattendance", "MainWindow"))
        self.comboBox.setItemText(0, _translate("newattendance", "Fy"))
        self.comboBox.setItemText(1, _translate("newattendance", "Sy"))
        self.comboBox.setItemText(2, _translate("newattendance", "Ty"))
        self.comboBox.setItemText(3, _translate("newattendance", "BE"))
        self.lbl_class.setText(_translate("newattendance", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Class</span></p></body></html>"))
        self.lbl_Rollno.setText(_translate("newattendance", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Roll No</span></p></body></html>"))
        self.label_month.setText(_translate("newattendance", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Month</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("newattendance", "January"))
        self.comboBox_3.setItemText(1, _translate("newattendance", "February"))
        self.comboBox_3.setItemText(2, _translate("newattendance", "March"))
        self.comboBox_3.setItemText(3, _translate("newattendance", "April"))
        self.comboBox_3.setItemText(4, _translate("newattendance", "May"))
        self.comboBox_3.setItemText(5, _translate("newattendance", "June"))
        self.comboBox_3.setItemText(6, _translate("newattendance", "July"))
        self.comboBox_3.setItemText(7, _translate("newattendance", "August"))
        self.comboBox_3.setItemText(8, _translate("newattendance", "September"))
        self.comboBox_3.setItemText(9, _translate("newattendance", "Octomber"))
        self.comboBox_3.setItemText(10, _translate("newattendance", "November"))
        self.comboBox_3.setItemText(11, _translate("newattendance", "December"))
        self.label_Totallec.setText(_translate("newattendance", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Total Lectures</span></p></body></html>"))
        self.label_attentedlecture.setText(_translate("newattendance", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Attentend Lectures</span></p></body></html>"))

        self.pushButton.setText(_translate("newattendance", "ADD"))
##ADDDDDDDDDD
        self.pushButton.clicked.connect(self.attendenceentryadddetails)
        self.textEdit_totalLectures.setHtml(_translate("newattendance", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">40</p></body></html>"))
        self.label_newattendancetitle.setText(_translate("newattendance", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ef2929;\">NEW ATTENDANCE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    newattendance = QtWidgets.QMainWindow()
    ui = Ui_newattendance()
    ui.setupUi(newattendance)
    newattendance.show()
    sys.exit(app.exec_())

