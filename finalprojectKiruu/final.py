from PyQt5 import QtCore, QtGui, QtWidgets
from NewOtherWindow import Ui_Form
#from newclassentry import Ui_MainWindow
from studentEntryform import Ui_StudentEntry
from NewClassEntry1 import Ui_NewClassEntry
import sqlite3


class Ui_MainWindow(object):

    def openWindow(self):

        username = self.textEdit_userrnm.toPlainText()
        password = self.textEdit_passwd.toPlainText()

        connection = sqlite3.connect("miniproject.db")
        result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD = ?", (username, password))
        if (len(result.fetchall()) > 0):
            print("User Found ! ")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Form()
            self.ui.setupUi(self.window)
            MainWindow.hide()
            self.window.show()


        else:
            print("User Not Found !")
           # self.showMessageBox('Warning', 'Invalid Username And Password')
        connection.close()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(973, 657)
        MainWindow.setMinimumSize(QtCore.QSize(973, 0))
        MainWindow.setMaximumSize(QtCore.QSize(973, 657))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/LoginPage.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submit_homelogin = QtWidgets.QPushButton(self.centralwidget)
        self.submit_homelogin.setGeometry(QtCore.QRect(620, 500, 161, 51))
        self.submit_homelogin.setObjectName("submit_homelogin")
        self.label_usernm = QtWidgets.QLabel(self.centralwidget)
        self.label_usernm.setGeometry(QtCore.QRect(510, 350, 121, 41))
        self.label_usernm.setObjectName("label_usernm")
        self.textEdit_userrnm = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_userrnm.setGeometry(QtCore.QRect(690, 350, 211, 41))
        self.textEdit_userrnm.setObjectName("textEdit_userrnm")
        self.textEdit_passwd = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_passwd.setGeometry(QtCore.QRect(690, 420, 211, 41))
        self.textEdit_passwd.setObjectName("textEdit_passwd")
        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setEnabled(True)
        self.label_pass.setGeometry(QtCore.QRect(510, 420, 121, 41))
        self.label_pass.setObjectName("label_pass")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submit_homelogin.setText(_translate("MainWindow", "Login"))

        self.submit_homelogin.clicked.connect(self.openWindow)

        self.label_usernm.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#a40000;\">Username</span></p></body></html>"))
        self.textEdit_userrnm.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_pass.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#a40000;\">Password</span></p></body></html>"))
import LoginImage_rc


if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
