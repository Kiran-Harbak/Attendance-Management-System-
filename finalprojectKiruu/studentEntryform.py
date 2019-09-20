from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_StudentEntry(object):

    def studententryadddetails(self):
        StuRollno = self.textEdit_newsturoll.toPlainText()
        firstnm   = self.textEdit_newstufn.toPlainText()
        lastnm    = self.textEdit_newstuln.toPlainText()
        classnm   = self.comboBox_newstu_class.currentText()

        connection = sqlite3.connect("miniproject.db")
        try:
            # Create table as per requirement
            sql = """CREATE TABLE IF NOT EXISTS StudentsEntry( StuRollno INT NOT NULL, firstNm CHAR(20) NOT NULL, lastNm CHAR(20) NOT NULL, classNm TEXT)"""
            connection.execute(sql)
            connection.execute("INSERT INTO StudentsEntry VALUES(?,?,?,?)",(StuRollno, firstnm, lastnm, classnm))
            connection.commit()
            print("Data Added Successfully !")
        except Exception:

            print("Error in StudentEntryAddDetails !")
        connection.close()

    def setupUi(self, StudentEntry):
        StudentEntry.setObjectName("StudentEntry")
        StudentEntry.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(StudentEntry)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_NewStuEntry = QtWidgets.QFrame(self.centralwidget)
        self.frame_NewStuEntry.setGeometry(QtCore.QRect(0, 0, 1001, 681))
        self.frame_NewStuEntry.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.frame_NewStuEntry.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_NewStuEntry.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_NewStuEntry.setObjectName("frame_NewStuEntry")
        self.label_StuentryTitle = QtWidgets.QLabel(self.frame_NewStuEntry)
        self.label_StuentryTitle.setGeometry(QtCore.QRect(200, 20, 281, 51))
        self.label_StuentryTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_StuentryTitle.setObjectName("label_StuentryTitle")
        self.lbl_Rollno = QtWidgets.QLabel(self.frame_NewStuEntry)
        self.lbl_Rollno.setGeometry(QtCore.QRect(70, 110, 121, 41))
        self.lbl_Rollno.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Rollno.setObjectName("lbl_Rollno")
        self.label_LastNm = QtWidgets.QLabel(self.frame_NewStuEntry)
        self.label_LastNm.setGeometry(QtCore.QRect(70, 290, 121, 41))
        self.label_LastNm.setAlignment(QtCore.Qt.AlignCenter)
        self.label_LastNm.setObjectName("label_LastNm")
        self.lbl_fname = QtWidgets.QLabel(self.frame_NewStuEntry)
        self.lbl_fname.setGeometry(QtCore.QRect(70, 190, 121, 41))
        self.lbl_fname.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_fname.setObjectName("lbl_fname")
        self.lbl_class = QtWidgets.QLabel(self.frame_NewStuEntry)
        self.lbl_class.setGeometry(QtCore.QRect(70, 380, 121, 41))
        self.lbl_class.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_class.setObjectName("lbl_class")
        self.pushButton = QtWidgets.QPushButton(self.frame_NewStuEntry)
        self.pushButton.setGeometry(QtCore.QRect(220, 480, 131, 51))
        self.pushButton.setStyleSheet("font: 75 11pt \"Serif\";font: 15pt \"Ubuntu\";\n"
"background-color: rgb(238, 238, 236);")
        self.pushButton.setObjectName("pushButton")

        #Calling fuction after clicking button

        self.pushButton.clicked.connect(self.studententryadddetails)

        self.textEdit_newsturoll = QtWidgets.QTextEdit(self.frame_NewStuEntry)
        self.textEdit_newsturoll.setGeometry(QtCore.QRect(250, 90, 271, 70))
        self.textEdit_newsturoll.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.textEdit_newsturoll.setObjectName("textEdit_newsturoll")
        self.textEdit_newstufn = QtWidgets.QTextEdit(self.frame_NewStuEntry)
        self.textEdit_newstufn.setGeometry(QtCore.QRect(250, 180, 271, 70))
        self.textEdit_newstufn.setStyleSheet("\n"
"background-color: rgb(186, 189, 182);")
        self.textEdit_newstufn.setObjectName("textEdit_newstufn")
        self.textEdit_newstuln = QtWidgets.QTextEdit(self.frame_NewStuEntry)
        self.textEdit_newstuln.setGeometry(QtCore.QRect(250, 270, 271, 70))
        self.textEdit_newstuln.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.textEdit_newstuln.setObjectName("textEdit_newstuln")
        self.comboBox_newstu_class = QtWidgets.QComboBox(self.frame_NewStuEntry)
        self.comboBox_newstu_class.setGeometry(QtCore.QRect(250, 374, 271, 61))
        self.comboBox_newstu_class.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.comboBox_newstu_class.setObjectName("comboBox_newstu_class")
        self.comboBox_newstu_class.addItem("")
        self.comboBox_newstu_class.addItem("")
        self.comboBox_newstu_class.addItem("")
        self.comboBox_newstu_class.addItem("")
        StudentEntry.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StudentEntry)
        self.statusbar.setObjectName("statusbar")
        StudentEntry.setStatusBar(self.statusbar)

        self.retranslateUi(StudentEntry)
        QtCore.QMetaObject.connectSlotsByName(StudentEntry)

    def retranslateUi(self, StudentEntry):
        _translate = QtCore.QCoreApplication.translate
        StudentEntry.setWindowTitle(_translate("StudentEntry", "MainWindow"))
        self.label_StuentryTitle.setText(_translate("StudentEntry", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ef2929;\">NEW STUDENT ENTRY</span></p></body></html>"))
        self.lbl_Rollno.setText(_translate("StudentEntry", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Roll No</span></p></body></html>"))
        self.label_LastNm.setText(_translate("StudentEntry", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Last Name</span></p></body></html>"))
        self.lbl_fname.setText(_translate("StudentEntry", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">First Name</span></p></body></html>"))
        self.lbl_class.setText(_translate("StudentEntry", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Class</span></p></body></html>"))
        self.pushButton.setText(_translate("StudentEntry", "ADD"))
        self.comboBox_newstu_class.setItemText(0, _translate("StudentEntry", "Fy"))
        self.comboBox_newstu_class.setItemText(1, _translate("StudentEntry", "Sy"))
        self.comboBox_newstu_class.setItemText(2, _translate("StudentEntry", "Ty"))
        self.comboBox_newstu_class.setItemText(3, _translate("StudentEntry", "BE"))


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentEntry = QtWidgets.QMainWindow()
    ui = Ui_StudentEntry()
    ui.setupUi(StudentEntry)
    StudentEntry.show()
    sys.exit(app.exec_())
