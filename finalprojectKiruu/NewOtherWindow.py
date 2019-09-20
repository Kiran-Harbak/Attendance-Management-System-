from PyQt5 import QtCore, QtGui, QtWidgets
from NewAttendance import Ui_newattendance
from studentEntryform import Ui_StudentEntry
#from newclassentry import Ui_StudentEntry
from NewClassEntry1 import Ui_NewClassEntry
from reports import Ui_Form1

class Ui_Form(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_newattendance()
        self.ui.setupUi(self.window)
        # Form.hide()
        self.window.show()

    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StudentEntry()
        self.ui.setupUi(self.window)
        # Form.hide()
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_NewClassEntry()
        self.ui.setupUi(self.window)
        # Form.hide()
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form1()
        self.ui.setupUi(self.window)
        # Form.hide()
        self.window.show()




    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(955, 792)
        Form.setStyleSheet("background-image: url(:/newPrefix/MainForm.jpg);")
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_Enroll_stu_report = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enroll_stu_report.setGeometry(QtCore.QRect(100, 190, 301, 91))
        self.pushButton_Enroll_stu_report.setStyleSheet("font: 75 15pt \"Serif\";")
        self.pushButton_Enroll_stu_report.setObjectName("pushButton_Enroll_stu_report")

        self.pushButton_Enroll_stu_report.clicked.connect(self.openWindow3)



        self.pushButton__Enroll_newattdace = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton__Enroll_newattdace.setGeometry(QtCore.QRect(560, 190, 301, 91))
        self.pushButton__Enroll_newattdace.setStyleSheet("font: 75 15pt \"Serif\";")
        self.pushButton__Enroll_newattdace.setObjectName("pushButton__Enroll_newattdace")

        self.pushButton__Enroll_newattdace.clicked.connect(self.openWindow)


        self.pushButton_Enroll_new_stu_entry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enroll_new_stu_entry.setGeometry(QtCore.QRect(100, 430, 301, 91))
        self.pushButton_Enroll_new_stu_entry.setStyleSheet("font: 75 15pt \"Serif\";")
        self.pushButton_Enroll_new_stu_entry.setObjectName("pushButton_Enroll_new_stu_entry")

        self.pushButton_Enroll_new_stu_entry.clicked.connect(self.openWindow1)


        self.pushButton_Enroll_create_newcls = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Enroll_create_newcls.setGeometry(QtCore.QRect(560, 430, 301, 91))
        self.pushButton_Enroll_create_newcls.setStyleSheet("font: 75 15pt \"Serif\";")
        self.pushButton_Enroll_create_newcls.setObjectName("pushButton_Enroll_create_newcls")

        self.pushButton_Enroll_create_newcls.clicked.connect(self.openWindow2)

        Form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Enroll_stu_report.setText(_translate("Form", "REPORT GENERATION"))
        self.pushButton__Enroll_newattdace.setText(_translate("Form", "NEW ATTENDANCE"))
        self.pushButton_Enroll_new_stu_entry.setText(_translate("Form", "NEW STUDENT ENTRY"))
        self.pushButton_Enroll_create_newcls.setText(_translate("Form", "CREATE NEW CLASS"))

import Form_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
