# Form implementation generated from reading ui file 'NewClassEntry1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_NewClassEntry(object):


    def AddDetails(self):

        try:

            classname = self.textEdit_className.toPlainText()
            sub = self.textEdit_Subject.toPlainText()
            studroll = self.textEdit_st_rollno.toPlainText()
            db = sqlite3.connect("miniproject.db")


            # Create table as per requirement
            sql = """CREATE TABLE IF NOT EXISTS NewClassEntry (
                      ClassNm  CHAR(20) NOT NULL,
                      Sub_Name  CHAR(20) NOT NULL,
                      StartRollNo INT NOT NULL)"""
            db.execute(sql)

            inQuery = "INSERT INTO NewClassEntry VALUES('" + classname + "','" + sub + "'," + studroll + ") "
            db.execute(inQuery)
            db.commit()
            db.close()



        except Exception:
            print("Error While Adding")


    def setupUi(self, NewClassEntry):


        NewClassEntry.setObjectName("NewClassEntry")
        NewClassEntry.resize(800, 600)
        NewClassEntry.setStyleSheet("color: rgb(136, 138, 133);\n"
"background-color: rgb(85, 87, 83);")
        self.centralwidget = QtWidgets.QWidget(NewClassEntry)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-90, 0, 961, 801))
        self.frame.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_NewEntry_add = QtWidgets.QPushButton(self.frame)
        self.pushButton_NewEntry_add.setGeometry(QtCore.QRect(400, 460, 121, 41))
        self.pushButton_NewEntry_add.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Serif\";font: 15pt \"Ubuntu\";")
        self.pushButton_NewEntry_add.setObjectName("pushButton_NewEntry_add")
        self.textEdit_Subject = QtWidgets.QTextEdit(self.frame)
        self.textEdit_Subject.setGeometry(QtCore.QRect(460, 260, 211, 61))
        self.textEdit_Subject.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 15pt \"Serif\";")
        self.textEdit_Subject.setObjectName("textEdit_Subject")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(170, 140, 131, 17))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_startrollno = QtWidgets.QLabel(self.frame)
        self.label_startrollno.setGeometry(QtCore.QRect(250, 370, 141, 31))
        self.label_startrollno.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_startrollno.setAlignment(QtCore.Qt.AlignCenter)
        self.label_startrollno.setObjectName("label_startrollno")
        self.label_classname = QtWidgets.QLabel(self.frame)
        self.label_classname.setGeometry(QtCore.QRect(210, 200, 191, 31))
        self.label_classname.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_classname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_classname.setObjectName("label_classname")
        self.label_subject = QtWidgets.QLabel(self.frame)
        self.label_subject.setGeometry(QtCore.QRect(240, 280, 141, 31))
        self.label_subject.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_subject.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subject.setObjectName("label_subject")
        self.textEdit_className = QtWidgets.QTextEdit(self.frame)
        self.textEdit_className.setGeometry(QtCore.QRect(460, 180, 211, 61))
        self.textEdit_className.setStyleSheet("background-color: rgb(186, 189, 182);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 15pt \"Serif\";")
        self.textEdit_className.setObjectName("textEdit_className")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 80, 321, 41))
        self.label.setObjectName("label")
        self.textEdit_st_rollno = QtWidgets.QTextEdit(self.frame)
        self.textEdit_st_rollno.setGeometry(QtCore.QRect(460, 350, 211, 61))
        self.textEdit_st_rollno.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(186, 189, 182);\n"
"font: 75 15pt \"Serif\";")
        self.textEdit_st_rollno.setObjectName("textEdit_st_rollno")
        NewClassEntry.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewClassEntry)
        self.statusbar.setObjectName("statusbar")
        NewClassEntry.setStatusBar(self.statusbar)

        self.retranslateUi(NewClassEntry)
        QtCore.QMetaObject.connectSlotsByName(NewClassEntry)

    def retranslateUi(self, NewClassEntry):
        _translate = QtCore.QCoreApplication.translate
        NewClassEntry.setWindowTitle(_translate("NewClassEntry", "MainWindow"))
#ADDDDDDDDDDDDDDDDDDDDDDD
        self.pushButton_NewEntry_add.setText(_translate("NewClassEntry", "ADD"))
        self.pushButton_NewEntry_add.clicked.connect(self.AddDetails)

        self.label_startrollno.setText(_translate("NewClassEntry", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Start Roll_No</span></p></body></html>"))
        self.label_classname.setText(_translate("NewClassEntry", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Class Name</span></p></body></html>"))
        self.label_subject.setText(_translate("NewClassEntry", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Subjects</span></p></body></html>"))
        self.label.setText(_translate("NewClassEntry", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ef2929;\">NEW CLASS ENTRY</span></p></body></html>"))


if __name__ == "__main__":


    try:


        import sys

        app = QtWidgets.QApplication(sys.argv)
        NewClassEntry = QtWidgets.QMainWindow()
        ui = Ui_NewClassEntry()
        ui.setupUi(NewClassEntry)
        NewClassEntry.show()
        sys.exit(app.exec_())
    except Exception:

        print("Error During Connection DB")


